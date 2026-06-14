from PPlay import sprite
import settings
from math import sqrt

#-----NAVE-----
def movimento_nave():
    velocidade = 400 / (1 + (settings.dificuldade - 1) * 0.2 + sqrt(max(0, settings.agravante - 1)) * 0.12)
    if (settings.teclado.key_pressed("a") or settings.teclado.key_pressed("left")) and settings.nave.x>=settings.linha.x+settings.linha.width:
        settings.nave.x -= velocidade * settings.tela.delta_time()
    elif (settings.teclado.key_pressed("d") or settings.teclado.key_pressed("right")) and settings.nave.x+settings.nave.width<settings.tela.width:
        settings.nave.x += velocidade * settings.tela.delta_time()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#-----DISPARO-----
def disparo():
    penalidade = (settings.dificuldade - 1) * 0.05 + sqrt(max(0, settings.agravante - 1)) * 0.015
    settings.tempo_atual_player += settings.tela.delta_time()
    if settings.teclado.key_pressed("space") and settings.tempo_atual_player >= settings.tempo_recarga_player + penalidade:
        tiro = sprite.Sprite("assets/disparo.png")
        tiro.x = settings.nave.x+settings.nave.width/2-tiro.width/2
        tiro.y = settings.nave.y
        settings.tot_tiro_player.append(tiro)
        settings.tempo_atual_player = 0

    for c in settings.tot_tiro_player:
        c.draw()
    for d in settings.tot_tiro_player[:]:
        d.y -= 3000*settings.tela.delta_time()
        if d.y+d.height<=0:
            settings.tot_tiro_player.remove(d)


