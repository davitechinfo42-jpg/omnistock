# OmniStock 2050 — Gestão Inteligente de Casa e Inventário

O **OmniStock 2050** é um sistema inteligente de controle de estoque residencial desenvolvido em **Python**, **Streamlit** e **SQLite**. O projeto combina arquitetura modular, análise preditiva de validade e Inteligência Artificial Generativa (**Google Gemini**) para reduzir o desperdício de alimentos e automatizar a lista de compras doméstica.

---

## Funcionalidades Principais

* **Autenticação Segura:** Cadastro e login de moradores com criptografia de senhas via `bcrypt` e controle de sessão isolado.
* **Gestão Completa de Estoque (CRUD):** Cadastro, edição e baixa de produtos organizados por categoria e data de validade no padrão ISO (`AAAA-MM-DD`).
* **Motor Preditivo:** Cálculo automático de vencimentos próximos e identificação de itens abaixo do estoque mínimo configurado.
* **Sugestão do Chef (IA Generativa):** Integração com o Google Gemini que filtra exclusivamente alimentos da despensa por categoria, prioriza itens próximos do vencimento e gera receitas práticas sem alucinação de ingredientes.

---

## Arquitetura do Projeto

```text
omnistock/
├── .streamlit/
│   ├── config.toml               # Configurações visuais e de tema do Streamlit
│   └── secrets.toml.example      # Modelo de variáveis de ambiente e chaves
├── views/
│   ├── cadastro.py               # Tela de registro de novos usuários
│   ├── home.py                   # Dashboard principal, alertas e Chef IA
│   ├── lista.py                  # Visualização e gerenciamento do estoque
│   └── login.py                  # Tela de autenticação
├── app.py                        # Ponto de entrada e roteamento da aplicação
├── auth.py                       # Lógica de segurança e hash com Bcrypt
├── carga_dados.py                # Script de povoamento inicial do banco
├── chef_ia.py                    # Integração com Google Gemini e filtro de categorias
├── crud_estoque.py               # Operações CRUD parametrizadas no banco de dados
├── database.py                   # Conexão SQLite e definição de tabelas
├── preditivo.py                  # Regras de alerta de validade e reposição
├── state.py                      # Gerenciamento de estado da sessão
├── ui.py                         # Componentes visuais e estilização customizada
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do repositório

## Executando Localmente

1- Clone o Repositório
git clone [https://github.com/davitechinfo42-jpg/omnistock.git](https://github.com/davitechinfo42-jpg/omnistock.git)
cd omnistock

2- Crie o Ambiente Virtual
python3 -m venv venv
source venv/bin/activate

3- Instale as Dependências
pip install -r requirements.txt

4- Popule o banco de dados inicialmente
python3 carga_dados.py

5- Crie a chave da API do google gemini
GEMINI_API_KEY = "SUA_CHAVE_API_AQUI"

6- Inicie 
python3 -m streamlit run app.py

Integrante,Papel e Contribuições no Projeto
Davi Leite Santana,"Arquitetura geral do sistema, integração da IA Generativa (chef_ia.py), motor preditivo (preditivo.py) e configuração do repositório."
Erick Manoel,"Módulo de autenticação e segurança (auth.py), implementação de criptografia com bcrypt, controle de sessão (state.py) e proteção de queries."
Gabriel,"Regras de negócio da despensa e estruturação da proposta de valor."
Chagas,"Modelagem do banco de dados SQLite (database.py), operações de persistência (crud_estoque.py) e carga de dados (carga_dados.py)."
Marcelo,"Interface do usuário (ui.py e views/), testes de usabilidade, validação de fluxo e infraestrutura de apresentação."