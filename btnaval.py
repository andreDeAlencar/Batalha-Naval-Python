from datetime import datetime
import random 
random.seed(datetime.now())


class Partida():

    def __init__(self):
        self.inicio = datetime.now()
        self.fim = self.inicio
        self.pontos = 0
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.alocacao_automatica()
            
            

    def jogar(self):
        return self.tabuleiro.matriz
        

    def finaliza(self):
        self.fim = datetime.now()
        del self


class Tabuleiro():

    def __init__(self):
        self.matriz = [[0 for x in range(17)] for x in range(17)]
        for j in range(17):
            for i in range(17):
                self.matriz[i][j] = [' ', False]
        self.submarinos = 0
        self.destroyers = 0
        self.hidros = 0
        self.cruzadores = 0
        self.couracados = 0
        


    def posicao_disponivel(self, x, y):
        disponivel = True
        for j in range(-1, 2):
            for i in range(-1, 2):
                if self.matriz[x + i][y + j][0] != ' ':
                    disponivel = False
        return disponivel


    def aloca_submarino(self, pos):
        if self.posicao_disponivel(pos[0], pos[1]):
            self.submarinos += 1
            self.matriz[pos[0]][pos[1]] = ['S', self.submarinos, 1, False]
            return True
        else:
            return False
            
    def aloca_destroyer(self, pos1, pos2):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]):
            self.destroyers += 1
            self.matriz[pos1[0]][pos1[1]] = ['D', self.destroyers, 1, False]
            self.matriz[pos2[0]][pos2[1]] = ['D', self.destroyers, 2, False]
            return True
        else:
            return False
            
    def aloca_hidro(self, pos1, pos2, pos3):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]) and self.posicao_disponivel(pos3[0], pos3[1]):
            self.hidros += 1
            self.matriz[pos1[0]][pos1[1]] = ['H', self.hidros, 1, False]
            self.matriz[pos2[0]][pos2[1]] = ['H', self.hidros, 2, False]
            self.matriz[pos3[0]][pos3[1]] = ['H', self.hidros, 3, False]
            return True
        else:
            return False
        
    def aloca_cruzador(self, pos1, pos2, pos3, pos4):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]) and self.posicao_disponivel(pos3[0], pos3[1]) and self.posicao_disponivel(pos4[0], pos4[1]):
            self.cruzadores += 1
            self.matriz[pos1[0]][pos1[1]] = ['C', self.cruzadores, 1, False]
            self.matriz[pos2[0]][pos2[1]] = ['C', self.cruzadores, 2, False]
            self.matriz[pos3[0]][pos3[1]] = ['C', self.cruzadores, 3, False]
            self.matriz[pos4[0]][pos4[1]] = ['C', self.cruzadores, 4, False]
            return True
        else:
            return False
        
    def aloca_couracado(self, pos1, pos2, pos3, pos4, pos5):
        if self.posicao_disponivel(pos1[0], pos1[1]) and self.posicao_disponivel(pos2[0], pos2[1]) and self.posicao_disponivel(pos3[0], pos3[1]) and self.posicao_disponivel(pos4[0], pos4[1]) and self.posicao_disponivel(pos5[0], pos5[1]):
            self.couracados += 1
            self.matriz[pos1[0]][pos1[1]] = ['Ç', self.couracados, 1, False]
            self.matriz[pos2[0]][pos2[1]] = ['Ç', self.couracados, 2, False]
            self.matriz[pos3[0]][pos3[1]] = ['Ç', self.couracados, 3, False]
            self.matriz[pos4[0]][pos4[1]] = ['Ç', self.couracados, 4, False]
            self.matriz[pos5[0]][pos5[1]] = ['Ç', self.couracados, 5, False]
            return True
        else:
            return False
        
    def alocacao_automatica(self):
        #hidro
        off = [-1, 1]
        for i in range(5):
            while True:
                x = random.randint(2,14)
                y = random.randint(2,14)
                offx = random.choice(off)
                offy = random.choice(off)
                offx2 = random.choice(off)
                offy2 = random.choice(off)
                while offx2*offy2 == offx*offy:
                    offx2 = random.choice(off)
                    offy2 = random.choice(off)
                if self.aloca_hidro((x, y), (x + offx, y + offy), (x + offx2, y + offy2)):
                    break
               

        #couraçado
        while True:
            x = random.randint(5,10)
            y = random.randint(5,10)
            offx = random.randint(-1, 1)
            if offx == 0:
                offy = random.choice(off)
            else:
                offy = 0       
            if self.aloca_couracado((x, y),(x + offx, y + offy),(x + 2*offx, y + 2*offy),(x + 3*offx, y + 3*offy),(x + 4*offx, y + 4*offy)):
                break
        
        #cruzador        
        for i in range(2):
            while True:
                x = random.randint(4,11)
                y = random.randint(4,11)
                offx = random.randint(-1, 1)
                if offx == 0:
                    offy = random.choice(off)
                else:
                    offy = 0       
                if self.aloca_cruzador((x, y),(x + offx, y + offy),(x + 2*offx, y + 2*offy),(x + 3*offx, y + 3*offy)):
                    break
                
        #destroyer            
        for i in range(3):
            while True:
                x = random.randint(2,14)
                y = random.randint(2,14)
                offx = random.randint(-1, 1)
                if offx == 0:
                    offy = random.choice(off)
                else:
                    offy = 0       
                if self.aloca_destroyer((x, y),(x + offx, y + offy)):
                    break
                
        #submarino        
        for i in range(4):
            while True:
                x = random.randint(1,15)
                y = random.randint(1,15)
                if self.aloca_submarino((x, y)):
                    break
