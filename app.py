import streamlit as st

st.set_page_config(page_title="Omnistock", page_icon="🏠", layout="wide")

import database
import state

try:
    database.get_engine()
except Exception as erro:
    st.error("Não foi possível conectar ao banco de dados. Preencha as informações de conexão em database.py.")
    st.caption(str(erro))
    st.stop()

state.sincronizar_google()

pagina = st.navigation(
    [
        st.Page("views/login.py", title="Login", url_path="login", default=True),
        st.Page("views/cadastro.py", title="Cadastro", url_path="cadastro"),
        st.Page("views/home.py", title="Home", url_path="home"),
        st.Page("views/perfil.py", title="Profile", url_path="perfil"),
        st.Page("views/lista.py", title="Lista de compras", url_path="lista-de-compras"),
        st.Page("views/estoque.py", title="Estoque", url_path="estoque"),
    ],
    position="hidden",
)
pagina.run()
