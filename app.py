from flask import Flask, request
import pymysql

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    "host": "autorack.proxy.rlwy.net",  # Host do Railway
    "port": 53190,                      # Porta do Railway
    "user": "root",                     # Usuário do banco
    "password": "rZQxexeLjpxoSvRSBtYLdticiboplgm",  # Senha do banco
    "database": "railway"               # Nome do banco
}

@app.route('/')
def home():
    return "Backend conectado ao Railway!"

@app.route('/testar_conexao')
def testar_conexao():
    try:
        connection = pymysql.connect(**db_config)
        return "Conexão ao banco de dados bem-sucedida!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

if __name__ == '__main__':
    app.run(debug=True)