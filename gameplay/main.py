from combat import colisao_tiro
from combat import dano_player
from player import *
from enemy import  *
from settings import *
import settings
from menu import *
cont = agora = 0
tempo = 1
estado = True
#matriz_inimigo(settings.mat_inimigo, 3, 5)
fps_cont = agora = 0
set_game()
while True:
    settings.e_imortal_agora += settings.tela.delta_time()
    if settings.e_imortal_agora >= settings.e_imortal:
        estado = not estado
        settings.e_imortal_agora = 0



    fps_cont += 1
    agora += settings.tela.delta_time()
 #   if agora != 0 and fps_cont != 0:
        #print(1/(agora/fps_cont))

    tela.set_background_color("black")
    posicao_botao()
    sair()

    if variavel_de_estado == "menu":
        seleciona()
        desenha_botao()

    if settings.variavel_de_estado == "jogo":
        fundo.draw()
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
        colisao_tiro(settings.mat_inimigo, 3, 5)
    elif settings.variavel_de_estado == "dificuldade":
        tela.set_background_color("black")

        tela_dificuldade()

    settings.tela.update()
