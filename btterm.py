from btnaval import Partida

def imprime(tab):
        print()
        for j in range(0, 17):
            print("| ", end="")
            for i in range(0, 17):
                try:
                    print(tab[i][j][0], end=" | ")
                except TypeError:
                    print(' ', end=" | ")
            print("\n")

p = Partida()
imprime(p.jogar())
