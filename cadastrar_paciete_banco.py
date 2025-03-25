import mysql.connector
def cadastrar_paciente(nome, idade, cpf):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FASTHEALTHY",
        database="clinica_medica",
        port = "3306"
    )
    cursor = conexao.cursor()

    sql = "INSERT INTO Pacientes (nome, idade, cpf) VALUES (%s, %s, %s)"
    valores = (nome, idade, cpf)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Paciente cadastrado com sucesso!")

    cursor.close()
    conexao.close()

# Testando o cadastro
cadastrar_paciente("João Silva", 30, "123.456.789-00")
