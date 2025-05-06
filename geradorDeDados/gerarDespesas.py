import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_despesas(n=200):
    tipos = ['Energia', 'Água', 'Internet', 'Salário', 'Compra Matéria-prima']
    setores = ['Produção', 'Financeiro', 'RH', 'Logística', 'Comercial']
    
    dados = []
    for i in range(1, n + 1):
        valor = round(random.uniform(50, 20000), 2)
        if random.random() < 0.05:
            valor *= 10  # outlier

        dados.append({
            'id_despesa': i,
            'data': fake.date_between(start_date='-1y', end_date='today'),
            'tipo': random.choice(tipos),
            'setor': random.choice(setores),
            'valor': '' if random.random() < 0.05 else valor,
            'fornecedor': fake.company() if random.random() > 0.1 else ''
        })

    pd.DataFrame(dados).to_csv('despesas.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'despesas.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_despesas()
