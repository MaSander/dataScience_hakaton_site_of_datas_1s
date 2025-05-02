import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_materiais(n=100):
    unidades = ['kg', 'litro', 'unidade']
    setores = ['Produção', 'Higiene', 'Cozinha']
    turnos = ['Manhã', 'Tarde', 'Noite']
    
    dados = []
    for i in range(1, n + 1):
        custo = round(random.uniform(0.5, 200), 2)
        if random.random() < 0.05:
            custo = -5.0  # erro

        dados.append({
            'id_material': i,
            'nome': fake.word(),
            'quantidade_uso': round(random.uniform(0.1, 50), 2),
            'unidade': random.choice(unidades),
            'setor_uso': random.choice(setores),
            'custo_unitario': custo,
            'fornecedor': fake.company(),
            'Filial': fake.city(),
            'turno': random.choice(turnos)
        })

    pd.DataFrame(dados).to_csv('materiais.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'materiais.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_materiais()
