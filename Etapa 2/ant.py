import numpy as np
import random
import math

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
        self.item_carregado = None

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

    def calcular_similaridade(self, matriz, corpo_referencia):
        if corpo_referencia is None:
            return 0.0

        soma_similaridade = 0.0
        total_celulas_vistas = 0
       
        alpha = 2
        altura = len(matriz)
        largura = len(matriz[0])

        for dy in range(-self.raio, self.raio + 1):
            for dx in range(-self.raio, self.raio + 1):
                
                if dx == 0 and dy == 0:
                    continue

                x = (self.x + dx) % largura
                y = (self.y + dy) % altura

                total_celulas_vistas += 1
                vizinho = matriz[y][x]

                if vizinho != 0: 
                    dist_euclidiana = math.sqrt((corpo_referencia.x - vizinho.x)**2 + (corpo_referencia.y - vizinho.y)**2)

                    similaridade = 1.0 - (dist_euclidiana / alpha)
                    soma_similaridade += similaridade

        if total_celulas_vistas == 0:
            return 0.0

        f = soma_similaridade / total_celulas_vistas
        return max(0.0, f)

    def probabilidade_pegar(self, similaridade):
        k1 = 0.3 
        return (k1 / (k1 + similaridade)) ** 2
    
    def probabilidade_largar(self, similaridade):
        k2 = 0.05
        return (similaridade / (k2 + similaridade)) ** 2
