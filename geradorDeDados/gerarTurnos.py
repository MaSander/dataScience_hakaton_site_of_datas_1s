import pandas as pd

def gerar_turnos():
    dados = [
        {'Turno': 'Manhã', 'Entrada': '06:00', 'Saída': '14:00'},
        {'Turno': 'Tarde', 'Entrada': '14:00', 'Saída': '22:00'},
        {'Turno': 'Noite', 'Entrada': '22:00', 'Saída': '06:00'},
        {'Turno': 'Invalido', 'Entrada': '25:00', 'Saída': '30:00'},  # valores errados
    ]

    df = pd.DataFrame(dados)
    # df.to_csv('turnos.csv', index=False, sep=';', encoding='utf-8')
    df.to_json('db/human_resources/turnos.json', orient='records', indent=4, force_ascii=False)
    print("Arquivo 'turnos.csv' gerado com sucesso.")

if __name__ == "__main__":
    gerar_turnos()
