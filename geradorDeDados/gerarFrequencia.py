import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')
random.seed(42)

def gerar_frequencia(n_func=100, dias=30):
    dados = []
    for id_funcionario in range(1, n_func + 1):
        for dia in range(dias):
            data = datetime.today() - timedelta(days=dia)
            faltou = random.random() < 0.1
            entrada = fake.time() if not faltou else ''
            saida = fake.time() if not faltou else ''
            horas_extras = round(random.uniform(0, 3), 1) if not faltou else 0

            if random.random() < 0.05:
                entrada = '99:99'  # erro proposital
                saida = ''

            dados.append({
                'id_funcionario': id_funcionario,
                'data': data.date(),
                'entrada': entrada,
                'saida': saida,
                'faltou': faltou,
                'horas_extras': horas_extras
            })

    df = pd.DataFrame(dados)
    df.to_csv('frequencia.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'frequencia.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_frequencia()
