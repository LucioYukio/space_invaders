from PPlay import window
from random import randint
from PPlay import  sprite
from PPlay.mouse import *
from PPlay import keyboard
from typing import List

variavel_de_estado = "menu"

quantidade_linhas_matriz_monstro = 0
quantidade_colunas_matriz_monstro = 0

tempo_fps = 2


tot_tiro_inimigo = []

tot_tiro_player = []
mat_inimigo : List[List[sprite.Sprite]] = []

dificuldade = 1
tempo_recarga_player = 0.25
tempo_atual_player = dificuldade-0.5

distorcao_temporal = randint(0, 30)

#dificuldade*0.5*distorcao_temporal*0.1
tempo_recarga_inimigo = 0.5
tempo_atual_recarga_inimigo = 0

movimentacao_inimigo = 1/dificuldade
tempo_atual_inimigo = 0

tela = window.Window(1200, 600)
teclado = keyboard.Keyboard()
botao_start = sprite.Sprite("assets/botoes/start.png")
botao_dificuldade = sprite.Sprite("assets/botoes/dificuldade.png")
botao_rank = sprite.Sprite("assets/botoes/rank.png")
botao_sair = sprite.Sprite("assets/botoes/sair.png")

botao_facil = sprite.Sprite("assets/botoes/facil.png")
botao_medio = sprite.Sprite("assets/botoes/medio.png")
botao_dificil = sprite.Sprite("assets/botoes/dificil.png")

nave = sprite.Sprite("assets/nave.png")
nave.set_position(tela.width/2, tela.height-nave.height-15)

linha = sprite.Sprite("assets/linha.png")

linha.set_position(tela.width/11, 0)
vida = 3

fundo = sprite.Sprite("assets/bg.png")
fundo.height, fundo.width = tela.height, tela.width
fundo.set_position(0,0)
velocidade_movimento = (400 / dificuldade) * tela.delta_time()

cooldown_imortal = 3
agora_cooldown_imortal = 3

e_imortal = 0.05
e_imortal_agora = 0.05

timer_1_seg = 1
timer_zerado = 0

velocidade_movimento_inimigo = 0.5


invencievel = False
# Um inimigo aleatório atira, o player tem 3 vidas, quando ele leva dano, pisca e fica imortal no meio da tela.
# O tempo entre os tiros é ligeramente aleatorio '