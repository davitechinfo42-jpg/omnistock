import streamlit as st

import database
import state
import ui

state.redirecionar_se_logado()
ui.tema("auth")

with st.container(key="auth_panel"):

    ui.cabecalho_auth()

    with st.form("form_login"):

        usuario = st.text_input(
            "Username",
            key="login_usuario"
        )

        senha = st.text_input(
            "Password",
            type="password",
            key="login_senha"
        )

        st.html(
            '<div class="auth-link">Forgot your password?</div>'
        )

        enviar = st.form_submit_button(
            "Login",
            use_container_width=True
        )

    if enviar:
        if not usuario.strip() or not senha:
            st.error("Informe o usuário e a senha.")
        else:
            dados = database.autenticar(usuario.strip(), senha)

            if dados is None:
                st.error("Usuário ou senha incorretos.")
            else:
                state.entrar(dados)
                st.switch_page("views/home.py")

    # Botões dentro do card
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button(
            "Entrar com Google",
            key="google_login",
            use_container_width=True
        ):
            state.iniciar_google()

        if st.button(
            "Novo usuário",
            key="link_novo_usuario",
            use_container_width=True
        ):
            st.switch_page("views/cadastro.py")