from combat import *
from player import *
from settings import *
from menu import *
import pygame
cont = agora = 0
tempo = 1
estado = True
#matriz_inimigo(settings.mat_inimigo, 3, 5)
fps_cont = agora = 0
while True:



    settings.e_imortal_agora += settings.tela.delta_time()
    if settings.e_imortal_agora >= settings.e_imortal:
        estado = not estado
        settings.e_imortal_agora = 0


    posicao_botao()
    sair()
    if settings.variavel_de_estado == "menu":
        tela.set_background_color("black")
        seleciona()
        desenha_botao()


    if settings.variavel_de_estado == "rank":
        ler_rank()


    if settings.variavel_de_estado == "jogo":
        fundo.draw()
        fps()
        desenha_inimigo()
        tiro_inimigo(settings.mat_inimigo)
        movimento_nave()
        disparo()
        movimento_inimigo(mat_inimigo)
        
        dano_player()
        texto_vida = f"Vida: {settings.vida}"
        fonte_texto = pygame.font.SysFont("Arial",20)
        largura_texto, altura_texto = fonte_texto.size(texto_vida)
        tela.draw_text(texto_vida, tela.width/15-largura_texto-10,  altura_texto, color="white", size=20)
        linha.draw()
        if settings.invencievel:
            timer_zerado += tela.delta_time()
            if timer_zerado >= timer_1_seg:
                settings.invencievel = False
                timer_zerado = 0
            if estado:
                nave.draw()
        else:
            nave.draw()
        colisao_tiro(settings.mat_inimigo)
    elif settings.variavel_de_estado == "dificuldade":
        tela.set_background_color("black")

        tela_dificuldade()

    settings.tela.update()