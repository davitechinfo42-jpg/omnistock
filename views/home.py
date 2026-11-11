
import streamlit as st

import state
import ui
import crud_estoque
import preditivo
import chef_ia

state.exigir_login()
ui.tema("app")

ui.topo("Profile", "views/perfil.py")

st.html(f'''
    <div class="hero">
        {ui.CASA_SVG}
        <p class="tagline">
            Omnistock, o melhor para facilitar suas compras<br>
            e controle de estoque
        </p>
    </div>
''')

st.markdown("### 🧠 Central Inteligente da Residência")

col_alerta, col_compra = st.columns(2)

alertas = []

with col_alerta:

    st.markdown("#### 🚨 Alertas de Validade")

    try:
        alertas = preditivo.analisar_vencimentos()

        if alertas:
            for alerta in alertas:

                if "🔴" in alerta:
                    st.error(alerta)

                else:
                    st.warning(alerta)

        else:
            st.success(
                "Tudo em ordem! Nenhum produto vencendo."
            )

    except Exception:
        st.info(
            "Cadastre produtos para ativar a predição de validade."
        )


with col_compra:

    st.markdown("#### 🛒 Sugestão de Reposição")

    try:
        compras = preditivo.gerar_lista_compras()

        if compras:

            for item in compras:

                st.warning(
                    f"**{item['Produto']}** — "
                    f"{item['Motivo']} "
                    f"(Qtd: {item['Qtd Atual']})"
                )

        else:
            st.success(
                "Despensa abastecida! Nenhuma compra necessária."
            )

    except Exception:
        st.info(
            "Sem dados de consumo suficientes ainda."
        )


st.divider()

st.markdown(
    """
    <div style="text-align: center;">
        <h3>👨‍🍳 Sugestão do Chef</h3>
        <p style="opacity: 0.75;">
            O Chef analisa todo o seu estoque de alimentos
            e cria receitas instantâneas priorizando os itens a vencer.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


col_esquerda, col_centro, col_direita = st.columns(
    [1, 2, 1]
)

with col_centro:

    gerar_receita = st.button(
        "✨ Gerar Receita Antidesperdício",
        use_container_width=True,
        type="primary"
    )


if gerar_receita:

    with st.spinner(
        "O Chef está analisando o estoque e preparando a receita..."
    ):

        try:

            todos_produtos = crud_estoque.listar_produtos()

            receita = chef_ia.criar_receita_anti_desperdicio(
                todos_produtos,
                alertas
            )

            st.success("Receita criada com sucesso!")

            st.markdown(receita)

        except Exception as e:

            st.error(
                f"Não foi possível gerar a receita: {e}"
            )



st.markdown("<br>", unsafe_allow_html=True)

col_estoque, col_lista = st.columns(2)


with col_estoque:

    if st.button(
        "📦 Estoque",
        use_container_width=True,
        type="secondary"
    ):

        st.switch_page("views/estoque.py")


with col_lista:

    if st.button(
        "🛒 Lista de Compras",
        use_container_width=True,
        type="secondary"
    ):

        st.switch_page("views/lista.py")
