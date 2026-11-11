# OmniStock 2050 — Smart Home & Inventory Management

O **OmniStock 2050** é um sistema inteligente de gestão de estoque residencial desenvolvido em Python com Streamlit e SQLite. O projeto integra conceitos avançados de Programação Orientada a Objetos (POO), arquitetura modularizada e Inteligência Artificial Generativa para evitar o desperdício de alimentos.

---

## Funcionalidades Principais

- **Gestão de Despensa (CRUD):** Controle completo de cadastro, atualização e listagem de produtos com datas de validade no formato padronizado ISO (`YYYY-MM-DD`).
- **Motor Preditivo de Consumo:** Algoritmo que analisa datas de expiração e calcula automaticamente sugestões de reposição baseadas no consumo da casa.
- **(IA Generativa):** Integração com a API do Google Gemini para ler os alertas de validade da despensa e sugerir receitas instantâneas anti-desperdício.
- **Segurança & Autenticação:** Criptografia de senhas com `bcrypt` e consultas SQL parametrizadas contra injeções maliciosas.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Interface:** Streamlit
- **Banco de Dados:** SQLite3
- **Inteligência Artificial:** Google Gemini API (`google-generativeai`)
- **Segurança:** Bcrypt

---

## Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/omnistock.git](https://github.com/SEU_USUARIO/omnistock.git)
   cd omnistock