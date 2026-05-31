from PPlay import keyboard
import settings
from enemy import *
from PPlay import mouse
m = mouse
#-----MENU-----
# Posicionamento dos botoes
def posicao_botao():

    metadex, metadey  = (settings.tela.width/2)-(settings.botao_start.width/2), settings.tela.height/3-settings.botao_start.height/2
    settings.botao_start.set_position(metadex, metadey)
    settings.botao_dificuldade.set_position(metadex, metadey+settings.botao_start.height+10)
    settings.botao_rank.set_position(metadex, settings.botao_dificuldade.y+50)
    settings.botao_sair.set_position(metadex, settings.botao_rank.y+50)
        
    settings.botao_facil.set_position(metadex, metadey)
    settings.botao_medio.set_position(metadex, settings.botao_dificuldade.y+50)
    settings.botao_dificil.set_position(metadex, settings.botao_rank.y+100)

# Desenha os botoes
def desenha_botao():
    settings.botao_start.draw()
    settings.botao_dificuldade.draw()
    settings.botao_rank.draw()
    settings.botao_sair.draw()
# Confere se o usurário quer sair 
def sair():
    teclado = keyboard.Keyboard()
    if teclado.key_pressed("esc"):
        settings.variavel_de_estado = "menu"

# Analisa em qual botao o usuario clicou no menu
def seleciona():
    global mouse, dificuldade
    mouse_anterior = False
    mouse_atual = m.Mouse().is_button_pressed(1)
    cliclou_agora = mouse_atual and not mouse_anterior
    teclado = keyboard.Keyboard()
    if m.Mouse().is_over_object(settings.botao_start):
        if m.Mouse().is_button_pressed(1):
            settings.variavel_de_estado = "jogo"
            set_game()
    if m.Mouse().is_over_object(settings.botao_dificuldade):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            settings.variavel_de_estado = "dificuldade"


    if m.Mouse().is_over_object(settings.botao_rank):
        if m.Mouse().is_button_pressed(1)and cliclou_agora:
            pass
    if m.Mouse().is_over_object(settings.botao_sair):
        if m.Mouse().is_button_pressed(1)and cliclou_agora:
            exit()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#-----TELA DIFICULDADE-----
def tela_dificuldade():
# Analisa em qual botao o usuario clicou e aplica a dificuldade selecionada
    if m.Mouse().is_over_object(settings.botao_facil):
        if m.Mouse().is_button_pressed(1):
            settings.dificuldade = 1
            settings.tempo_recarga = settings.dificuldade
            set_game()
            settings.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(settings.botao_medio):
        if m.Mouse().is_button_pressed(1):
            settings.dificuldade = 2
            print(settings.dificuldade)
            set_game()
            settings.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(settings.botao_dificil):
        if m.Mouse().is_button_pressed(1):
            settings.dificuldade = 3
            set_game()
            settings.variavel_de_estado = "jogo"
    settings.tempo_recarga = settings.dificuldade
# Desenha os botoes de dificuldade
    settings.botao_facil.draw()
    settings.botao_medio.draw()
    settings.botao_dificil.draw()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def set_game():
    matriz_inimigo(settings.mat_inimigo)
    settings.vida = 3
