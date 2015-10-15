import random
from timeit import default_timer as timer
from datetime import datetime

#Faz numeros aleatorios de verdade
random.seed(datetime.now())

class Partida():

    def __init__(self, n, s):
        self.tempoI = timer() 
        self.pontos = 0
        self.jogador = 'Player'
        self.tab = Tab(n)
        self.tab.alocAuto(s)
        while(self.tab.imprime(self) or self.tab.endCheck()):
            x, y = input('coordenadas (1 a %d): ' % n).split()
            self.tab.submDestroy(int(x), int(y), self)
        self.tempoF = timer()
        print('Tempo: %d segundo(s)'% (self.tempoF - self.tempoI))
        print("fim")

    def maisPontos(self):
        self.pontos += 1

class Submarino():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
class Tab():
    
    #Função construtora
    def __init__(self, n):
        self.tmatriz = n
        self.subs = [] #Quantidade de submarinos vivos
        self.matriz = [[0 for x in range(self.tmatriz + 2)] for x in range(self.tmatriz + 2)] #Gera uma matriz preenchida com zeros 
        
        #Preenche a matriz com espaços vazios
        for j in range(0, self.tmatriz + 2):
            for i in range(0, self.tmatriz + 2):
                self.matriz[i][j] = ' '
        
        #Preenche as bordas com X
        for i in range(0 ,self.tmatriz + 2):
            self.matriz[0][i] = 'X'
            self.matriz[i][0] = 'X'
            self.matriz[self.tmatriz + 1][i] = 'X'
            self.matriz[i][self.tmatriz + 1] = 'X'
    
    #Checa se a posição recebida tem espaços ocupados em volta
    def check(self, x, y):
        f = False
        for j in range(-1, 2):
            for i in range(-1, 2):
                if self.matriz[x + i][y + j] == 'S':
                    f = True
        return f
    
    #Marca a posição onde está o submarino
    def deploySubm(self, x, y):
        if not self.check(x, y):
            self.subs.append(Submarino(x, y))
            self.matriz[x][y] = 'S'
            return True
        else:
            return False
     
    #Imprime o tabuleiro   
    def imprime(self, p):
        print()
        print('Pontuação: %d' % p.pontos)
        for j in range(0, self.tmatriz + 2):
            print("| ", end="")
            for i in range(0, self.tmatriz + 2):
                print(self.matriz[i][j], end=" | ")
            print() 
    
    #Aloca a quantidade de submarinos recebida em posições aleatorias
    def alocAuto(self, n):
        while n > 0:
            if self.deploySubm(random.randint(1, self.tmatriz), random.randint(1, self.tmatriz)):
                n = n - 1
    
    #Checa se todos os submarinos ja foram destruidos            
    def endCheck(self):
        if self.subs == []:
            return False
        else:
            return True
    
    #Destroi submarino ou acerta a agua dependendo da posição recebida        
    def submDestroy(self, x, y, p):
        if self.matriz[x][y] == 'S':
            for v in self.subs:
                if v.x == x and v.y == y:
                    self.subs.remove(v)
            self.matriz[x][y] = 'D'
            p.maisPontos()
        elif self.matriz[x][y] == ' ':
            self.matriz[x][y] = 'A'
        else:
            print("Já destruido")
                
                



n, s = input('Tamanho e Quantidade: ').split()
p = Partida(int(n), int(s))
       
