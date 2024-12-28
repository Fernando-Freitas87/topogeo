import os
from flask import Flask
import pymysql

app = Flask(__name__)

# Configuração do banco de dados (usando variáveis de ambiente)
db_config = {
    "host": os.getenv("MYSQLHOST", "localhost"),  # Host do banco de dados
    "port": int(os.getenv("MYSQLPORT", 3306)),    # Porta do banco
    "user": os.getenv("MYSQLUSER", "root"),       # Usuário do banco
    "password": os.getenv("SENHA_MYSQL", ""),     # Senha do banco
    "database": os.getenv("MYSQL_BANCO_DE_DADOS", "test")  # Nome do banco
}

@app.route('/')
def home():
    return "Backend conectado ao Railway!"

@app.route('/testar_conexao')
def testar_conexao():
    try:
        # Testa a conexão com o banco de dados
        connection = pymysql.connect(**db_config)
        connection.close()  # Fecha a conexão após o teste
        return "Conexão ao banco de dados bem-sucedida!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

# Para evitar erros relacionados ao favicon em navegadores
@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == "__main__":
    # Porta definida pelo Railway ou 8080 como fallback
    port = int(os.getenv("PORT", 5050))
    app.run(host="127.0.0.1", port=port)