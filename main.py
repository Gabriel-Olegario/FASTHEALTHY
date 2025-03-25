import mysql.connector
import os 

# Conectar ao MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FASTHEALTHY",
    database="clinica_medica",
    port = "3306"
)

cursor = conexao.cursor()

class Paciente:
    Pacientes =[]
    def __init__(self, _nome, _idade, _CPF):
        self._nome = _nome
        self._idade = _idade
        self._CPF = _CPF
        #Adiciona pacientes na lista Pacientes 
        Paciente.Pacientes.append(self)

     
    def __str__(self):
        return f"{self._nome}\n {self._idade}\n {self._CPF}"

    @classmethod
    def listar_pacientes(cls):
       pass


def cadastro():
    print("-----SEJA BEM-VINDO-----")
    print("Deseja fazer login?")
    print("1 - Sim")
    print("2 - Não")
    opcao = int(input("Digite a opção desejada: "))
    
    try:
        if opcao == 1:
            login()
            return  # 🔹 Para evitar que continue a execução da função
        elif opcao == 2:    
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            CPF = input("Digite seu CPF: ")

    except ValueError:
        print("Opção inválida. Tente novamente.")
        cadastro()
        return  # 🔹 Para evitar que continue a execução da função

    if nome and idade and CPF:  # 🔹 Verifica se as variáveis foram preenchidas
        try:
            sql = "INSERT INTO Pacientes (nome, idade, CPF) VALUES (%s, %s, %s)"
            valores = (nome, idade, CPF)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Paciente cadastrado com sucesso!")
        except mysql.connector.Error as erro:
            print(f"Erro ao cadastrar usuário: {erro}")
            
    cursor.close()
    conexao.close()

    
    login()
            
def login():
    limpar_tela()
    print("-----LOGIN-----")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    CPF = input("Digite seu CPF: ")

 # Consultar o banco de dados para verificar se o usuário existe
    sql = "SELECT * FROM pacientes WHERE nome = %s AND idade = %s AND cpf = %s"
    valores = (nome, idade, CPF)
    
    cursor.execute(sql, valores)
    pacientes = cursor.fetchone()  # Obtém o primeiro resultado encontrado

    if pacientes:
        print("✅ Login concluído! Bem-vindo,", pacientes[1])
    else:
        print("❌ Nome ou CPF incorretos. Tente novamente.")
            
    cursor.close()
    conexao.close()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')       
def menu():
    limpar_tela()
    print("-----MENU-----")
    print("1 - Pesquisar sintomas")
    print("2 - Minhas informações")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        sintomas_sentindo()
    elif opcao == 2:
        pass
    elif opcao == 3:
        print("Obrigado por utilizar nosso sistema")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu()
def sintomas_sentindo():
    pass
def main():
    limpar_tela()
    cadastro()    
    #login()

    

main()
