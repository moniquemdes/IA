import numpy as np
import random
import math
#aleatorio posicao inicial dos corpos
# e formigas

class Ant:
    x = 0;
    y = 0;
    idAnt = 0;


    def __init__(self, x, y, idAnt, raio, ocupado=False):
        self.x = x
        self.y = y
        self.idAnt = idAnt
        self.raio = raio
        self.ocupado = ocupado

#raio de visão 4-> cada formuiga pode ter um raio de visão das células adjacentes (cima, baixo, esquerda, direita)

    def move(self, direcao, grid_width, grid_height):
        if direcao == 'up' and self.y > 0:
            self.y -= 1
        elif direcao == 'down' and self.y < grid_height - 1:
            self.y += 1
        elif direcao == 'left' and self.x > 0:
            self.x -= 1
        elif direcao == 'right' and self.x < grid_width - 1:
            self.x += 1

    #calcular a fração de células ocupadas por corpos no raio de visão
    def calcular_densidade_local(self, matriz):
        corpos_ao_redor = 0
        total_celulas_vistas = 0

        altura = len(matriz)
        largura = len(matriz[0])

        for dy in range(-self.raio, self.raio + 1):
            for dx in range(-self.raio, self.raio + 1):
                
                # ignora a própria posição
                if dx == 0 and dy == 0:
                    continue

                # aplica "wrap-around"
                x = (self.x + dx) % largura
                y = (self.y + dy) % altura

                total_celulas_vistas += 1

                if matriz[y][x] == 1:
                    corpos_ao_redor += 1

        if total_celulas_vistas == 0:
            return 0.0

        return corpos_ao_redor / total_celulas_vistas

