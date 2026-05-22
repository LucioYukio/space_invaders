from multiprocessing.spawn import old_main_modules
from typing import List
from PPlay import sprite
import settings
from settings import velocidade_movimento_inimigo


#-----INIMIGO-----

# Cria a matriz dos inimigos, bota o sprite e define a posição inicial deles, recebe uma matriz vazia e a quantidade de linhas (l) e de colunas (c) pra criar a matriz
def matriz_inimigo(mat: List[List[sprite.Sprite]], l, c):
    mat.clear()
    for i in range(l):
        linha : List[sprite.Sprite] = []
        for j in range(c):
            inimigo = sprite.Sprite("assets/inimigo.png")
            linha.append(inimigo)
        mat.append(linha)
    cont = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j==0 and i == j:
                 mat[i][j].x = settings.tela.width/4 
                 mat[i][j].y = 0 
            elif j==0:
                mat[i][j].x = mat[i-1][j].x 
                mat[i][j].y = mat[i-1][j].y + inimigo.height + inimigo.height/2 
            else:
                mat[i][j].x = mat[i][j-1].x + inimigo.width + inimigo.width/2 
                mat[i][j].y = mat[i][j-1].y
        

# Aplica a movimentação do inimigo
def movimento_inimigo(mat:List[List[sprite.Sprite]]):
    inimigo = sprite.Sprite("assets/inimigo.png")
    settings.tempo_atual_inimigo += settings.tela.delta_time()
    if settings.tempo_atual_inimigo>=settings.movimentacao_inimigo:
        for i in mat:
            for j in i:
                j.x += settings.velocidade_movimento_inimigo
        if mat[0][-1].x + inimigo.width >= settings.tela.width and settings.velocidade_movimento_inimigo>0:
            settings.velocidade_movimento_inimigo *= -1
            for a in mat:
                for b in a:
                    b.y += inimigo.height
        elif mat[0][0].x <= 0 and settings.velocidade_movimento_inimigo < 0:
            settings.velocidade_movimento_inimigo *= -1
            for a in mat:
                for b in a:
                    b.y += inimigo.height
        settings.tempo_atual_inimigo = 0

# Desenha o inimigo
def desenha_inimigo():
    for i in settings.mat_inimigo:
        for j in i:
            j.draw()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=