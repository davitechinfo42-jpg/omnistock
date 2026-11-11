import crud_estoque
from datetime import datetime

def analisar_vencimentos():
    """Varre o estoque e retorna itens vencidos ou que vencem em até 3 dias."""
    produtos = crud_estoque.listar_produtos()
    alertas_validade = []
    
    hoje = datetime.now().date()
    
    for produto in produtos:
        try:
            data_validade = datetime.strptime(produto["data_validade"], "%Y-%m-%d").date()
            
            dias_para_vencer = (data_validade - hoje).days
            
            if dias_para_vencer < 0:
                alertas_validade.append(f"🔴 VENCIDO: {produto['nome']} (Venceu há {abs(dias_para_vencer)} dias)")
            elif 0 <= dias_para_vencer <= 3:
                alertas_validade.append(f"🟠 ATENÇÃO: {produto['nome']} vence em {dias_para_vencer} dias!")
        except Exception:
            continue
            
    return alertas_validade

def gerar_lista_compras():
    """
    Motor Preditivo: Calcula se o produto vai acabar com base no consumo diário.
    Gera a lista de reabastecimento inteligente.
    """
    produtos = crud_estoque.listar_produtos()
    lista_compras = []
    
    for produto in produtos:
        quantidade = produto["quantidade"]
        minimo = produto["estoque_minimo"]
        consumo_diario = produto["consumo_diario"]
        
        if quantidade <= minimo:
            lista_compras.append({
                "Produto": produto["nome"],
                "Motivo": "Abaixo do estoque mínimo",
                "Qtd Atual": quantidade
            })
            continue 
            
        if consumo_diario > 0:
            dias_restantes = quantidade / consumo_diario
            if dias_restantes <= 3:
                lista_compras.append({
                    "Produto": produto["nome"],
                    "Motivo": f"Acaba em {int(dias_restantes)} dias",
                    "Qtd Atual": quantidade
                })
                
    return lista_compras