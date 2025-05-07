import pandas as pd
import random
from faker import Faker
from pandas.core.indexes.base import Index

fake = Faker('pt_BR')

def gerar_clientes(n=100):
    categorias = ['Atacado', 'Varejo', 'Restaurante', 'Distribuidor', 'Indústria']
    dados = []

    for i in range(1, n + 1):
        nome = fake.company()
        if random.random() < 0.05:
            nome = nome[:3]  # truncado
        email = fake.email()
        if random.random() < 0.05:
            email = 'emailinvalido'  # sem @
        cidade = fake.city()
        categoria = random.choice(categorias)

        dados.append({
            'id_cliente': i,
            'nome': nome,
            'email': email,
            'cidade': cidade,
            'categoria': categoria
        })

    # pd.DataFrame(dados).to_csv('clientes.csv', index=False, sep=';', encoding='utf-8')
    pd.DataFrame(dados).to_json('db/commercial/clientes.json', orient='records', indent=4, force_ascii=False)
    print("Arquivo 'clientes.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_clientes()
