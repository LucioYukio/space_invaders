from traitlets import List
import settings
from PPlay import sprite


def colisao_tiro(mat: List[List[sprite.Sprite]], l, c):
    #if mat[l][0].x<= settings.tot_tiro[0].x and mat[l][c].x >= settings.tot_tiro[0].x and settings.tot_tiro[0].y:
        for a in range(len(mat)):
            for d in range(len(mat[a]))   :
                if len(settings.tot_tiro_player) > 0:
                    if mat[a][d].collided(settings.tot_tiro_player[0]):
                        settings.tot_tiro_player.remove(settings.tot_tiro_player[0])
                        mat[a].pop(d)
                    if not mat[a]:
                        mat.remove(mat[a])
                        return


def dano_player():
    if not settings.invencievel:
        for c in settings.tot_tiro_inimigo:
            if c.collided(settings.nave):
                settings.vida-=1
                if settings.vida==0:
                    settings.variavel_de_estado = "menu"
                settings.nave.x = settings.tela.width/2
                settings.invencievel = True
                settings.agora_cooldown_imortal += settings.tela.delta_time()
    