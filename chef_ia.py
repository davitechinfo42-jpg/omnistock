import os
import streamlit as st
import google.generativeai as genai

CHAVE_API = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")

if CHAVE_API:
    genai.configure(api_key=CHAVE_API)

CATEGORIAS_NAO_ALIMENTOS = [
    "higiene", 
    "limpeza", 
    "não alimentar", 
    "não alimentício", 
    "utensílios", 
    "casa", 
    "perfumaria"
]

def eh_alimento(produto):
    """
    Verifica se o produto é comestível analisando a Categoria registrada no banco.
    Possui fallback para o nome caso a categoria esteja vazia.
    """
    categoria = str(produto.get('categoria', '')).strip().lower()
    
    if categoria:
        if any(termo in categoria for termo in CATEGORIAS_NAO_ALIMENTOS):
            return False
        if any(termo in categoria for termo in ["alimento", "comida", "bebida", "frios", "hortifruti", "despensa", "mercearia"]):
            return True

    nome = str(produto.get('nome', '')).strip().lower()
    palavras_nao_alimentos = ["papel", "sabonete", "detergente", "creme dental", "amaciante", "desinfetante", "shampoo", "condicionador", "esponja"]
    return not any(item in nome for item in palavras_nao_alimentos)


def criar_receita_anti_desperdicio(produtos_estoque, alertas_validade):
    """
    Filtra os produtos comestíveis via Categoria e gera a receita inteligente.
    """
    if not CHAVE_API:
        return "Chave de API do Gemini não configurada. Defina a variável GEMINI_API_KEY."

    if not produtos_estoque:
        return "Sua despensa está vazia! Cadastre produtos no estoque para o Chef Inteligente criar receitas."

    alimentos = [p for p in produtos_estoque if eh_alimento(p)]
    
    if not alimentos:
        return "Nenhum alimento encontrado no estoque para gerar receitas."

    ingredientes = ", ".join([p['nome'] for p in alimentos])
    alertas = ", ".join(alertas_validade) if alertas_validade else "Nenhum"

    prompt = f"""Use SOMENTE estes ingredientes disponíveis: {ingredientes}.
Prioridade de uso para itens a vencer: {alertas}.

Gere uma receita direta em português sem saudações ou rascunhos. Use exatamente a estrutura:
🍽️ [Nome da Receita]
🛒 **Ingredientes Utilizados:**
⏱️ **Modo de Preparo:**
"""

    try:
        modelos_disponiveis = [
            m.name for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        
        if not modelos_disponiveis:
            return "Nenhum modelo ativo encontrado para esta chave de API."

        texto_bruto = ""
        for nome_modelo in modelos_disponiveis:
            try:
                model = genai.GenerativeModel(nome_modelo)
                response = model.generate_content(prompt)
                if response and response.text:
                    texto_bruto = response.text
                    break
            except Exception:
                continue

        if not texto_bruto:
            return "Não foi possível obter resposta do servidor."

        if "🍽️" in texto_bruto:
            partes = texto_bruto.split("🍽️")
            texto_limpo = "🍽️" + partes[-1]
            return texto_limpo.strip()

        return texto_bruto.strip()

    except Exception as e:
        return f"Erro ao gerar receita: {e}"