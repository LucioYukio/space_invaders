from PPlay import window
from PPlay import  sprite
from PPlay.mouse import *
from PPlay import keyboard
from typing import List

variavel_de_estado = "menu"

velocidade_movimento_inimigo = 100

tot_tiro = []
mat_inimigo : List[List[sprite.Sprite]] = []

dificuldade = 1
tempo_recarga = dificuldade-0.8
tempo_atual = dificuldade-0.8


movimentacao_inimigo = 1/dificuldade
tempo_atual_inimigo = 1/dificuldade

tela = window.Window(1200, 700)
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


velocidade_movimento = (400 / dificuldade) * tela.delta_time()