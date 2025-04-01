import mysql.connector

def listar_pacientes():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="FASTHEALTHY",
        database="clinica_medica",
        port = "3306"
    )
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Pacientes")
    pacientes = cursor.fetchall()

    if pacientes:
        print("\n--- Lista de Pacientes ---")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Idade: {paciente[2]}, CPF: {paciente[3]}")
    else:
        print("\nNenhum paciente cadastrado.")

    cursor.close()
    conexao.close()

# Testando a listagem
listar_pacientes()
