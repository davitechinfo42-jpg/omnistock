import crud_estoque

# Mock Data Doméstico - OmniStock 2050
# Estrutura: (Nome, Categoria, Quantidade Atual, Estoque Mínimo, Consumo Diário, Validade)
# Data atual do sistema: 09/11/2026

produtos_mock = [
    # 🔴 VENCENDO (Alerta de validade)
    ("Iogurte Natural", "Alimentação", 4, 2, 1.0, "2026-11-10"),  # Vence amanhã!
    ("Leite Integral", "Alimentação", 6, 2, 1.0, "2026-11-12"),   # Vence em 3 dias
    
    # 🟡 ACABANDO (Alerta de reposição: Qtd atual <= Estoque mínimo)
    ("Papel Higiênico", "Higiene", 2, 6, 0.5, "2028-12-01"),     # Só restam 2, precisa de 6
    ("Café 500g", "Alimentação", 1, 2, 0.1, "2027-08-15"),         # Só resta 1
    ("Pão de Forma", "Alimentação", 1, 2, 0.5, "2026-11-11"),      # Acabando e vencendo em 2 dias!

    # 🟢 TUDO OK (Estoque normal e validade longa)
    ("Arroz 5kg", "Alimentação", 3, 1, 0.1, "2027-05-10"),
    ("Sabonete", "Higiene", 8, 4, 0.2, "2028-01-01"),
    ("Creme Dental", "Higiene", 4, 2, 0.1, "2027-10-20"),
    ("Detergente", "Limpeza", 5, 2, 0.2, "2027-11-01"),
    ("Azeite de Oliva", "Alimentação", 2, 1, 0.05, "2028-03-15"),
    ("Amaciante 2L", "Limpeza", 3, 1, 0.1, "2027-12-05")
]

def rodar_carga():
    print("Iniciando injeção do Mock Data Doméstico do OmniStock 2050...")
    
    for p in produtos_mock:
        try:
            crud_estoque.cadastrar_produto(
                nome=p[0], 
                categoria=p[1], 
                quantidade=p[2], 
                estoque_minimo=p[3], 
                consumo_diario=p[4], 
                validade=p[5]
            )
            print(f"✅ Inserido: {p[0]}")
        except Exception as e:
            print(f"❌ Erro ao inserir {p[0]}: {e}")
            
    print("\nCarga de dados residenciais concluída com sucesso no banco oficial!")

if __name__ == "__main__":
    rodar_carga()