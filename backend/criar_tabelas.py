import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FASTHEALTHY",
    database="clinica_medica",
    port="3306"
)

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sintomas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES Pacientes(id) ON DELETE CASCADE
)
""")

print("✅ Tabela 'Sintomas' criada com sucesso!")

cursor.close()
conexao.close()
