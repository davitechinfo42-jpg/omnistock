from html import escape
import streamlit as st
import database
import state
import ui
import crud_estoque  

state.exigir_login()
ui.tema("app")

CATEGORIAS = {"Todos": None, "Higiene": "Higiene", "Alimentação": "Alimentação", "Limpeza": "Limpeza"}

def alterar_qtd(item_id, delta):
    database.alterar_quantidade(item_id, delta)

def remover_item(item_id):
    database.remover_produto(item_id)

def abrir_novo_produto():
    st.session_state["add_estoque"] = True

def fechar_novo_produto():
    st.session_state["add_estoque"] = False

ui.topo("Profile", "views/perfil.py")

with st.container(key="filtro"):
    col_add, col_filt = st.columns([1.2, 1])
    with col_add:
        st.button("➕ Novo Produto", on_click=abrir_novo_produto, use_container_width=True)
    with col_filt:
        with st.popover("Filtro"):
            escolha = st.radio("Categoria", list(CATEGORIAS), key="filtro_estoque")

if st.session_state.get("add_estoque", False):
    with st.form("form_novo_estoque"):
        st.write("📦 **Entrada de Novo Produto**")
        
        nome = st.text_input("Nome do Produto")
        categoria = st.selectbox("Categoria", ["Alimentação", "Higiene", "Limpeza"])
        
        col1, col2 = st.columns(2)
        qtd = col1.number_input("Quantidade Atual", min_value=1, value=1)
        minimo = col2.number_input("Estoque Mínimo", min_value=1, value=1)
        
        col3, col4 = st.columns(2)
        consumo = col3.number_input("Consumo Diário", min_value=0.01, value=0.1, step=0.1)
        validade = col4.date_input("Data de Validade")
        
        col_salvar, col_cancel = st.columns(2)
        
        if col_salvar.form_submit_button("Salvar no Estoque"):
            if nome.strip():
                val_str = validade.strftime("%Y-%m-%d")
                crud_estoque.cadastrar_produto(nome, categoria, qtd, minimo, consumo, val_str)
                st.session_state["add_estoque"] = False
                st.rerun() 
            else:
                st.error("Preencha o nome do produto.")
                
        col_cancel.form_submit_button("Cancelar", on_click=fechar_novo_produto)

if CATEGORIAS[escolha]:
    st.html(f'<p class="filtro-ativo">Mostrando: {escape(escolha)}</p>')

itens = database.listar_estoque(CATEGORIAS[escolha])

if itens:
    for item in itens:
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
        with col1:
            st.markdown(f"**{escape(item['nome'])}**")
        with col2:
            st.write(f"{item['quantidade']} un")
        with col3:
            st.button("➖", key=f"menos_{item['id']}", on_click=alterar_qtd, args=(item['id'], -1))
        with col4:
            st.button("➕", key=f"mais_{item['id']}", on_click=alterar_qtd, args=(item['id'], 1))
        with col5:
            st.button("🗑️", key=f"del_{item['id']}", on_click=remover_item, args=(item['id'],))
else:
    st.html('<p class="vazio">Nenhum item encontrado no estoque.</p>')

ui.rodape(("Home", "views/home.py"), ("Lista de compras", "views/lista.py"))