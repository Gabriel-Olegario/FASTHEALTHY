import mysql.connector

# Conectar ao MySQL (substitua os valores conforme seu MySQL)
conexao = mysql.connector.connect(
    host="localhost",       # Servidor MySQL (local)
    user="root",            # Usuário do MySQL
    password="FASTHEALTHY",    # Sua senha do MySQL
    port = "3306"
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar um banco de dados chamado 'clinica_medica'
cursor.execute("CREATE DATABASE IF NOT EXISTS clinica_medica")

print("Banco de dados criado com sucesso!")

# Fechar a conexão
cursor.close()
conexao.close()