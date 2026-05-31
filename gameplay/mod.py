from typing import List

import PPlay.mouse as m
from PPlay import keyboard
import amb
from PPlay import  sprite




#-----MENU-----
# Posicionamento dos botoes
def posicao_botao():

    metadex, metadey  = (amb.tela.width/2)-(amb.botao_start.width/2), amb.tela.height/3-amb.botao_start.height/2
    amb.botao_start.set_position(metadex, metadey)
    amb.botao_dificuldade.set_position(metadex, metadey+amb.botao_start.height+10)
    amb.botao_rank.set_position(metadex, amb.botao_dificuldade.y+50)
    amb.botao_sair.set_position(metadex, amb.botao_rank.y+50)
        
    amb.botao_facil.set_position(metadex, metadey)
    amb.botao_medio.set_position(metadex, amb.botao_dificuldade.y+50)
    amb.botao_dificil.set_position(metadex, amb.botao_rank.y+100)

# Desenha os botoes
def desenha_botao():
    amb.botao_start.draw()
    amb.botao_dificuldade.draw()
    amb.botao_rank.draw()
    amb.botao_sair.draw()
# Confere se o usurário quer sair 
def sair():
    teclado = keyboard.Keyboard()
    if teclado.key_pressed("esc"):
        amb.variavel_de_estado = "menu"

# Analisa em qual botao o usuario clicou no menu
def seleciona():
    global mouse, dificuldade
    mouse_anterior = False
    mouse_atual = m.Mouse().is_button_pressed(1)
    cliclou_agora = mouse_atual and not mouse_anterior
    teclado = keyboard.Keyboard()
    if m.Mouse().is_over_object(amb.botao_start):
        if m.Mouse().is_button_pressed(1):
            amb.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(amb.botao_dificuldade):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            amb.variavel_de_estado = "dificuldade"


    if m.Mouse().is_over_object(amb.botao_rank):
        if m.Mouse().is_button_pressed(1)and cliclou_agora:
            pass
    if m.Mouse().is_over_object(amb.botao_sair):
        if m.Mouse().is_button_pressed(1)and cliclou_agora:
            exit()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#-----TELA DIFICULDADE-----
def tela_dificuldade():
# Analisa em qual botao o usuario clicou e aplica a dificuldade selecionada
    if m.Mouse().is_over_object(amb.botao_facil):
        if m.Mouse().is_button_pressed(1):
            amb.dificuldade = 1
            amb.tempo_recarga = amb.dificuldade
            amb.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(amb.botao_medio):
        if m.Mouse().is_button_pressed(1):
            amb.dificuldade = 2
            print(amb.dificuldade)
            amb.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(amb.botao_dificil):
        if m.Mouse().is_button_pressed(1):
            amb.dificuldade = 3
            amb.variavel_de_estado = "jogo"
    amb.tempo_recarga = amb.dificuldade
# Desenha os botoes de dificuldade
    amb.botao_facil.draw()
    amb.botao_medio.draw()
    amb.botao_dificil.draw()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#-----NAVE-----
def movimento_nave():
    if amb.teclado.key_pressed("a") or amb.teclado.key_pressed("left") and amb.nave.x>=0:
        amb.nave.x -= (400 / amb.dificuldade) * amb.tela.delta_time()
    elif amb.teclado.key_pressed("d") or amb.teclado.key_pressed("right") and amb.nave.x+amb.nave.width<amb.tela.width:
        amb.nave.x += (400 / amb.dificuldade) * amb.tela.delta_time()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#-----DISPARO-----
def disparo():

    amb.tempo_atual += amb.tela.delta_time()
    if amb.teclado.key_pressed("space") and amb.tempo_atual>=amb.tempo_recarga:
        print(amb.tempo_recarga)
        tiro = sprite.Sprite("assets/disparo.png")
        tiro.x = amb.nave.x+amb.nave.width/2-tiro.width/2
        tiro.y = amb.nave.y
        amb.tot_tiro.append(tiro)
        print("TIRO")
        amb.tempo_atual = 0
        print(len(amb.tot_tiro), amb.tempo_recarga)

    for c in amb.tot_tiro:
        c.draw()
    for d in amb.tot_tiro:
        d.y -= 3000*amb.tela.delta_time()
        if d.y<=0:
            amb.tot_tiro.remove(d)


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
                 mat[i][j].x = amb.tela.width/4 
                 mat[i][j].y = 0 
            elif j==0:
                mat[i][j].x = mat[i-1][j].x 
                mat[i][j].y = mat[i-1][j].y + inimigo.height + inimigo.height/2 
            else:
                mat[i][j].x = mat[i][j-1].x + inimigo.width + inimigo.width/2 
                mat[i][j].y = mat[i][j-1].y
        

# Aplica a movimentação do inimigo
def movimento_inimigo(mat:List[List[sprite.Sprite]]):
    amb.tempo_atual_inimigo += amb.tela.delta_time()
    if amb.tempo_atual_inimigo>=amb.movimentacao_inimigo:
        for i in mat:
            for j in i:
                j.x += 100
        amb.tempo_atual_inimigo = 0

# Desenha o inimigo
def desenha_inimigo():
    for i in amb.mat_inimigo:
        for j in i:
            j.draw()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=