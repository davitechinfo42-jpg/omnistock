import sqlite3
from datetime import datetime

BANCO = "estoque_2050.db"

def conectar():
    """Cria a conexão e configura para retornar dicionários, facilitando para o Streamlit."""
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row 
    return conexao

def criar_tabelas():
    """Gera a estrutura do banco de dados na primeira execução."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            estoque_minimo INTEGER NOT NULL DEFAULT 1,
            consumo_diario REAL NOT NULL DEFAULT 0.1,
            data_validade TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            nome_produto TEXT NOT NULL,
            quantidade_retirada INTEGER NOT NULL,
            data_movimentacao TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def listar_produtos():
    """Retorna todos os produtos como uma lista de dicionários."""
    criar_tabelas()
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM produtos")
    produtos = [dict(row) for row in cursor.fetchall()]
    
    conexao.close()
    return produtos

def cadastrar_produto(nome, categoria, quantidade, estoque_minimo, consumo_diario, validade):
    """Recebe os dados do Streamlit e salva no banco sem usar input()."""
    criar_tabelas()
    
    if quantidade < 0:
        return False, "A quantidade inicial não pode ser negativa."

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO produtos 
            (nome, categoria, quantidade, estoque_minimo, consumo_diario, data_validade)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome.strip(), categoria.strip(), int(quantidade), int(estoque_minimo), float(consumo_diario), validade))
        
        conexao.commit()
        return True, "Produto cadastrado com sucesso!"
    except Exception as e:
        return False, f"Erro ao cadastrar: {e}"
    finally:
        conexao.close()

def dar_baixa_estoque(produto_id, quantidade_baixa):
    """Subtrai o estoque e registra o histórico silenciosamente."""
    criar_tabelas()
    
    if int(quantidade_baixa) <= 0:
        return False, "A quantidade para baixa deve ser maior que zero."

    conexao = conectar()
    cursor = conexao.cursor()

    # Busca o saldo atual
    cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if not produto:
        conexao.close()
        return False, "Produto não encontrado."

    nome_produto = produto["nome"]
    saldo_atual = produto["quantidade"]

    if quantidade_baixa > saldo_atual:
        conexao.close()
        return False, f"Estoque insuficiente. Saldo atual: {saldo_atual}."

    novo_saldo = saldo_atual - quantidade_baixa
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (novo_saldo, produto_id))

    cursor.execute("""
        INSERT INTO historico (produto_id, nome_produto, quantidade_retirada, data_movimentacao)
        VALUES (?, ?, ?, ?)
    """, (produto_id, nome_produto, quantidade_baixa, data_hora_atual))

    conexao.commit()
    conexao.close()
    
    return True, f"Baixa registrada! Novo saldo de {nome_produto}: {novo_saldo}"

def deletar_produto(produto_id):
    """Remove um produto do estoque."""
    criar_tabelas()
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    
    cursor.execute("UPDATE historico SET produto_id = NULL WHERE produto_id = ?", (produto_id,))
    
    conexao.commit()
    conexao.close()
    return True, "Produto deletado com sucesso."

def listar_estoque(categoria=None):
    """Função de compatibilidade para atender views que chamam listar_estoque."""
    return listar_produtos()