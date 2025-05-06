import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_rotas(n=50):
    tipos = ['Caminhão', 'Furgão', 'Carreta']
    dados = []

    for _ in range(n):
        origem = fake.city()
        destino = fake.city()
        distancia = round(random.uniform(10, 3000), 2)
        if random.random() < 0.05:
            distancia = -100  # erro proposital

        dados.append({
            'origem': origem,
            'destino': destino,
            'distancia_km': distancia,
            'tipo_veiculo': random.choice(tipos)
        })

    pd.DataFrame(dados).to_csv('rotas.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'rotas.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_rotas()
