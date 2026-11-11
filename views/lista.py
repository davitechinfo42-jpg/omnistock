
from html import escape

import streamlit as st

import database
import state
import ui

dados = state.exigir_login()
ui.tema("app")


def abrir_novo():
    st.session_state["novo_item"] = True


def cancelar_novo():
    st.session_state["novo_item"] = False
    st.session_state.pop("novo_nome", None)
    st.session_state.pop("novo_qtd", None)


def salvar_novo():
    nome = st.session_state.get("novo_nome", "").strip()

    if not nome:
        st.toast("Digite o nome do item.", icon="⚠️")
        return

    database.adicionar_compra(
        dados["id"],
        nome,
        int(st.session_state.get("novo_qtd", 1))
    )

    cancelar_novo()


def remover(item_id):
    database.remover_compra(dados["id"], item_id)


ui.topo("Profile", "views/perfil.py")

with st.container(key="lista"):

    itens = database.listar_compras(dados["id"])

    col_esquerda, col_add, col_baixar = st.columns([1, 1, 1])

    with col_add:
        st.button(
            "Adicionar",
            key="adicionar",
            on_click=abrir_novo,
            use_container_width=True
        )

    with col_baixar:
        if itens:
            texto = (
                "LISTA DE COMPRAS - OMNISTOCK 2050\n"
                "=================================\n\n"
            )

            for item in itens:
                texto += f"• {item['nome']} (Qtd: {item['quantidade']})\n"

            st.download_button(
                label="Baixar Lista",
                data=texto,
                file_name="minha_lista_compras.txt",
                mime="text/plain",
                use_container_width=True
            )

    adicionando = st.session_state.get("novo_item", False)

    if adicionando:
        col_nome, col_qtd, col_salvar, col_cancelar = st.columns(
            [3, 1.2, 1, 1]
        )

        col_nome.text_input(
            "Nome do item",
            key="novo_nome",
            placeholder="Nome do item",
            label_visibility="collapsed"
        )

        col_qtd.number_input(
            "Quantidade",
            min_value=1,
            value=1,
            step=1,
            key="novo_qtd",
            label_visibility="collapsed"
        )

        col_salvar.button(
            "Salvar",
            key="link_salvar",
            on_click=salvar_novo
        )

        col_cancelar.button(
            "Cancelar",
            key="link_cancelar",
            on_click=cancelar_novo
        )

    for item in itens:
        col_nome, col_qtd, col_remover = st.columns([3, 1.2, 2])

        col_nome.html(
            f'<span class="lista-nome">{escape(item["nome"])}</span>'
        )

        col_qtd.html(
            f'<span class="lista-qtd">{item["quantidade"]}</span>'
        )

        col_remover.button(
            "Remover",
            key=f"link_remover_{item['id']}",
            on_click=remover,
            args=(item["id"],)
        )

    if not itens and not adicionando:
        st.html(
            '<p class="vazio">'
            'Sua lista está vazia. Use Adicionar para incluir o primeiro item.'
            '</p>'
        )

ui.rodape(
    ("Estoque", "views/estoque.py"),
    ("Home", "views/home.py")
)
