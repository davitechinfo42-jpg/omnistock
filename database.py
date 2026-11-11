import re

import streamlit as st
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    delete,
    func,
    insert,
    select,
)
from sqlalchemy.engine import URL
from sqlalchemy.exc import IntegrityError

from auth import verificar_senha

# LEMBRETE: preencher com as informações de conexão do banco de dados (dialect, ex.: "postgresql+psycopg2" ou "mysql+pymysql"; host; port; user; password; database).
DB_CONFIG = {
    "dialect": "sqlite",
    "database": "estoque_2050.db"
}

metadata = MetaData()

usuarios = Table(
    "usuarios",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("usuario", String(50), nullable=False, unique=True),
    Column("email", String(255), unique=True),
    Column("senha_hash", String(255)),
    Column("criado_em", DateTime, server_default=func.now()),
)

lista_compras = Table(
    "lista_compras",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "usuario_id",
        Integer,
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    ),
    Column("nome", String(120), nullable=False),
    Column("quantidade", Integer, nullable=False, default=1),
)


class UsuarioExistente(Exception):
    pass


@st.cache_resource
def get_engine():
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///estoque_2050.db", connect_args={'check_same_thread': False})
    metadata.create_all(engine)
    return engine


def _como_dict(linha):
    return {"id": linha.id, "usuario": linha.usuario, "email": linha.email}


def criar_usuario(usuario, senha_hash, email=None):
    with get_engine().begin() as conn:
        existe = conn.execute(
            select(usuarios.c.id).where(func.lower(usuarios.c.usuario) == usuario.lower())
        ).first()
        if existe:
            raise UsuarioExistente(usuario)
        try:
            resultado = conn.execute(
                insert(usuarios).values(usuario=usuario, email=email, senha_hash=senha_hash)
            )
        except IntegrityError as erro:
            raise UsuarioExistente(usuario) from erro
    return {"id": resultado.inserted_primary_key[0], "usuario": usuario, "email": email}


def autenticar(usuario, senha):
    with get_engine().connect() as conn:
        linha = conn.execute(
            select(usuarios).where(func.lower(usuarios.c.usuario) == usuario.lower())
        ).first()
    if linha is None or not linha.senha_hash:
        return None
    if not verificar_senha(senha, linha.senha_hash):
        return None
    return _como_dict(linha)


def _buscar_por_email(email):
    with get_engine().connect() as conn:
        linha = conn.execute(
            select(usuarios).where(func.lower(usuarios.c.email) == email.lower())
        ).first()
    return _como_dict(linha) if linha else None


def usuario_google(email, nome=None):
    existente = _buscar_por_email(email)
    if existente:
        return existente
    base = re.sub(r"[^A-Za-z0-9_.-]", "", (nome or email.split("@")[0]).replace(" ", ""))
    base = (base or "usuario")[:24]
    candidato = base
    for tentativa in range(2, 52):
        try:
            return criar_usuario(candidato, None, email)
        except UsuarioExistente:
            existente = _buscar_por_email(email)
            if existente:
                return existente
            candidato = f"{base}{tentativa}"
    raise UsuarioExistente(base)


def listar_compras(usuario_id):
    consulta = (
        select(lista_compras.c.id, lista_compras.c.nome, lista_compras.c.quantidade)
        .where(lista_compras.c.usuario_id == usuario_id)
        .order_by(lista_compras.c.id)
    )
    with get_engine().connect() as conn:
        return [dict(linha._mapping) for linha in conn.execute(consulta)]


def adicionar_compra(usuario_id, nome, quantidade):
    with get_engine().begin() as conn:
        conn.execute(
            insert(lista_compras).values(usuario_id=usuario_id, nome=nome, quantidade=quantidade)
        )


def remover_compra(usuario_id, item_id):
    with get_engine().begin() as conn:
        conn.execute(
            delete(lista_compras).where(
                lista_compras.c.id == item_id, lista_compras.c.usuario_id == usuario_id
            )
        )


def listar_estoque(categoria=None):
    import sqlite3
    conexao = sqlite3.connect("estoque_2050.db")
    cursor = conexao.cursor()
    
    if categoria and categoria.lower() != "todos":
        # Envolve a categoria com % para ignorar problemas de acentuação exata ou espaços soltos
        cursor.execute("SELECT id, nome, quantidade, categoria FROM produtos WHERE categoria LIKE ?", (f"%{categoria}%",))
    else:
        cursor.execute("SELECT id, nome, quantidade, categoria FROM produtos ORDER BY nome")
        
    linhas = cursor.fetchall()
    conexao.close()
    
    return [{"id": linha[0], "nome": linha[1], "quantidade": linha[2], "categoria": linha[3]} for linha in linhas]

def alterar_quantidade(item_id, delta):
    import sqlite3
    conexao = sqlite3.connect("estoque_2050.db")
    cursor = conexao.cursor()
    # Usa MAX(0) para garantir que ninguém deixe o estoque negativo
    cursor.execute("UPDATE produtos SET quantidade = MAX(0, quantidade + ?) WHERE id = ?", (delta, item_id))
    conexao.commit()
    conexao.close()

def remover_produto(item_id):
    import sqlite3
    conexao = sqlite3.connect("estoque_2050.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (item_id,))
    conexao.commit()
    conexao.close()