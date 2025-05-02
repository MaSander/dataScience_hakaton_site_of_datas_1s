import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

def gerar_entregas(n=100):
    tipos = ['Seca', 'Refrigerada', 'Congelada']
    dados = []

    for i in range(1, n + 1):
        data_saida = datetime.now() - timedelta(days=random.randint(1, 60))
        tempo_previsto = random.randint(1, 5)
        tempo_real = tempo_previsto + random.randint(-1, 3)
        horario_saida = fake.time()
        horario_entrega = fake.time()
        custo_frete = round(random.uniform(100, 1500), 2)
        if random.random() < 0.05:
            custo_frete *= 10

        dados.append({
            'id_entrega': i,
            'data_saida': data_saida.date(),
            'data_entrega': (data_saida + timedelta(days=tempo_real)).date(),
            'origem': fake.city(),
            'destino': fake.city(),
            'transportadora': fake.company(),
            'custo_frete': custo_frete,
            'tempo_previsto': tempo_previsto,
            'tempo_real': tempo_real,
            'horario_saida': horario_saida,
            'horario_entrega': horario_entrega,
            'tipo_carga': random.choice(tipos),
            'filial_responsavel': fake.city()
        })

    pd.DataFrame(dados).to_csv('entregas.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'entregas.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_entregas()
