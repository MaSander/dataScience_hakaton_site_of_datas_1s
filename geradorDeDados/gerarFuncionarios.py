import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np

fake = Faker('pt_BR')
random.seed(42)

def gerar_funcionarios(n=100):
    cargos = ['Auxiliar', 'Analista', 'Gerente', 'Supervisor', 'Operador']
    setores = ['Produção', 'Financeiro', 'RH', 'Logística', 'Comercial']
    turnos = ['Manhã', 'Tarde', 'Noite']

    dados = []
    for i in range(1, n + 1):
        nome = fake.name()
        if random.random() < 0.05:
            nome = nome[:3]  # nome truncado (erro comum)

        sexo = random.choice(['M', 'F', '', 'X']) if random.random() < 0.1 else random.choice(['M', 'F'])

        data_admissao = fake.date_between(start_date='-10y', end_date='today')
        if random.random() < 0.05:
            data_admissao = fake.date_between(start_date='+1y', end_date='+2y')  # data futura

        cargo = random.choice(cargos)
        setor = random.choice(setores)
        turno = random.choice(turnos)

        salario = round(random.uniform(1200, 15000), 2)
        if random.random() < 0.05:
            salario *= 10  # outlier de salário

        if random.random() < 0.05:
            salario = ''  # campo em branco

        dados.append({
            'id_funcionario': i,
            'nome': nome,
            'sexo': sexo,
            'data_admissao': data_admissao,
            'cargo': cargo,
            'setor': setor,
            'turno': turno,
            'salario': salario
        })

    df = pd.DataFrame(dados)
    # df.to_csv('funcionarios.csv', index=False, sep=';', encoding='utf-8')
    df.to_json('db/human_resources/funcionarios.json')
    print("Arquivo 'funcionarios.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_funcionarios()
