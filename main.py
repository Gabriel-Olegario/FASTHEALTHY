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

class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.info_doenca()  # Chama o método para coletar informações médicas
        self.sintomas = []  # Inicializa a lista de sintomas

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
        altura = float(input("Altura:"))
        peso = float(input("Peso:"))

        diabetes = input("Diabetes: (Sim/Não)")
        if diabetes == "Sim":
            tipo_diabetes = input("Tipo de diabetes: (1 / 2 / 3(gestacional))")
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
       
        hipertensao = input("Hipertensão: (Sim/Não)").lower()
        if hipertensao == "Sim":
            tipo_hipertensao = input("Tipo de hipertensão: (1 / 2)").lower()
            if tipo_hipertensao == "1":
                tipo_hipertensao = "Hipertensão Tipo 1"
            elif tipo_hipertensao == "2":
                tipo_hipertensao = "Hipertensão Tipo 2"
            else:
                tipo_hipertensao = None
        elif hipertensao == "Não":
            tipo_hipertensao = None
        
        problemas_cardiacos = input("Problemas cardíacos: (Sim/Não)").lower()
        if problemas_cardiacos == "Sim":
            problemas_cardiacos = "Sim"
        else:
                problemas_cardiacos = False

        imc, classificacao = calcular_imc(peso, altura)
        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

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
    

def cadastro():
    limpar_tela()

    print("-----SEJA BEM-VINDO-----")
    print("Deseja fazer login?")
    print("1 - Sim")
    print("2 - Não")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    
    try:
        if opcao == 1:
            login()
            return
        elif opcao == 2:    
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            cpf = input("Digite seu CPF: ")
        elif opcao == 3:
            print("Obrigado por utilizar nosso sistema")
            exit()
    except ValueError:
        print("Opção inválida. Tente novamente.")
        return  

    if nome and idade and cpf:
        paciente = Paciente(nome, idade, cpf)  # Cria um objeto Paciente
        paciente.salvar_no_bd()  # Chama o método para salvar no banco

    login()

            
def login():
    limpar_tela()
    print("-----LOGIN-----")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")

 # Consultar o banco de dados para verificar se o usuário existe
    # O código literalmente manda o texto abaixo e cola no cursor para executar
    sql = "SELECT * FROM pacientes WHERE nome = %s AND cpf = %s" # Query SQL para verificar se o paciente existe na tabela
    valores = (nome, cpf) # Valores a serem verificados na tabela
    
    cursor.execute(sql, valores) # Executa a query com os valores
    # O fetchone() retorna uma linha do resultado da consulta
    pacientes = cursor.fetchone()  # Obtém o primeiro resultado encontrado

    if pacientes:
        print("✅ Login concluído! Bem-vindo,", pacientes[1]) # Exibe o nome do paciente (índice 1 da tupla retornada)
        input("Pressione Enter para continuar...")
        menu()
    else:
        print("❌ Nome ou CPF incorretos. Tente novamente.")
        input("Pressione Enter para continuar...")
        cadastro()

            

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')       

#Rascunho de um possível menu

def menu():
    limpar_tela()
    print("-----MENU-----")
    print("1 - Pesquisar sintomas")
    print("2 - Informações médicas")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        sintomas_sentindo()
    elif opcao == 2:
        info_doenca()
    elif opcao == 3:
        print("Obrigado por utilizar nosso sistema")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()

# A I.A tem que ser implementada aqui
def sintomas_sentindo():
    limpar_tela()
    print("-----Sintomas-----")
    pass
def main():
    limpar_tela()
    cadastro()    
    #login()

    

main()

# Fechando a conexão com o MySQL ao final do programa
cursor.close()  # Fecha o cursor
# Fechar a conexão com o banco de dados
conexao.close()

