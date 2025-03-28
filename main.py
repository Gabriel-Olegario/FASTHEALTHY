import mysql.connector
import os

# Conectar ao MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FASTHEALTHY",
        database="clinica_medica",
        port="3306"
    )

conexao = conectar_bd()  # Abre a conexão
cursor = conexao.cursor()

# Função para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II (severa)"
    else:
        classificacao = "Obesidade Grau III (mórbida)"

    return imc, classificacao

class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sintomas = []  # Inicializa a lista de sintomas
        self.info_doenca()  # Chama o método para coletar informações médicas

    def salvar_no_bd(self):
        try:
            sql = "INSERT INTO pacientes (nome, idade, cpf) VALUES (%s, %s, %s)"
            valores = (self.nome, self.idade, self.cpf)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Paciente cadastrado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao cadastrar usuário: {erro}")

    def info_doenca(self):
        print("-----Informações médicas importantes-----")
        altura = float(input("Altura (em metros): "))
        peso = float(input("Peso (em kg): "))

        diabetes = input("Diabetes: (Sim/Não) ")
        if diabetes == "Sim":
            tipo_diabetes = input("Tipo de diabetes: (1 / 2 / 3(gestacional)) ")
            if tipo_diabetes == "1":
                tipo_diabetes = "Diabetes Tipo 1"
            elif tipo_diabetes == "2":
                tipo_diabetes = "Diabetes Tipo 2"
            elif tipo_diabetes == "3":
                tipo_diabetes = "Diabetes Gestacional"
            else:
                tipo_diabetes = None
        elif diabetes == "Não":
            tipo_diabetes = None

        hipertensao = input("Hipertensão: (Sim/Não) ").lower()
        if hipertensao == "Sim":
            tipo_hipertensao = input("Tipo de hipertensão: (1 / 2) ")
            if tipo_hipertensao == "1":
                tipo_hipertensao = "Hipertensão Tipo 1"
            elif tipo_hipertensao == "2":
                tipo_hipertensao = "Hipertensão Tipo 2"
            else:
                tipo_hipertensao = None
        elif hipertensao == "Não":
            tipo_hipertensao = None

        problemas_cardiacos = input("Problemas cardíacos: (Sim/Não) ").lower()
        problemas_cardiacos = "Sim" if problemas_cardiacos == "Sim" else "Não"

        imc, classificacao = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

# Função para cadastro
def cadastro():
    limpar_tela()

    print("-----CADASTRO-----")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cpf = input("Digite seu CPF: ")

    if nome and idade and cpf:
        paciente = Paciente(nome, idade, cpf)  # Cria um objeto Paciente
        paciente.salvar_no_bd()  # Chama o método para salvar no banco

    print("Cadastro realizado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
    menu()

# Função de login
def login():
    limpar_tela()
    print("-----LOGIN-----")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")

    # Consultar o banco de dados para verificar se o usuário existe
    sql = "SELECT * FROM pacientes WHERE nome = %s AND cpf = %s"  # Query SQL
    valores = (nome, cpf)  # Valores a serem verificados na tabela

    cursor.execute(sql, valores)  # Executa a query
    pacientes = cursor.fetchone()  # Obtém o primeiro resultado encontrado

    if pacientes:
        print("✅ Login concluído! Bem-vindo,", pacientes[1])  # Exibe o nome do paciente
        input("Pressione Enter para continuar...")
        # Verificar se é o primeiro login, caso positivo, pedir informações médicas
        if pacientes[1]:  # Verificar se o paciente já tem as informações médicas
            print("Você já possui informações médicas registradas.")
        else:
            print("Por favor, preencha suas informações médicas.")
            paciente = Paciente(pacientes[1], pacientes[2], pacientes[3])  # Exemplo de objeto paciente
            paciente.info_doenca()  # Coletar informações médicas
        sintomas_sentindo()
    else:
        print("❌ Nome ou CPF incorretos. Tente novamente.")
        input("Pressione Enter para continuar...")
        menu()

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para o menu principal
def menu():
    limpar_tela()
    print("-----MENU PRINCIPAL-----")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        login()
    elif opcao == 3:
        print("Obrigado por utilizar nosso sistema")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()

# Função para o menu de sintomas
def sintomas_sentindo():
    limpar_tela()
    print("-----Sintomas-----")
    sintomas = input("Descreva detalhadamente seus sintomas: ")
    # Processar os sintomas com IA aqui
    print(f"Você informou os seguintes sintomas: {sintomas}")
    print("IA processando...")  # Aqui você integraria a IA para fornecer o diagnóstico
    print("Possíveis diagnósticos e recomendações serão fornecidos em breve.")
    pass

# Função principal
def main():
    limpar_tela()
    menu()

main()

# Fechando a conexão com o MySQL ao final do programa
cursor.close()  # Fecha o cursor
conexao.close()  # Fecha a conexão com o banco de dados
