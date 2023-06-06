from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/personalizada')
def home_perso():
    usu = 'Fabrício Galende M. de Carvalho'
    # Para ler dados do BD ou csv (usar pandas)
    # criar a variável com os dados da lista
    # enviar para a aplicação de modo similar.
    return render_template('home_personalizada.html', usuario=usu)

