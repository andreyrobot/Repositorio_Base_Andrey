from flask import Flask
fk = Flask(__name__)


@fk.route('/')
def pagina():
    return 'blá blá blá blá'


@fk.route('/soma/<int:n1/<int:n2>')
def somar (n1,n2):
    return f"Sua Soma De {n1} + {n2} Tem O Resultado De {n1 + n2}"

@fk.route('/subtrair/<int:n1/<int:n2>')
def subtrair (n1,n2):
    return f"Sua subtração De {n1} - {n2} Tem O Resultado De {n1 - n2}"

@fk.route('/dividie/<int:n1/<int:n2>')
def divisão (n1,n2):
    return f"Sua divisão De {n1} / {n2} Tem O Resultado De {n1 / n2}"

@fk.route('/multiplicação/<int:n1/<int:n2>')
def multiplicação (n1,n2):
    return f"Sua multiplicação De {n1} * {n2} Tem O Resultado De {n1 * n2}"




@fk.route('/bemvindo/<name>')
def bemvindo():
    return f"Sla Mn Olha os megocio ae 😃"

if __name__ == "__main__":
    fk.run(debug=True)