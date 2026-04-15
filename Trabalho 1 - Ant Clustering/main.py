from ant import Ant
import random
import math
import time  

if __name__ == '__main__':

    TAMANHO_MATRIZ = 64
    NUM_ITENS = 300
    NUM_FORMIGAS = 15
    ITERACOES = 100000

    matriz = [[0 for _ in range(TAMANHO_MATRIZ)] for _ in range(TAMANHO_MATRIZ)]

    itens_colocados = 0
    while itens_colocados < NUM_ITENS:
        x_rand = random.randint(0, TAMANHO_MATRIZ - 1)
        y_rand = random.randint(0, TAMANHO_MATRIZ - 1)

        if matriz[y_rand][x_rand] == 0:
            matriz[y_rand][x_rand] = 1
            itens_colocados += 1

    formigas = []
    for i in range(NUM_FORMIGAS):
        x_ant = random.randint(0, TAMANHO_MATRIZ - 1)
        y_ant = random.randint(0, TAMANHO_MATRIZ - 1)
        nova_formiga = Ant(x=x_ant, y=y_ant, idAnt=i+1, raio=1, ocupado=False)
        formigas.append(nova_formiga)

    altura_matriz = TAMANHO_MATRIZ
    largura_matriz = TAMANHO_MATRIZ

    print("\nEstado INICIAL da matriz:")
    for linha in matriz:
        print(''.join(f"{'1' if x == 1 else ' ':>2}" for x in linha))
    print("-" * 40)
    
    tempo_inicio = time.time()

    for iteracao in range(ITERACOES):
        for formiga in formigas:
            densidade = formiga.calcular_densidade_local(matriz)
            direcao = random.choice(['up', 'down', 'left', 'right'])
            
            if not formiga.ocupado: 
                if matriz[formiga.y][formiga.x] == 1:
                    if densidade < random.random(): 
                        formiga.ocupado = True
                        matriz[formiga.y][formiga.x] = 0 
                    else:
                        formiga.move(direcao, largura_matriz, altura_matriz)
                else: 
                    formiga.move(direcao, largura_matriz, altura_matriz)

            else: 
                if matriz[formiga.y][formiga.x] == 0:
                    if densidade > random.random(): 
                        formiga.ocupado = False
                        matriz[formiga.y][formiga.x] = 1 
                    else:
                        formiga.move(direcao, largura_matriz, altura_matriz)
                else: 
                    formiga.move(direcao, largura_matriz, altura_matriz)


    tempo_fim = time.time()
    
    tempo_total = tempo_fim - tempo_inicio

    print("\nEstado FINAL da matriz:")
    for linha in matriz:
        print(''.join(f"{'1' if x == 1 else ' ':>2}" for x in linha))
    print("-" * 40)
    
    print(f"Tempo total de execução: {tempo_total:.2f} segundos.")
