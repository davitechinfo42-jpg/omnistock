import sqlite3
import bcrypt
import re

BANCO = "estoque_2050.db"

PADRAO_USUARIO = re.compile(r"^[A-Za-z0-9_.-]{3,30}$")


def conectar_banco():
    """Conecta ao SQLite e garante que a tabela de usuários exista."""
    conexao = sqlite3.connect(BANCO, check_same_thread=False)
    conexao.row_factory = sqlite3.Row  
    
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)
    conexao.commit()
    return conexao

def validar_cadastro(usuario, senha, repetir):
    """Função original do Marcelo para validar as regras de formulário na tela."""
    erros = []
    if not PADRAO_USUARIO.fullmatch(usuario.strip()):
        erros.append("O usuário deve ter de 3 a 30 caracteres, usando letras, números, ponto, hífen ou sublinhado.")
    
    if len(senha) < 6:
        erros.append("A senha deve ter pelo menos 6 caracteres.")
    elif senha != repetir:
        erros.append("As senhas não coincidem.")
        
    return erros

def gerar_hash(senha: str) -> str:
    """Função de compatibilidade exigida pela tela de cadastro antiga usando bcrypt."""
    return bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

def cadastrar_usuario(nome: str, email: str, senha: str) -> tuple[bool, str]:
    """Salva no SQLite e retorna Tupla para o Streamlit ler."""
    nome = nome.strip()
    email = email.strip().lower()

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        senha_hash = bcrypt.hashpw(
            senha.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        comando = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)"
        cursor.execute(comando, (nome, email, senha_hash))
        conexao.commit()

        return True, "Usuário cadastrado com sucesso!"

    except sqlite3.IntegrityError:
        return False, "Não foi possível cadastrar: e-mail já registrado."
    except Exception as erro:
        return False, f"Erro ao cadastrar usuário: {erro}"
    finally:
        conexao.close()


def autenticar_usuario(email: str, senha: str) -> tuple[bool, str]:
    """Verifica login no SQLite e retorna Tupla para o Streamlit."""
    email = email.strip().lower()

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        comando = "SELECT id, nome, email, senha FROM usuarios WHERE email = ?"
        cursor.execute(comando, (email,))
        usuario = cursor.fetchone()

        if usuario is None:
            return False, "E-mail ou senha incorretos."

        nome_usuario = usuario["nome"]
        hash_armazenado = usuario["senha"]

        senha_correta = bcrypt.checkpw(
            senha.encode("utf-8"),
            hash_armazenado.encode("utf-8")
        )

        if senha_correta:
            return True, f"Login realizado! Bem-vindo, {nome_usuario}!"
        else:
            return False, "E-mail ou senha incorretos."

    except Exception as erro:
        return False, f"Erro durante a autenticação: {erro}"
    finally:
        conexao.close()

def verificar_senha(senha: str, armazenado: str) -> bool:
    """Função de compatibilidade exigida pelo database.py usando bcrypt."""
    try:
        return bcrypt.checkpw(senha.encode("utf-8"), armazenado.encode("utf-8"))
    except Exception:
        return False