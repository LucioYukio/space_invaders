from combat import colisao_tiro
from player import *
from enemy import  *
from settings import *
from menu import *
cont = agora = 0
tempo = 1
matriz_inimigo(mat_inimigo, 3, 5)
while True:
    cont += 1
    agora+= settings.tela.delta_time()
    if agora>=tempo:
        fps = cont/settings.tela.delta_time()
        print(fps)
        cont = 0
    tela.set_background_color("black")
    posicao_botao()
    sair()

    if variavel_de_estado == "menu":
        seleciona()
        desenha_botao()

    if settings.variavel_de_estado == "jogo":
        tela.set_background_color("black")
        movimento_nave()
        disparo()
        desenha_inimigo()
        movimento_inimigo(mat_inimigo)
        nave.draw()
        colisao_tiro(mat_inimigo, 3, 5)
    elif settings.variavel_de_estado == "dificuldade":
        tela.set_background_color("black")

        tela_dificuldade()

    settings.tela.update()
