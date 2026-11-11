import streamlit as st

import database


def usuario_atual():
    return st.session_state.get("usuario")


def entrar(dados):
    st.session_state["usuario"] = dados


def exigir_login():
    dados = usuario_atual()
    if dados is None:
        st.switch_page("views/login.py")
    return dados


def redirecionar_se_logado():
    if usuario_atual() is not None:
        st.switch_page("views/home.py")


def identidade_google():
    try:
        if st.user.is_logged_in:
            email = getattr(st.user, "email", None)
            if email:
                return {"email": email, "nome": getattr(st.user, "name", None)}
    except Exception:
        return None
    return None


def sincronizar_google():
    if usuario_atual() is None:
        identidade = identidade_google()
        if identidade:
            entrar(database.usuario_google(identidade["email"], identidade["nome"]))


def iniciar_google():
    try:
        st.login("google")
    except Exception:
        st.error("Login com Google não configurado. Veja .streamlit/secrets.toml.example.")


def sair():
    google = identidade_google() is not None
    st.session_state.clear()
    if google:
        st.logout()
    st.switch_page("views/login.py")
