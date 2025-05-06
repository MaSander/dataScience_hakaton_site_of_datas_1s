import pandas as pd
import random

def gerar_orcamento():
    setores = ['Produção', 'Financeiro', 'RH', 'Logística', 'Comercial']
    anos = [2024, 2025]
    dados = []

    for setor in setores:
        for ano in anos:
            for mes in range(1, 13):
                previsto = round(random.uniform(5000, 100000), 2)
                realizado = previsto * random.uniform(0.8, 1.2)
                if random.random() < 0.05:
                    realizado *= 5  # outlier

                dados.append({
                    'setor': setor,
                    'mes': mes,
                    'ano': ano,
                    'valor_previsto': previsto,
                    'valor_realizado': realizado
                })

    pd.DataFrame(dados).to_csv('orcamento.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'orcamento.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_orcamento()
