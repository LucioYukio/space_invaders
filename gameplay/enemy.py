from multiprocessing.spawn import old_main_modules
from typing import List
from random import randint, choice
from PPlay import sprite
import settings
from settings import velocidade_movimento_inimigo


#-----INIMIGO-----

# Cria a matriz dos inimigos, bota o sprite e define a posição inicial deles, recebe uma matriz vazia e a quantidade de linhas (l) e de colunas (c) pra criar a matriz
def matriz_inimigo(mat: List[List[sprite.Sprite]]):
    l = 3 + (settings.dificuldade // 2)
    c = 6 + settings.dificuldade
    print(l,c)
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
                 mat[i][j].x = settings.tela.width/11
                 mat[i][j].y = 0 
            elif j==0:
                mat[i][j].x = mat[i-1][j].x 
                mat[i][j].y = mat[i-1][j].y + inimigo.height + inimigo.height/2 
            else:
                mat[i][j].x = mat[i][j-1].x + inimigo.width + inimigo.width/2 
                mat[i][j].y = mat[i][j-1].y
            
# Aplica a movimentação do inimigo
def movimento_inimigo(mat:List[List[sprite.Sprite]]):
    if settings.mat_inimigo:
        inimigo = sprite.Sprite("assets/inimigo.png")
        for i in mat:
            for j in i:
                j.x += settings.velocidade_movimento_inimigo * settings.dificuldade/2
            
        if mat[0][-1].x + inimigo.width >= settings.tela.width or mat[0][-1].x + settings.velocidade_movimento_inimigo > settings.tela.width and settings.velocidade_movimento_inimigo>0:
            for a in mat:
                for b in a:
                    b.y += inimigo.height
            settings.velocidade_movimento_inimigo *= -1
            if mat[0][-1].x + settings.velocidade_movimento_inimigo > settings.tela.width:
                for i in mat:
                    for j in i:
                        j.x += settings.tela.width + settings.velocidade_movimento_inimigo - mat[0][-1]
        elif mat[0][0].x <= settings.   tela.width/11 and settings.velocidade_movimento_inimigo < 0:
            settings.velocidade_movimento_inimigo *= -1
            for a in mat:
                for b in a:
                    b.y += inimigo.height
            for a in mat:
                for b in a:
                    b.y += inimigo.height
        settings.tempo_atual_inimigo = 0
        
            
def tiro_inimigo(mat:List[List[sprite.Sprite]]):
    if settings.mat_inimigo:
        escolido = inimigo_aleatorio()
        settings.tempo_atual_recarga_inimigo += settings.tela.delta_time()
        if settings.tempo_atual_recarga_inimigo >= settings.tempo_recarga_inimigo:
            tiro = sprite.Sprite("assets/disparo.png")
            tiro.x = escolido.x + escolido.width / 2 - tiro.width / 2
            tiro.y = escolido.y + escolido.height
            settings.tot_tiro_inimigo.append(tiro)
            settings.tempo_atual_recarga_inimigo = 0

        for c in settings.tot_tiro_inimigo:
            c.draw()
        for d in settings.tot_tiro_inimigo:
            d.y += 2000 * settings.tela.delta_time()
            if d.y >= settings.tela.height + d.height:
                settings.tot_tiro_inimigo.remove(d)

def inimigo_aleatorio():
    if settings.mat_inimigo:
        return choice(choice(settings.mat_inimigo))


def inimigos_vivos():
    lista = []
    for c in settings.mat_inimigo:
        for d in c:
            lista.append(d)



# Desenha o inimigo
def desenha_inimigo():
    for i in settings.mat_inimigo:
        for j in i:
            j.draw()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=