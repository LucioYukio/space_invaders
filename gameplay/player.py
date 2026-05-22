from PPlay import sprite
import settings


#-----NAVE-----
def movimento_nave():
    if settings.teclado.key_pressed("a") or settings.teclado.key_pressed("left") and settings.nave.x>=0:
        settings.nave.x -= (400 / settings.dificuldade) * settings.tela.delta_time()
    elif settings.teclado.key_pressed("d") or settings.teclado.key_pressed("right") and settings.nave.x+settings.nave.width<settings.tela.width:
        settings.nave.x += (400 / settings.dificuldade) * settings.tela.delta_time()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#-----DISPARO-----
def disparo():

    settings.tempo_atual += settings.tela.delta_time()
    if settings.teclado.key_pressed("space") and settings.tempo_atual>=settings.tempo_recarga:
        print(settings.tempo_recarga)
        tiro = sprite.Sprite("assets/disparo.png")
        tiro.x = settings.nave.x+settings.nave.width/2-tiro.width/2
        tiro.y = settings.nave.y
        settings.tot_tiro.append(tiro)
        print("TIRO")
        print(len(settings.tot_tiro))
        settings.tempo_atual = 0
        print(len(settings.tot_tiro), settings.tempo_recarga)

    for c in settings.tot_tiro:
        c.draw()
    for d in settings.tot_tiro:
        d.y -= 3000*settings.tela.delta_time()
        if d.y<=0:
            settings.tot_tiro.remove(d)


