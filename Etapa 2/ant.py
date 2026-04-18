from ant import Ant
from corpo import Corpo
import random
import math

def carregar_corpos(caminho):
    corpos = []

    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip()

            if linha == "" or linha.startswith("#"):
                continue

            partes = linha.split()

            x = float(partes[0].replace(",", "."))
            y = float(partes[1].replace(",", "."))
            grupo = int(partes[2])

            corpos.append(Corpo(x, y, grupo))

    return corpos

if __name__ == '__main__':

    TAMANHO_MATRIZ = 50
    # NUM_CORPOS = 300
    NUM_FORMIGAS = 150
    ITERACOES = 700000000

    matriz = [[0 for _ in range(TAMANHO_MATRIZ)] for _ in range(TAMANHO_MATRIZ)]

   
    corpos = carregar_corpos("base.txt")

    for corpo in corpos:
        while True:
            x_rand = random.randint(0, TAMANHO_MATRIZ - 1)
            y_rand = random.randint(0, TAMANHO_MATRIZ - 1)

            if matriz[y_rand][x_rand] == 0:
                matriz[y_rand][x_rand] = corpo
                break

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
        print(''.join(f"{x.grupo if x != 0 else ' ':>2}" for x in linha))
    print("-" * 40)

    tempo_inicio = time.time()

    for iteracao in range(ITERACOES):
        for formiga in formigas:
            
            direcao = random.choice(['up', 'down', 'left', 'right'])
            corpo_atual = matriz[formiga.y][formiga.x]
            
            
            # if not formiga.ocupado: 
            #     if matriz[formiga.y][formiga.x] == 1:
            #         if probabilidade_pegar < random.random(): 
            #             formiga.ocupado = True
            #             matriz[formiga.y][formiga.x] = 0 
            #         else:
            #             formiga.move(direcao, largura_matriz, altura_matriz)
            #     else: 
            #         formiga.move(direcao, largura_matriz, altura_matriz)

            
            # else: 
            #     if matriz[formiga.y][formiga.x] == 0:
            #         if probabilidade_largar > random.random(): 
            #             formiga.ocupado = False
            #             matriz[formiga.y][formiga.x] = 1 
            #         else:
            #             formiga.move(direcao, largura_matriz, altura_matriz)
            #     else: 
            #         formiga.move(direcao, largura_matriz, altura_matriz)    

            if not formiga.ocupado: 
                if corpo_atual != 0:
                    similaridade = formiga.calcular_similaridade(matriz, corpo_atual)
                    prob_pegar = formiga.probabilidade_pegar(similaridade)
                    
                    if prob_pegar > random.random(): 
                        formiga.ocupado = True
                        formiga.item_carregado = corpo_atual 
                        matriz[formiga.y][formiga.x] = 0     
                    else:
                        formiga.move(direcao, largura_matriz, altura_matriz)
                else: 
                    formiga.move(direcao, largura_matriz, altura_matriz)
            
            else: 
                if corpo_atual == 0: 
                   
                    similaridade = formiga.calcular_similaridade(matriz, formiga.item_carregado)
                    prob_largar = formiga.probabilidade_largar(similaridade)
                    
                    if prob_largar > random.random(): 
                        matriz[formiga.y][formiga.x] = formiga.item_carregado 
                        formiga.ocupado = False
                        formiga.item_carregado = None
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

    #metrica de distancia vetorial / mediana / manhattan / cosseno / euclidiana 
    #fazer com a vizinhança de cada formiga, calcular a distância média entre os corpos e comparar com a distância média inicial para avaliar a eficácia da organização.
