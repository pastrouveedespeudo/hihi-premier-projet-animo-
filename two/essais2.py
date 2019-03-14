import os
import cv2
import time
import shutil
from conteneur_de_liste import *
import numpy as np
from PIL import Image, ImageDraw, ImageChops
import time


class essais2:

    def droite(self, path):
        liste = conteneur.conteneur(self)

        self.path = path

        #os.chdir(self.path)
        #liste = os.listdir()

        #for i in liste:

        im = cv2.imread("1.jpg")


        c=0
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
     
                if im[x,y][0] == 255 and\
                   im[x,y][1] == 255 and\
                   im[x,y][2] == 255:
                    liste[1][c].append((x,y))
            c+=1


        return liste[1]

    def liste(self, liste):
        liste_x = conteneur.conteneur(self)
        
        
        c=0
        compteur = 0
        for i in liste:
            if i == []:
                pass
            else:
                nombre_x = 0
                for j in liste[c]:
                    nombre_x += 1

                if nombre_x > 4:
                    liste_x[2][compteur].append(c)
                    compteur +=1
                    
                c+=1

                
        return liste_x[2]

        
    def traitement_liste(self, liste, liste2):
        liste_x = conteneur.conteneur(self)
        
        self.liste2 = liste2
        self.liste = liste
        
        c = 0
        for i in self.liste:
            if i == []:
                pass
            else:

                print("c\est rangées possèdent une droite")
                print(liste2[i[0]])

            c+=1












if __name__ == "__main__":


    path1 = r"C:\Users\jeanbaptiste\coatis\edge1"

    essais2 = essais2()
    liste = essais2.droite(path1)
    liste2 = essais2.liste(liste)
    essais2.traitement_liste(liste2, liste)




























































