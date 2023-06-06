from flask import app, Flask, render_template

minha_app = Flask(__name__)

@minha_app.route('/')
def home():
    return render_template('home.html')


@minha_app.route('/personalizada')
def home_perso():
    usu = 'PASTEL DE COXINHA'
    # Para ler dados do BD ou csv (usar pandas)
    # criar a variável com os dados da lista
    # enviar para a aplicação de modo similar.
    return render_template('home_personalizada.html', usuario=usu)

if __name__ == '__main__':
    minha_app.run('0.0.0.0')