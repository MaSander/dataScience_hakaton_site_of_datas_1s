import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_uso_equipamento(n_equip=50, dias=30):
    turnos = ['Manhã', 'Tarde', 'Noite']
    dados = []

    for id_eq in range(1, n_equip + 1):
        for d in range(dias):
            data = datetime.today() - timedelta(days=d)
            horas = round(random.uniform(0, 12), 2)
            if random.random() < 0.05:
                horas = 25  # fora do normal

            dados.append({
                'id_equipamento': id_eq,
                'data': data.date(),
                'horas_uso': horas,
                'turno': random.choice(turnos)
            })

    pd.DataFrame(dados).to_json('db/operational/uso_equipamento.json')
    print("Arquivo 'uso_equipamento.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_uso_equipamento()
