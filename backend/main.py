import mysql.connector
import os
from sintomas import processar_sintomas  # Importa a função do módulo sintomas

# Função para conectar ao banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FASTHEALTHY",
        database="clinica_medica",
        port="3306"
    )

conexao = conectar_bd()
cursor = conexao.cursor()

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    classificacao = (
        "Abaixo do peso" if imc < 18.5 else
        "Peso normal" if imc < 25 else
        "Sobrepeso" if imc < 30 else
        "Obesidade Grau I" if imc < 35 else
        "Obesidade Grau II (severa)" if imc < 40 else
        "Obesidade Grau III (mórbida)"
    )
    return imc, classificacao

class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sintomas = []
        self.coletar_info_medica()

    def salvar_no_bd(self):
        try:
            sql = "INSERT INTO pacientes (nome, idade, cpf) VALUES (%s, %s, %s)"
            cursor.execute(sql, (self.nome, self.idade, self.cpf))
            conexao.commit()
            print("Paciente cadastrado com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao cadastrar usuário: {erro}")

    def coletar_info_medica(self):
        print("----- Informações médicas -----")
        altura = float(input("Altura (em metros): "))
        peso = float(input("Peso (em kg): "))
        
        imc, classificacao = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

# Função para cadastrar paciente
def cadastro():
    limpar_tela()
    print("----- CADASTRO -----")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cpf = int(input("Digite seu CPF: "))

    
    try:
        int(idade)
    except:
        print("❌ Idade inválida. A idade deve ser um número inteiro.")
        input("Pressione Enter para voltar ao menu...")
        menu()

    # Validação do CPF
    if cpf == "":
        print("❌ CPF inválido. O CPF não pode ser vazio.")
        menu()
    if cpf < 11:
        print("❌ CPF inválido. O CPF deve ter 11 dígitos.")
        input("Pressione Enter para voltar ao menu...")
        menu()

    if nome and idade and cpf:
        paciente = Paciente(nome, idade, cpf)
        paciente.salvar_no_bd()
    input("Pressione Enter para voltar ao menu...")
    menu()

# Função de login
# Função de login
def login():
    limpar_tela()
    print("----- LOGIN -----")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF (somente números): ").replace(".", "").replace("-", "")  # Remove pontuações

    conexao = conectar_bd()  # Abre conexão com o banco
    cursor = conexao.cursor()

    # Ajustando para garantir que estamos comparando o CPF como string
    cursor.execute("SELECT id, nome, idade, cpf FROM pacientes WHERE nome = %s AND REPLACE(REPLACE(cpf, '.', ''), '-', '') = %s", (nome, cpf))
    paciente = cursor.fetchone()  # Obtém os dados do paciente

    if paciente:
        paciente_id, nome, idade, cpf = paciente
        print(f"✅ Login concluído! Bem-vindo, {nome}.")

        input("Pressione Enter para continuar...")

        # Chama a função para coletar sintomas, passando o paciente_id
        coletar_sintomas(paciente_id)

    else:
        print("❌ Nome ou CPF incorretos. Tente novamente.")
        input("Pressione Enter para continuar...")
        menu()

    cursor.close()
    conexao.close()





# Função para coletar sintomas
def coletar_sintomas(paciente_id):
    limpar_tela()
    print("----- Sintomas -----")
    sintomas = input("Descreva detalhadamente seus sintomas: ")
    resultado = processar_sintomas(sintomas)  # IA processa os sintomas
    print("\n--- Diagnóstico Preliminar ---")
    print(resultado)
    input("\nPressione Enter para voltar ao menu...")
    menu()

# Menu principal
def menu():
    limpar_tela()
    print("----- MENU PRINCIPAL -----")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastro()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Obrigado por utilizar nosso sistema!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()

# Executa o programa
if __name__ == "__main__":
    menu()
    cursor.close()
    conexao.close()
