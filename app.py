from flask import Flask, request
import pymysql
import os

app = Flask(__name__)

# Configuração do banco de dados (usando variáveis de ambiente)
db_config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),       # Host do banco
    "port": int(os.getenv("MYSQL_PORT", 3306)),         # Porta do banco
    "user": os.getenv("MYSQL_USER", "root"),            # Usuário
    "password": os.getenv("MYSQL_PASSWORD", ""),        # Senha
    "database": os.getenv("MYSQL_DATABASE", "test")     # Nome do banco
}

@app.route('/')
def home():
    return "Backend conectado ao Railway!"

@app.route('/testar_conexao')
def testar_conexao():
    try:
        # Conectando ao banco de dados
        connection = pymysql.connect(**db_config)
        connection.close()  # Fechar a conexão após o teste
        return "Conexão ao banco de dados bem-sucedida!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

if __name__ == '__main__':
    # Usar a porta definida pelo Railway
    port = int(os.getenv("PORT", 8080))  # Defina a porta padrão como 8080
    app.run(host="0.0.0.0", port=port)