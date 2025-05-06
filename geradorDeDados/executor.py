import subprocess

arquivos = [
    "gerarClientes.py",
    "gerarDespesas.py",
    "gerarEntregas.py",
    "gerarEquipamentos.py",
    "gerarFrequencia.py",
    "gerarFuncionarios.py",
    "gerarMateriais.py",
    "gerarOrcamento.py",
    "gerarProdutos.py",
    "gerarRotas.py",
    "gerarTurnos.py",
    "gerarUsoEquipamento.py",
    "gerarVendas.py"
]

for arquivo in arquivos:
    try:
        subprocess.run(["python", arquivo], check=True)
        print(f"Arquivo {arquivo} executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o arquivo {arquivo}: {e}")
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")