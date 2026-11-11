
from urllib.parse import quote

import streamlit as st


TAGLINE = "Omnistock, o melhor para facilitar suas compras e controle de estoque!"

GOOGLE_G = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
    '<path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>'
    '<path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>'
    '<path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>'
    '<path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/>'
    "</svg>"
)

GOOGLE_URI = "data:image/svg+xml;utf8," + quote(GOOGLE_G)

CASA_SVG = (
    '<svg viewBox="0 0 160 160" fill="none" stroke="#3d5bff" stroke-width="3" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M16 80 80 22l64 58"/>'
    '<path d="M112 44V30h14v28"/>'
    '<path d="M30 68v72h100V68"/>'
    '<rect x="62" y="64" width="36" height="64" rx="6"/>'
    '<path d="M74 72h12"/>'
    '<path d="M69 92q11-9 22 0M74 98q6-5 12 0"/>'
    '<circle cx="80" cy="104" r="1.6" fill="#3d5bff"/>'
    '<path d="M68 118h10"/><circle cx="85" cy="118" r="3"/>'
    "</svg>"
)

LOGO = '<span class="logo">OmniStock</span>'


BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,700&display=swap');

:root{
    --texto:#dfe6ff;
    --suave:#b4c0ff;
    --botao-a:#0b0f52;
    --botao-b:#060839;
    --botao-hover:#151b86;
    --acento-a:#5a6cf0;
    --acento-b:#3745bd;
}

html,body,.stApp,input,button,textarea,label,p,a,
[data-testid="stMarkdownContainer"]{
    font-family:'Lora',Georgia,serif;
}

.stApp{
    color:var(--texto);
}

header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"],
footer{
    display:none!important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"]{
    background:transparent!important;
    position:relative;
    z-index:1;
}

.stElementContainer:has(style){
    display:none;
}

.block-container,
[data-testid="stMainBlockContainer"]{
    max-width:980px;
    padding:1.4rem 1.5rem 9rem!important;
}

[data-testid="stHorizontalBlock"]{
    flex-wrap:nowrap!important;
    align-items:center;
    gap:.6rem;
}

[data-testid="stColumn"]{
    min-width:0!important;
}

[data-testid="stForm"]{
    border:none!important;
    padding:0!important;
    background:transparent!important;
}

[data-testid="stWidgetLabel"] p{
    font-size:.74rem;
    color:var(--texto);
}

[data-baseweb="input"],
[data-baseweb="base-input"]{
    background:rgba(4,10,66,.8)!important;
    border-radius:8px!important;
    border-color:transparent!important;
}

[data-baseweb="input"]:focus-within{
    box-shadow:0 0 0 1px rgba(160,180,255,.75)!important;
}

[data-baseweb="input"] input{
    color:#fff!important;
    -webkit-text-fill-color:#fff!important;
    background:transparent!important;
    font-size:.88rem;
}

[data-baseweb="input"] button,
[data-testid="stNumberInputStepDown"],
[data-testid="stNumberInputStepUp"]{
    background:transparent!important;
    color:var(--suave)!important;
}

[data-testid="stPopover"]{
    width:100%;
}

[data-testid="stButton"] button,
[data-testid="stFormSubmitButton"] button,
[data-testid="stPopover"] button{
    width:100%;
    min-height:2.6rem;
    border:none!important;
    border-radius:9px;
    background:linear-gradient(180deg,var(--botao-a),var(--botao-b));
    color:var(--texto);
    font-size:.85rem;
    box-shadow:0 8px 18px rgba(0,0,40,.55);
    transition:background .15s,box-shadow .15s;
}

[data-testid="stButton"] button p,
[data-testid="stFormSubmitButton"] button p,
[data-testid="stPopover"] button p{
    color:inherit;
    font-size:inherit;
    margin:0;
}

[data-testid="stButton"] button:hover,
[data-testid="stFormSubmitButton"] button:hover,
[data-testid="stPopover"] button:hover{
    background:var(--botao-hover);
    color:#fff;
}

[data-testid="stButton"] button:focus-visible,
[data-testid="stFormSubmitButton"] button:focus-visible,
[data-testid="stPopover"] button:focus-visible{
    outline:2px solid #9db0ff;
    outline-offset:2px;
}

[class*="st-key-link_"] [data-testid="stButton"],
[class*="st-key-link_"] [data-testid="stFormSubmitButton"]{
    display:flex;
    justify-content:center;
}

[class*="st-key-link_"] button{
    width:auto!important;
    min-height:0!important;
    padding:.15rem .4rem!important;
    background:none!important;
    box-shadow:none!important;
    color:var(--suave)!important;
    text-decoration:underline;
    font-size:.74rem!important;
}

[class*="st-key-link_"] button:hover{
    background:none!important;
    color:#fff!important;
}

.st-key-adicionar,
.st-key-filtro{
    width:min(200px,60%);
    margin:0 auto;
}

.st-key-adicionar button,
.st-key-filtro button{
    background:linear-gradient(180deg,var(--acento-a),var(--acento-b))!important;
    box-shadow:0 0 24px rgba(90,110,255,.5)!important;
    color:#fff!important;
}

.st-key-adicionar button:hover,
.st-key-filtro button:hover{
    background:linear-gradient(180deg,#7080ff,#4553cf)!important;
}

.logo{
    display:inline-block;
    font-weight:700;
    font-style:italic;
    font-size:2.2rem;
    line-height:1;
    letter-spacing:-.1em;
    color:#fff;
    text-shadow:0 0 14px rgba(120,160,255,.85);
}

.tagline{
    margin:0;
    font-size:.78rem;
    line-height:1.4;
    text-align:center;
    color:var(--texto);
}

.pilula{
    margin-top:.7rem;
    padding:.7rem 1rem;
    border-radius:9px;
    background:linear-gradient(180deg,var(--botao-a),var(--botao-b));
    box-shadow:0 8px 18px rgba(0,0,40,.55);
    text-align:center;
    font-size:.85rem;
    overflow-wrap:anywhere;
}

.vazio{
    margin:2rem 0 0;
    text-align:center;
    color:var(--suave);
    font-size:.85rem;
}
"""


CSS_AUTH = """
.stApp{
    background:linear-gradient(135deg,#0a3dd6 0%,#0746e8 45%,#0a2fc0 100%)!important;
}

.stApp::before{
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:0;
    background:
    linear-gradient(118deg,transparent 0 6%,rgba(80,200,255,.30) 6% 11%,transparent 11% 14%,rgba(70,185,255,.22) 14% 20%,transparent 20% 24%,rgba(60,170,255,.14) 24% 32%,transparent 32%),
    linear-gradient(152deg,transparent 0 52%,rgba(255,255,255,.06) 52% 100%),
    radial-gradient(circle at 85% 90%,rgba(0,20,140,.55),transparent 55%);
}

.st-key-auth_panel{
    width:min(440px,94vw);
    margin:5vh auto 0;
    padding:1.5rem 2.6rem 1.7rem;
    gap:.55rem;
    border-radius:14px;
    background:rgba(6,36,170,.45);
    backdrop-filter:blur(8px);
    -webkit-backdrop-filter:blur(8px);
    border:1px solid rgba(255,255,255,.1);
    box-shadow:0 24px 60px rgba(0,12,90,.45);
}

.auth-cabeca{
    display:grid;
    grid-template-columns:1fr auto 1fr;
    align-items:center;
    margin-bottom:.4rem;
}

.auth-avatar svg{
    width:46px;
    height:46px;
    display:block;
}

.auth-linha{
    height:1px;
    background:rgba(255,255,255,.4);
    margin:.3rem 0 .5rem;
}

.esqueceu{
    text-align:right;
    font-size:.7rem;
    color:var(--suave);
}

.esqueceu span{
    text-decoration:underline;
}

.st-key-auth_panel [data-testid="stFormSubmitButton"]{
    display:flex;
    justify-content:center;
}

.st-key-auth_panel [data-testid="stFormSubmitButton"] button{
    width:46%;
}

.st-key-google_login [data-testid="stButton"]{
    display:flex;
    justify-content:center;
}

.st-key-google_login button{
    width:62%;
    padding-left:2.4rem!important;
    background:url("__GOOGLE__") no-repeat 1rem center/1.15rem,rgba(255,255,255,.14)!important;
}

.st-key-google_login button:hover{
    background:url("__GOOGLE__") no-repeat 1rem center/1.15rem,rgba(255,255,255,.24)!important;
}

@media (max-width:560px){
    .st-key-auth_panel{
        padding:1.2rem 1.4rem 1.4rem;
    }
}
""".replace("__GOOGLE__", GOOGLE_URI)


CSS_APP = """
.stApp{
    background:radial-gradient(ellipse 85% 75% at 28% 58%,#0b0bd6 0%,#06069f 28%,#030360 55%,#01011f 100%)!important;
}

.stApp::before,
.stApp::after{
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:0;
    background-image:radial-gradient(rgba(140,165,255,.6) 1px,transparent 1.7px);
    background-size:7px 7px;
}

.stApp::before{
    -webkit-mask-image:radial-gradient(ellipse 50% 58% at 100% 0%,#000 0%,transparent 100%);
    mask-image:radial-gradient(ellipse 50% 58% at 100% 0%,#000 0%,transparent 100%);
}

.stApp::after{
    -webkit-mask-image:radial-gradient(ellipse 34% 40% at 0% 100%,rgba(0,0,0,.7) 0%,transparent 100%);
    mask-image:radial-gradient(ellipse 34% 40% at 0% 100%,rgba(0,0,0,.7) 0%,transparent 100%);
}

.st-key-topo{
    margin-bottom:.5rem;
}

.st-key-base{
    position:fixed!important;
    left:50%!important;
    bottom:1.6rem!important;
    transform:translateX(-50%)!important;
    width:min(980px,calc(100vw - 3rem))!important;
    max-width:980px!important;
    z-index:5;
}

.st-key-base > div{
    width:100%!important;
}

.st-key-base [data-testid="stHorizontalBlock"]{
    display:grid!important;
    grid-template-columns:minmax(0,1fr) minmax(300px,auto) minmax(0,1fr)!important;
    align-items:center!important;
    justify-content:stretch!important;
    width:100%!important;
    gap:1rem!important;
}

.st-key-base [data-testid="stColumn"]{
    min-width:0!important;
    width:auto!important;
    max-width:none!important;
    flex:none!important;
    margin:0!important;
}

.st-key-base [data-testid="stColumn"]:first-child{
    justify-self:start!important;
    text-align:left!important;
}

.st-key-base [data-testid="stColumn"]:nth-child(2){
    justify-self:center!important;
    text-align:center!important;
}

.st-key-base [data-testid="stColumn"]:last-child{
    justify-self:end!important;
    text-align:right!important;
}

.st-key-base [data-testid="stColumn"]:first-child [data-testid="stButton"],
.st-key-base [data-testid="stColumn"]:last-child [data-testid="stButton"]{
    width:max-content!important;
}

.st-key-base [data-testid="stColumn"]:first-child button,
.st-key-base [data-testid="stColumn"]:last-child button{
    width:auto!important;
    white-space:nowrap!important;
}

.st-key-base .tagline{
    width:100%;
    text-align:center;
}

.st-key-base_home{
    position:fixed!important;
    left:50%!important;
    bottom:1.6rem!important;
    transform:translateX(-50%)!important;
    width:min(480px,92vw)!important;
    z-index:5;
}

.st-key-contato{
    position:fixed;
    left:2rem;
    bottom:2.1rem;
    z-index:5;
}

@media (max-width:760px){
    .st-key-contato{
        left:50%;
        transform:translateX(-50%);
        bottom:5.4rem;
    }
}

.hero{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:1.4rem;
    margin-top:2.5vh;
    text-align:center;
}

.hero svg{
    width:190px;
    height:190px;
    filter:drop-shadow(0 0 12px rgba(61,91,255,.85));
}

.hero .tagline{
    font-size:.95rem;
}

.st-key-perfil{
    position:relative!important;
    left:auto!important;
    transform:translateX(-50%)!important;
    width:min(340px,calc(100vw - 2rem))!important;
    margin-left:50%!important;
    margin-right:0!important;
    gap:.3rem;
}

.perfil-avatar{
    display:flex;
    justify-content:center;
    margin:.2rem 0 .4rem;
}

.perfil-avatar svg{
    width:96px;
    height:96px;
    display:block;
    filter:drop-shadow(0 8px 16px rgba(0,0,40,.6));
}

.st-key-senha_botao,
.st-key-celular_botao{
    margin-top:.7rem;
}

.st-key-lista{
    width:min(640px,100%);
    margin:0 auto;
    gap:.5rem;
}

.lista-nome,
.lista-qtd{
    font-size:.88rem;
}

.filtro-ativo{
    margin:.6rem 0 0;
    text-align:center;
    font-size:.76rem;
    color:var(--suave);
}

.estoque-grade{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:1.1rem 3.5rem;
    max-width:640px;
    margin:1.6rem auto 0;
}

.estoque-item{
    display:grid;
    grid-template-columns:1fr 2.5rem;
    font-size:.88rem;
}

.estoque-item .qtd{
    text-align:right;
}

@media (max-width:760px){
    .st-key-base{
        width:calc(100vw - 2rem)!important;
    }

    .st-key-base [data-testid="stHorizontalBlock"]{
        grid-template-columns:minmax(0,1fr) minmax(120px,1.5fr) minmax(0,1fr)!important;
        gap:.4rem!important;
    }

    .st-key-base .tagline{
        font-size:.65rem;
    }

    .st-key-base [data-testid="stButton"] button{
        font-size:.7rem;
        padding:.4rem!important;
    }
}

@media (max-width:560px){
    .estoque-grade{
        grid-template-columns:1fr;
    }
}
"""


def tema(variante):
    css = BASE_CSS + (CSS_AUTH if variante == "auth" else CSS_APP)
    st.html(f"<style>{css}</style>")


def avatar_svg(fundo):
    return (
        f'<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="32" fill="{fundo}"/>'
        '<circle cx="32" cy="25" r="9" fill="#fff"/>'
        '<path d="M14 52c0-10 8-16 18-16s18 6 18 16z" fill="#fff"/></svg>'
    )


def cabecalho_auth():
    st.html(
        f'<div class="auth-cabeca">{LOGO}<span class="auth-avatar">{avatar_svg("#0b2a8c")}</span><span></span></div>'
    )


def em_desenvolvimento():
    st.toast("Work in progress", icon="🚧")


def botao_nav(rotulo, destino):
    if st.button(rotulo, key=f"nav_{rotulo}"):
        st.switch_page(destino)


def topo(rotulo, destino):
    with st.container(key="topo"):
        esquerda, _, direita = st.columns([1, 1.6, 1])
        esquerda.html(LOGO)

        with direita:
            _, coluna_perfil = st.columns([1, 0.35])

            with coluna_perfil:
                botao_nav(rotulo, destino)


def rodape(esquerda, direita):
    with st.container(key="base"):
        col_a, col_b, col_c = st.columns([1, 1.6, 1])

        with col_a:
            botao_nav(*esquerda)

        col_b.html(f'<p class="tagline">{TAGLINE}</p>')

        with col_c:
            botao_nav(*direita)


def rodape_centralizado(esquerda, direita):
    with st.container(key="base_home"):
        col_a, col_b = st.columns(2)

        with col_a:
            botao_nav(*esquerda)

        with col_b:
            botao_nav(*direita)
