from flask import Flask, render_template, url_for, jsonify, request
from btnaval import Partida


app = Flask(__name__)

p = []
p.append(Partida())

@app.route("/")
def home():
    url_for('static', filename='indexstyle.css')
    url_for('static', filename='indexscript.js')
    return render_template('index.html')
    
@app.route("/jogo_solo")
def jogo_solo():
    global p
    del p[0]
    p.append(Partida())
    url_for('static', filename='jogo_solo.css')
    url_for('static', filename='jogo_solo.js')
    return render_template('jogo_solo.html')

@app.route("/jogar")
def jogar():
    global p
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)
    if not p[0].finaliza():
        if p[0].jogar(x,y):
            return jsonify(acertou = p[0].tabuleiro.matriz[x][y][0] != 'A',
                           fim = p[0].finaliza(),
                           pontos = p[0].pontos,
                           tiros = p[0].tiros,
                           destruiu = p[0].destruiu,
                           submarinos = p[0].tabuleiro.submarinos,
                           destroyers = p[0].tabuleiro.destroyers,
                           hidros = p[0].tabuleiro.hidros,
                           cruzadores = p[0].tabuleiro.cruzadores,
                           couracados = p[0].tabuleiro.couracados)

if __name__ == "__main__":
    app.run()
