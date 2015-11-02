from datetime import datetime


class Partida():

    def __init__(self):
        self.inicio = datetime.now()
        self.fim = self.inicio
        self.pontos = 0
        self.tabuleiro = Tabuleiro()

    def posicao_disponivel(self, x, y):
        disponivel = True
        for j in range(-1, 2):
            for i in range(-1, 2):
                if self.tabuleiro[x + i][y + j] != 0:
                    disponivel = False
        return disponivel

    def aloca_destroyer(self, pos1, pos2):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]):
            self.tabuleiro.matriz[pos1[0]][pos[1]] = 

    def aloca_submarino(self, x, y):
        if self.posicao_disponivel(x, y):
            self.tabuleiro.matriz[x][y] = Submarino()
            self.tabuleiro.embarcacoes.append(self.tabuleiro.matriz[x][y])

    def destroi_submarino(self, submarino):
        submarino.destruido = True
        self.tabuleiro.embarcacoes.remove(submarino)

    #def jogar(self, x, y):
        

    def finaliza(self):
        self.fim = datetime.now()
        del self


class Tabuleiro():

    def __init__(self):
        self.matriz = [[0 for x in range(17)] for x in range(17)]
        self.embarcacoes = []

class Destroyer():

    def __init__(self, pos1, pos2):
        parte1 = {x: pos1[0], y: pos1[1], destruido: False}
        parte2 = {x: pos2[0], y: pos2[1], destruido: False}


class Submarino():

    def __init__(self, x, y):
        x = x
        y = y
        destruido = False
