import csv
import random
import datetime
import math

# --- Configurações ---
NUM_ROWS = 423
CSV_FILENAME = 'delicias_do_campo_logistica_viagens.csv'

# --- Listas de Dados Base ---
origins = [
    "Sorriso, MT", "Petrolina, PE", "Chapecó, SC", "Uberlândia, MG", "Pelotas, RS",
    "Campinas, SP", "Rio Verde, GO", "Dourados, MS", "Barreiras, BA", "Londrina, PR",
    "Rondonópolis, MT", "Ji-Paraná, RO", "Balsas, MA", "Juazeiro, BA" # Adicionado Juazeiro para rotas curtas
]
destinations = [
    "Santos, SP", "Recife, PE", "Curitiba, PR", "Belo Horizonte, MG", "Porto Alegre, RS",
    "Rio de Janeiro, RJ", "Paranaguá, PR", "São Paulo, SP", "Brasília, DF", "Goiânia, GO",
    "Fortaleza, CE", "Manaus, AM", "São Luís, MA", "Vitória, ES", "Salvador, BA",
    "Juazeiro, BA" # Para testar Origem = Destino e rotas curtas
]
truck_types = ["Simples", "Bitrem", "Rodo Trem"]
driver_types = ["Frota", "Agregado", "Terceiro"]

# --- Probabilidades das Falhas (Ajuste conforme necessário) ---
PROB_MISSING_PAYMENT = 0.05  # 5%
PROB_MISSING_QUANTITY = 0.04 # 4%
PROB_MISSING_DRIVER = 0.03  # 3%
PROB_TYPO_CITY = 0.06       # 6% (3% origem, 3% destino)
PROB_DATE_FORMAT = 0.02     # 2% usar DD/MM/YYYY
PROB_OUTLIER_HIGH_PAYMENT = 0.015 # 1.5%
PROB_OUTLIER_LOW_PAYMENT = 0.015  # 1.5%
PROB_OUTLIER_QUANTITY = 0.02  # 2% quantidade incompatível
PROB_TRUCK_NAME_INCONSISTENCY = 0.01 # 1% (RodoTrem, Bi-trem)
PROB_QUANTITY_UNIT_KG = 0.01   # 1% marcar como Kg sem mudar valor
PROB_FUTURE_DATE = 0.005     # 0.5%
PROB_PAST_DATE = 0.005       # 0.5%
PROB_ORIGIN_DEST_EQUAL = 0.01 # 1%

# --- Funções Auxiliares ---

def generate_realistic_date(start_year=2024, end_year=2025):
    """Gera uma data aleatória entre start_year e hoje."""
    try:
        start_date = datetime.date(start_year, 1, 1)
        # Usa a data atual fornecida pelo contexto ou uma data fixa se falhar
        # CURRENT_TIME = "Thursday, April 10, 2025 at 10:08:43 PM -03"
        end_date = datetime.date(2025, 4, 10)
        # end_date = datetime.date.today() # Se preferir usar a data atual real
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        if days_between_dates < 0: # Caso o start_year seja futuro
             days_between_dates = 365 # Gera data no último ano
             start_date = end_date - datetime.timedelta(days=days_between_dates)

        random_number_of_days = random.randrange(days_between_dates + 1)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date
    except ValueError:
         # Fallback em caso de erro de data (ex: ano inválido)
         return datetime.date(2024, random.randint(1, 12), random.randint(1, 28))


def introduce_typo(text):
    """Introduz um erro de digitação simples."""
    if len(text) < 3:
        return text
    pos = random.randint(0, len(text) - 2)
    type_of_typo = random.choice(['swap', 'drop', 'double'])
    if type_of_typo == 'swap':
        chars = list(text)
        chars[pos], chars[pos+1] = chars[pos+1], chars[pos]
        return "".join(chars)
    elif type_of_typo == 'drop':
         # Evitar dropar vírgula ou espaço essencial em nomes compostos
         if text[pos] not in [',', ' ']:
            return text[:pos] + text[pos+1:]
         else: # Tenta dropar a próxima letra se a atual for espaço/vírgula
            if pos + 1 < len(text) and text[pos+1] not in [',', ' ']:
                 return text[:pos+1] + text[pos+2:]
            else:
                 return text # Não faz nada se for complexo
    elif type_of_typo == 'double':
        # Evitar duplicar vírgula ou espaço
        if text[pos] not in [',', ' ']:
            return text[:pos+1] + text[pos] + text[pos+1:]
        else:
            return text # Não faz nada
    return text

def get_realistic_quantity(truck_type):
    """Gera quantidade baseada no tipo de caminhão."""
    if truck_type == "Simples":
        return round(random.uniform(10.0, 15.0), 1)
    elif truck_type == "Bitrem":
        return round(random.uniform(30.0, 45.0), 1)
    elif truck_type == "Rodo Trem":
        return round(random.uniform(50.0, 65.0), 1)
    else: # Caso tenha alguma inconsistência no nome
        return round(random.uniform(10.0, 65.0), 1) # Faixa ampla

def get_realistic_payment(truck_type, quantity, origin, destination):
    """Estima pagamento baseado no caminhão, quantidade e uma noção de distância."""
    base = 0
    # Estimativa muito simples de distância (longa, média, curta)
    long_haul_origins = ["Sorriso, MT", "Rondonópolis, MT", "Ji-Paraná, RO", "Barreiras, BA", "Balsas, MA"]
    long_haul_destinations = ["Santos, SP", "Manaus, AM", "Paranaguá, PR", "São Paulo, SP", "Rio de Janeiro, RJ", "Fortaleza, CE", "Porto Alegre, RS"]
    is_long_haul = origin in long_haul_origins or destination in long_haul_destinations

    if truck_type == "Simples":
        base = random.uniform(2000, 4000)
    elif truck_type == "Bitrem":
        base = random.uniform(5500, 9500)
    elif truck_type == "Rodo Trem":
        base = random.uniform(8000, 16000) # Maior variação para long haul
    else: # Nome inconsistente
         base = random.uniform(2000, 16000)

    # Ajuste simples por distância percebida
    if is_long_haul and truck_type != "Simples":
        base *= random.uniform(1.1, 1.4)
    elif origin.split(',')[1] == destination.split(',')[1]: # Mesmo estado (curta?)
        base *= random.uniform(0.7, 0.9)

    # Ajuste pela quantidade (fator menor)
    # base += quantity * random.uniform(10, 30)

    return round(base, 2)

# --- Geração dos Dados ---
data = []
for i in range(1, NUM_ROWS + 1):
    trip_id = i
    current_data = {} # Dicionário para a linha atual

    # --- Geração Base ---
    trip_date = generate_realistic_date()
    origin = random.choice(origins)
    destination = random.choice(destinations)
    truck_type = random.choice(truck_types)
    driver_type = random.choice(driver_types)
    quantity = get_realistic_quantity(truck_type)
    payment = get_realistic_payment(truck_type, quantity, origin, destination)

    # --- Aplicação das Falhas ---

    # Falha: Origem = Destino
    if random.random() < PROB_ORIGIN_DEST_EQUAL:
        destination = origin
        # Recalcular pagamento? Pode ser baixo ou um erro mantendo valor alto. Deixar o calculado.

    # Falha: Tipo de Motorista Faltando
    if random.random() < PROB_MISSING_DRIVER:
        driver_type = None # Ou "" (string vazia)

    # Falha: Nome do Caminhão Inconsistente
    if random.random() < PROB_TRUCK_NAME_INCONSISTENCY:
        if "Rodo Trem" in truck_type:
            truck_type = random.choice(["RodoTrem", "Rodotrem"])
        elif "Bitrem" in truck_type:
            truck_type = random.choice(["Bi-trem", "Bi trem"])
        # Não precisa recalcular quantity/payment, a base já foi pega

    # Falha: Quantidade Incompatível (Outlier)
    if random.random() < PROB_OUTLIER_QUANTITY:
        if truck_type == "Simples":
            quantity = round(random.uniform(25.0, 40.0), 1) # Muito alto
        elif truck_type == "Rodo Trem":
            quantity = round(random.uniform(10.0, 35.0), 1) # Muito baixo
        # Bitrem é intermediário, mais difícil de ser outlier claro

    # Falha: Quantidade Faltando (Aplicar *depois* de outros ajustes de quantidade)
    if random.random() < PROB_MISSING_QUANTITY:
        quantity = None # Ou ""

    # Falha: Unidade de Quantidade Inconsistente (Aplicar *depois* de outros ajustes e se não for None)
    if quantity is not None and random.random() < PROB_QUANTITY_UNIT_KG:
        quantity = f"{quantity} Kg" # Transforma em string e adiciona Kg

    # Falha: Pagamento Outlier Alto/Baixo
    payment_modifier = 1.0
    if random.random() < PROB_OUTLIER_HIGH_PAYMENT:
        payment_modifier = random.uniform(5.0, 10.0)
    elif random.random() < PROB_OUTLIER_LOW_PAYMENT:
        payment_modifier = random.uniform(0.05, 0.2)
    payment = round(payment * payment_modifier, 2)

    # Falha: Pagamento Faltando (Aplicar *depois* de outros ajustes de pagamento)
    if random.random() < PROB_MISSING_PAYMENT:
        payment = None # Ou ""

    # Falha: Erro de Digitação nas Cidades
    if random.random() < PROB_TYPO_CITY / 2: # Metade da chance para origem
        origin = introduce_typo(origin)
    if random.random() < PROB_TYPO_CITY / 2: # Metade da chance para destino
        destination = introduce_typo(destination)

    # Falha: Data Inválida (Futuro ou Passado)
    if random.random() < PROB_FUTURE_DATE:
        trip_date = trip_date + datetime.timedelta(days=random.randint(200, 730))
    elif random.random() < PROB_PAST_DATE:
        trip_date = trip_date - datetime.timedelta(days=random.randint(3650, 7300)) # 10-20 anos atrás

    # Falha: Formato de Data Inconsistente (Aplicar por último na data)
    date_str = trip_date.strftime('%Y-%m-%d')
    if random.random() < PROB_DATE_FORMAT:
        date_str = trip_date.strftime('%d/%m/%Y')

    # --- Montar a linha do dicionário ---
    current_data['ID Viagem'] = trip_id
    current_data['Data Viagem'] = date_str
    current_data['Origem'] = origin
    current_data['Destino'] = destination
    current_data['Tipo Caminhão'] = truck_type
    current_data['Motorista (Tipo)'] = driver_type if driver_type is not None else ""
    # Formatar quantidade apenas se não for string (Kg) e não for None
    if isinstance(quantity, (int, float)):
        current_data['Quantidade (Toneladas)'] = f"{quantity:.1f}"
    else:
        current_data['Quantidade (Toneladas)'] = quantity if quantity is not None else ""

    # Formatar pagamento apenas se for numérico e não None
    if isinstance(payment, (int, float)):
         current_data['Valor Pago (R$)'] = f"{payment:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") # Formato BR
    else:
         current_data['Valor Pago (R$)'] = payment if payment is not None else ""


    data.append(current_data)

# --- Escrever no arquivo CSV ---
print(f"Gerando {NUM_ROWS} linhas de dados...")
try:
    with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
        # Definir nomes das colunas (ordem importa)
        fieldnames = ['ID Viagem', 'Data Viagem', 'Origem', 'Destino',
                      'Tipo Caminhão', 'Motorista (Tipo)', 'Quantidade (Toneladas)',
                      'Valor Pago (R$)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader() # Escreve o cabeçalho
        writer.writerows(data) # Escreve todas as linhas de dados

    print(f"Banco de dados fictício salvo como '{CSV_FILENAME}'")

except IOError:
    print(f"Erro: Não foi possível escrever no arquivo {CSV_FILENAME}. Verifique as permissões.")
except Exception as e:
     print(f"Ocorreu um erro inesperado: {e}")