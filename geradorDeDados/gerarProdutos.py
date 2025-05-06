import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_produtos(n=50):
    categorias = ['Congelado', 'Fresco', 'Industrializado', 'Bebida', 'Limpeza']
    dados = []

    for i in range(1, n + 1):
        preco = round(random.uniform(1, 100), 2)
        if random.random() < 0.05:
            preco *= 20  # outlier
        estoque = random.randint(0, 1000)
        if random.random() < 0.05:
            estoque = -10  # valor inválido

        dados.append({
            'id_produto': i,
            'nome_produto': fake.word().capitalize(),
            'categoria': random.choice(categorias),
            'preco_unitario': preco,
            'estoque_atual': estoque
        })

    pd.DataFrame(dados).to_csv('produtos.csv', index=False, sep=';', encoding='utf-8')
    print("Arquivo 'produtos.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_produtos()
