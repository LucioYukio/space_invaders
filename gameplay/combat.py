from traitlets import List
import settings
from PPlay import sprite
import menu


def colisao_tiro(mat: List[List[sprite.Sprite]]):
    #if mat[l][0].x<= settings.tot_tiro[0].x and mat[l][c].x >= settings.tot_tiro[0].x and settings.tot_tiro[0].y:
        for a in range(len(mat)):
            for d in range(len(mat[a]))   :
                if len(settings.tot_tiro_player) > 0:
                    if mat[a][d].collided(settings.tot_tiro_player[0]):
                        settings.atingiu_inimigo = True
                        mata_inimigo(mat, a, d)
                        return
def mata_inimigo(mat:List[List[sprite.Sprite]],a, d):
    if settings.atingiu_inimigo:
        settings.tot_tiro_player.remove(settings.tot_tiro_player[0])
        mat[a].pop(d)
        calc_pontos()
        if not mat[a]:
            mat.remove(mat[a])
        if not mat:
            prox_fase()
            return
        settings.atingiu_inimigo = False

def prox_fase():
    print(settings.agravante)
    menu.set_game()


def calc_pontos():
    settings.pontos += (5 * settings.dificuldade)


def dano_player():
    if not settings.invencievel:
        for c in settings.tot_tiro_inimigo:
            if c.collided(settings.nave):
                settings.vida-=1
                if settings.vida==0:
                    settings.variavel_de_estado = "menu"
                    menu.adicionar_rank()
                settings.nave.x = settings.tela.width/2
                settings.invencievel = True
                settings.agora_cooldown_imortal += settings.tela.delta_time()