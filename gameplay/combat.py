from traitlets import List
import settings
from PPlay import sprite


def colisao_tiro(mat: List[List[sprite.Sprite]], l, c):
    #if mat[l][0].x<= settings.tot_tiro[0].x and mat[l][c].x >= settings.tot_tiro[0].x and settings.tot_tiro[0].y:
        for c in range(len(mat)):
            for d in range(c)   :
                if len(settings.tot_tiro) > 0:

                    if mat[c][d].collided(settings.tot_tiro[0]):
                        print("colidiu")
                        settings.tot_tiro.remove(settings.tot_tiro[0])
                        mat[c].remove(mat[c][d])