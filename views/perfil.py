
from html import escape

import streamlit as st

import state
import ui

dados = state.exigir_login()
ui.tema("app")

st.html("""
<style>
.st-key-perfil {
    position: relative !important;
    left: auto !important;
    transform: none !important;
    width: min(340px, calc(100vw - 2rem)) !important;
    margin-left: auto !important;
    margin-right: auto !important;
    gap: .3rem !important;
}

.st-key-perfil > div {
    width: 100% !important;
}

.st-key-perfil .perfil-avatar {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: .2rem 0 .4rem;
}

.st-key-perfil .perfil-avatar svg {
    width: 96px;
    height: 96px;
    display: block;
    filter: drop-shadow(0 8px 16px rgba(0,0,40,.6));
}

.st-key-perfil .pilula {
    width: 100%;
    box-sizing: border-box;
    text-align: center;
}

.st-key-perfil [data-testid="stButton"] {
    display: flex;
    justify-content: center;
    width: 100%;
}

.st-key-perfil [class*="st-key-link_"] button {
    width: auto !important;
    min-height: 0 !important;
    padding: .15rem .4rem !important;
    background: none !important;
    box-shadow: none !important;
    color: #b4c0ff !important;
    text-decoration: underline !important;
    font-size: .74rem !important;
}

.st-key-perfil [class*="st-key-link_"] button:hover {
    background: none !important;
    color: #fff !important;
}

.st-key-perfil .st-key-senha_botao button {
    width: auto !important;
}

.st-key-perfil [data-testid="stPopover"] {
    width: 100% !important;
}

.st-key-perfil [data-testid="stPopover"] button {
    width: 100% !important;
}

.st-key-perfil .st-key-senha_botao,
.st-key-perfil .st-key-celular_botao {
    margin-top: .7rem;
}
</style>
""")

ui.topo("Home", "views/home.py")

email = dados.get("email")

with st.container(key="perfil"):

    st.html(
        f'<div class="perfil-avatar">{ui.avatar_svg("#0a0e4a")}</div>'
    )

    st.html(
        f'<div class="pilula">{escape(dados["usuario"])}</div>'
    )

    if st.button("Change username", key="link_alterar_usuario"):
        ui.em_desenvolvimento()

    st.html(
        f'<div class="pilula">'
        f'{escape(email) if email else "No email linked"}'
        f'</div>'
    )

    if st.button(
        "Verified" if email else "Add email",
        key="link_email"
    ):
        ui.em_desenvolvimento()

    if st.button("Change password", key="senha_botao"):
        ui.em_desenvolvimento()

    if st.button("Delete account", key="link_excluir_conta"):
        ui.em_desenvolvimento()

    with st.popover(
        "📱 Link your smartphone",
        use_container_width=True
    ):
        st.markdown("**Sincronização OmniStock Mobile**")

        st.caption(
            "Escaneie o QR Code com a câmera do celular:"
        )

        st.image(
            "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://10.219.219.108:8504",
            width=150
        )

        st.info(
            "Aguardando dispositivo na rede local..."
        )

    if st.button(
        "Change link",
        key="link_alterar_celular"
    ):
        ui.em_desenvolvimento()

    if st.button("Sair", key="link_sair"):
        state.sair()

ui.rodape(
    ("Estoque", "views/estoque.py"),
    ("Lista de compras", "views/lista.py")
)
