import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

def gerar_equipamentos(n=50):
    setores = ['Produção', 'Logística', 'Embalagem']
    status_opcoes = ['Operacional', 'Manutenção', 'Parado']
    manutencao_tipo = ['Preventiva', 'Corretiva', '']

    dados = []
    for i in range(1, n + 1):
        data_manutencao = fake.date_between(start_date='-1y', end_date='today') if random.random() > 0.2 else ''
        tempo_parado = random.randint(0, 20)
        custo = round(random.uniform(100, 5000), 2)
        if random.random() < 0.05:
            custo *= 10  # outlier

        dados.append({
            'id_equipamento': i,
            'modelo': fake.lexify(text='MOD-???'),
            'setor': random.choice(setores),
            'status_atual': random.choice(status_opcoes),
            'tipo_manutencao': random.choice(manutencao_tipo),
            'data_manutencao': data_manutencao,
            'tempo_parado_dias': tempo_parado,
            'custo_manutencao': custo
        })

    # pd.DataFrame(dados).to_csv('equipamentos.csv', index=False, sep=';', encoding='utf-8')
    pd.DataFrame(dados).to_json('db/operational/equipamentos.json', orient='records', indent=4, force_ascii=False)
    print("Arquivo 'equipamentos.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_equipamentos()
