import streamlit as st

import auth
import database
import state
import ui

state.redirecionar_se_logado()
ui.tema("auth")

with st.container(key="auth_panel"):

    ui.cabecalho_auth()

    with st.form("form_cadastro"):

        usuario = st.text_input(
            "Username",
            key="cadastro_usuario"
        )

        senha = st.text_input(
            "Password",
            type="password",
            key="cadastro_senha"
        )

        repetir = st.text_input(
            "Repeat password",
            type="password",
            key="cadastro_repetir"
        )

        st.html('<div class="auth-linha"></div>')

        col1, col2, col3 = st.columns([0.6, 2.8, 0.6])

        with col2:
            enviar = st.form_submit_button(
                "Cadastrar",
                use_container_width=True
            )

    if enviar:
        erros = auth.validar_cadastro(
            usuario, senha, repetir
        )

        if erros:
            st.error("\n\n".join(erros))
        else:
            try:
                dados = database.criar_usuario(
                    usuario.strip(),
                    auth.gerar_hash(senha)
                )
            except database.UsuarioExistente:
                st.error("Este usuário já está em uso.")
            else:
                state.entrar(dados)
                st.switch_page("views/home.py")

    # Botões centralizados dentro do card
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "Entrar com Google",
            key="google_login",
            use_container_width=True
        ):
            state.iniciar_google()

        if st.button(
            "Já tem uma conta?",
            key="link_ja_tenho_conta",
            use_container_width=True
        ):
            st.switch_page("views/login.py")