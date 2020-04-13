import random

class Tuplas:
    def __init__(self,LINHA,COLUNA,BOMBAS):
        self.tupla = []
        self.bombas = BOMBAS
        self.linha = LINHA
        self.coluna = COLUNA
        self.set_tupla()
        
    def set_tupla(self):
        temp = []
        for i in range(self.linha):
            for j in range(self.coluna):
                temp.append(0)
            self.tupla.append(temp)
            temp = []
        self.set_bombas()
        
    def set_bombas(self):
        bombas = self.bombas
        while bombas != 0:
            linha = random.randint(0,self.linha - 1)
            coluna = random.randint(0,self.coluna - 1)
            if self.tupla[linha][coluna] != 'X':
                self.tupla[linha][coluna] = 'X'
                bombas = bombas - 1
        self.calcula_vizinhos()
        
    def calcula_vizinhos(self):
        contador = 0
        for i in range(self.linha):
            for j in range(self.coluna):
                if self.tupla[i][j] != 'X':
                    try:
                        if i-1 >= 0 and j-1 >= 0 and self.tupla[i-1][j-1] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i-1 >= 0 and j >= 0 and self.tupla[i-1][j] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i-1 >= 0 and j+1 >= 0 and self.tupla[i-1][j+1] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i >= 0 and j-1 >= 0 and self.tupla[i][j-1] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i >= 0 and j+1 >= 0 and self.tupla[i][j+1] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i+1 >= 0 and j-1 >= 0 and self.tupla[i+1][j-1] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i+1 >= 0 and j >= 0 and self.tupla[i+1][j] == 'X':
                            contador += 1
                    except:
                        pass
                    try:
                        if i+1 >= 0 and j+1 >= 0 and self.tupla[i+1][j+1] == 'X':
                            contador += 1
                    except:
                        pass
                    self.tupla[i][j] = contador
                    contador = 0
                    
    def get_tupla(self):
        return self.tupla
