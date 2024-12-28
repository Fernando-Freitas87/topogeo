import os
import pymysql
from flask import Flask


app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    "host": os.getenv("MYSQLHOST", "localhost"),       # Lê da variável de ambiente ou usa "localhost" como padrão
    "port": int(os.getenv("MYSQLPORT", 3306)),        # Porta definida no Railway
    "user": os.getenv("MYSQLUSER", "root"),           # Usuário definido no Railway
    "password": os.getenv("SENHA_MYSQL", ""),         # Senha definida no Railway
    "database": os.getenv("MYSQL_BANCO_DE_DADOS", "test")  # Nome do banco
}

@app.route('/')
def home():
    return "Backend conectado ao Railway!"

@app.route('/testar_conexao')
def testar_conexao():
    try:
        connection = pymysql.connect(**db_config)
        connection.close()
        return "Conexão ao banco de dados bem-sucedida!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Porta definida pelo Railway
    app.run(host="0.0.0.0", port=port)