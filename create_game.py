import random

class Tuplas:
    def __init__(self,LINHA,COLUNA,BOMBAS):
        self.bombas = BOMBAS
        self.linha = LINHA
        self.coluna = COLUNA
        self.tupla = [[0 for j in range(self.coluna)] for i in range(self.linha)]
        self.set_bombas()
        
    def set_bombas(self):
        bombas = self.bombas
        while bombas != 0:
            x = random.randint(0,self.linha - 1)
            y = random.randint(0,self.coluna - 1)
            if self.tupla[x][y] != 'X':
                self.tupla[x][y] = 'X'
                bombas -= 1
        self.calcula_vizinhos()
        
    def calcula_vizinhos(self):
        contador = 0
        vizinhos = [[-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1], [-1,0]]
        for i in range(self.linha):
            for j in range(self.coluna):
                if self.tupla[i][j] != 'X':
                    for vizinho in vizinhos:
                        x = i+vizinho[0]
                        y = j+vizinho[1]
                        if x >= 0 and x < self.linha and y >= 0 and y < self.coluna and self.tupla[x][y] == 'X':
                            contador += 1
                    self.tupla[i][j] = contador
                    contador = 0
                    
    def get_tupla(self):
        return self.tupla
