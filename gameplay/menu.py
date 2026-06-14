from PPlay import keyboard
from enemy import *
import settings
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
    if settings.variavel_de_estado != "dificuldade":
        pass
    if m.Mouse().is_over_object(settings.botao_start):
        if m.Mouse().is_button_pressed(1):
            set_game()
            settings.variavel_de_estado = "jogo"
    if m.Mouse().is_over_object(settings.botao_dificuldade):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            settings.variavel_de_estado = "dificuldade"
    if m.Mouse().is_over_object(settings.botao_rank):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            settings.variavel_de_estado = "rank"
            print("foi aqui")
    if m.Mouse().is_over_object(settings.botao_rank):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            pass
    if m.Mouse().is_over_object(settings.botao_sair):
        if m.Mouse().is_button_pressed(1) and cliclou_agora:
            exit()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#-----TELA DIFICULDADE-----
def tela_dificuldade():
# Analisa em qual botao o usuario clicou e aplica a dificuldade selecionada
    if settings.variavel_de_estado == "dificuldade":
        if m.Mouse().is_over_object(settings.botao_facil):
            if m.Mouse().is_button_pressed(1):
                settings.dificuldade = 1
                settings.variavel_de_estado = "jogo"
                set_game()
        if m.Mouse().is_over_object(settings.botao_medio):
            if m.Mouse().is_button_pressed(1):
                settings.dificuldade = 2
                settings.variavel_de_estado = "jogo"
                set_game()
        if m.Mouse().is_over_object(settings.botao_dificil):
            if m.Mouse().is_button_pressed(1):
                settings.dificuldade = 3
                settings.variavel_de_estado = "jogo"
                set_game()
        settings.tempo_recarga = settings.dificuldade

        # Desenha os botoes de dificuldade
        settings.botao_facil.draw()
        settings.botao_medio.draw()
        settings.botao_dificil.draw()

def salvar_rank():
    lista = []
    with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, pontos = linha.strip().split(",")  # .strip() remove quebras de linha
            lista.append([nome, pontos])
    for a in lista:
        tem = False
        for b in settings.rank:
            if a == b:
                tem = True
        if not tem:
            settings.rank.append(a)

def adicionar_rank():
    salvar_rank()
    pessoa = []
    nome = str(input("Digite seu nome:"))
    pessoa.append(nome)
    pessoa.append(settings.pontos)
    settings.rank.append(pessoa)
    settings.rank.sort(key=lambda x:int(x[1]), reverse=True)

    with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
        for a in settings.rank:
            arquivo.write(f"{a[0]},{a[1]}\n")
def ler_rank():
    rank = settings.rank
    if len(settings.rank) >=4:
        rank = settings.rank[:4]
    for i in range(0,len(rank)):
        nome, pontos = rank[i]
        settings.tela.draw_text(f"{i+1} : {nome} - {pontos}", 150, 100 + i*80, size=50, color=(255,255,0))



    with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
        lista = []
        for linha in arquivo:
            nome, pontos = linha.strip().split(",")  # .strip() remove quebras de linha
            lista.append([nome, pontos])
        return lista

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def set_game():
    settings.agravante += settings.dificuldade
    settings.mat_inimigo.clear()
    matriz_inimigo(settings.mat_inimigo,settings.agravante)
    settings.vida = 3
    salvar_rank()

def fps():
    settings.cont_tempo += settings.tela.delta_time()
    settings.frames += 1

    if settings.cont_tempo >= 1:
        settings.fps_atual = settings.frames
        settings.frames = 0
        settings.cont_tempo = 0

    settings.tela.draw_text("FPS: " + str(settings.fps_atual), 30, 70, size=20, color=(255, 255, 255))
