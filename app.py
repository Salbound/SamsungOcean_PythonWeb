from flask import Flask, g, render_template, flash, request, redirect
import sqlite3


DATABASE = "blog.bd"
SECRET_KEY = "pudim"

# Pré confighurando o servidor
app = Flask(__name__)
app.config.from_object(__name__)

# Abrir conexão com banco. Não esquecer de criar um arquivo antes próprio do banco no terminal 'sqlite3 blog.bd < esquema.sql'
def conectar_bd():
    return sqlite3.connect(DATABASE)

# Sim, o 'g' no def é uma classe da biblioteca do Flask.g ¯\_(ツ)_/¯. 
@app.before_request
def antes_requisição():
    g.bd = conectar_bd()

# Sim, o parâmetro exc não é utilizado nesse caso, entretanto é obrigatório colocar. Exc = exception, para guardar log de erro no return.
@app.teardown_request
def fim_requisição(exc):
    g.bd.close()

# Inicializando o servidor e banco
@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({
            "titulo": titulo,
            "texto": texto
            })
    return render_template("exibir_entradas.html", posts=entradas)

@app.route('/inserir', methods=['POST'])
def inserir_entrada():
    sql = "INSERT INTO entradas(titulo, texto) VALUES (?, ?);"
    titulo = request.form['titulo']
    texto = request.form['texto']
    g.bd.execute(sql, [titulo, texto])
    g.bd.commit()
    return redirect('/')






# ================================
#Usando GitPod
#- Cria um repositoróio GitHub
#- Entre no GitPod
#- Na Url do gitpod adicione /#[Url_repositório_GitHub)
#	Ex: gitpod.io/#https://github.com/Salbound/SamsungOcean_PythonWeb
#- Uma interface igual do VSCode abrirá


#Comandos pip/python
#pip flask
#pip install python-dotenv
#pip install pyngrok
#pip freeze ==> Lista todas as bibliotecas instaladas no python
#pip freeze > [nome.arquivo.txt] ==> salva em um arquivo txt o nome das bibliotecas instaladas
#pip install -r requirements.txt ==> Irá instalar todas as bibliotecas que estão dentro do requirements.txt


# sudo apt install python3-dev ==> No GitPod.io deu problema no python. Precisou rodar um comando de linux para forçar a install o Python3 na máquina.

#Comandos terminal
# sqlite3 blog.bd < esquema.sql
# sqlite3 blog.bd ==> para entrar no banco e poder colocar comandos SQL
# INSERT INTO entradas(titulo, texto) VALUES ('teste de entrada', 'texto de testye');
# SELECT * FROM entradas;
# Ctrl+D para sair do sqlite3

#Flask
# Após montar código, no terminal digite 'flask run'. Ele irá montar o servidor HTTP.
# Cliclando no http criando (Running on http://127.0.0.1:5000/), você irá para uma pagina em branco.
# Para acessar a página que foi digitada, é preciso alterar a URL no final com a informação do @app.route
#	Ex: https://5000-salbound-samsungoceanpyt-lmxzvsyxun9.ws-us31.gitpod.io/home

#arquivo '.flaskenv' é um txt sem extensão, o qual ele configura o environment do servidor Flask

# Comandos GIT para atualizar no github (não tem salvar aqui direto no git)
#git add .
#git commit -m "primeira parte"
#git push

#https://github.com/feulo-ocean/aula_python_web
#http://turing.com.br/material/flask/tutorial/index.html