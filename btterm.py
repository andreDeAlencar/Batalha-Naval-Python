from btnaval import Partida

def imprime(tab, pontos, tiros, ptab):
        print('\nPontuação: ', pontos, end="     ")
        print('     Tiros: ', tiros, end="\n")
        for j in range(0, 17):
            print("| ", end="")
            for i in range(0, 17):
                    if tab[i][j][2]:
                        if tab[i][j][0] == 'A':
                                print('O', end=" | ")
                        else:
                                print('X', end=" | ")
                    else:
                        print(' ', end=" | ")
            print()
        print('Submarinos:\t', ptab.submarinos)
        print('Destroyers:\t', ptab.destroyers)
        print('Hidro-aviões:\t', ptab.hidros)
        print('Cruzadores:\t', ptab.cruzadores)
        print('Couraçados:\t', ptab.couracados)
 
def imprimePF(pontos, tiros, tempo, ptab):
        print('\nPontuação final: ', pontos)
        print('Tiros restantes: ', tiros)
        print('Tempo: ', tempo)
        print('Submarinos restantes:\t', ptab.submarinos)
        print('Destroyers restantes:\t', ptab.destroyers)
        print('Hidro-aviões restantes:\t', ptab.hidros)
        print('Cruzadores restantes:\t', ptab.cruzadores)
        print('Couraçados restantes:\t', ptab.couracados)


        

p = Partida()
imprime(p.tabuleiro.matriz, p.pontos, p.tiros, p.tabuleiro)
while True:     
        while True:
                x, y = input('\ncoordenadas: ').split()
                try:
                        if p.jogar(int(x), int(y)):
                                break
                except:
                        pass
        imprime(p.tabuleiro.matriz, p.pontos, p.tiros, p.tabuleiro)
        if p.finaliza():
                break
imprimePF(p.pontos, p.tiros, p.tempo, p.tabuleiro)
