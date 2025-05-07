import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_vendas(n=200, max_clientes=100, max_produtos=50):
    dados = []

    for i in range(1, n + 1):
        id_cliente = random.randint(1, max_clientes)
        id_produto = random.randint(1, max_produtos)
        data_venda = datetime.now() - timedelta(days=random.randint(0, 365))
        quantidade = random.randint(1, 50)
        valor_total = round(quantidade * random.uniform(2, 100), 2)
        if random.random() < 0.05:
            valor_total *= 10  # outlier

        pedido_concluido = random.choice([True, False])
        avaliacao = random.choice([1, 2, 3, 4, 5, '', 10]) if pedido_concluido else ''

        dados.append({
            'id_venda': i,
            'id_cliente': id_cliente,
            'id_produto': id_produto,
            'data_venda': data_venda.date(),
            'quantidade': quantidade,
            'valor_total': valor_total,
            'pedido_concluido': pedido_concluido,
            'avaliacao_servico': avaliacao
        })

    # pd.DataFrame(dados).to_csv('vendas.csv', index=False, sep=';', encoding='utf-8')
    pd.DataFrame(dados).to_json('db/commercial/vendas.json', orient='records', indent=4, force_ascii=False)
    print("Arquivo 'vendas.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_vendas()
