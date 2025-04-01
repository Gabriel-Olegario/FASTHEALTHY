import mysql.connector

# Conectar ao MySQL e ao banco de dados criado
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FASTHEALTHY",
    database="clinica_medica",
    port = "3306"
)

cursor = conexao.cursor()

# Criar a tabela Pacientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL
)
""")

print("Tabela 'Pacientes' criada com sucesso!")

# Fechar a conexão
cursor.close()
conexao.close()
