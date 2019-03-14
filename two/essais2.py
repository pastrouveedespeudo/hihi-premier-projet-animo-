import os
import cv2
import time
import shutil
from conteneur_de_liste import *
import numpy as np
from PIL import Image, ImageDraw, ImageChops
import time
from collections import Counter

class essais2:

    def droite(self, path, image):
        liste = conteneur.conteneur(self)
        self.image = image
        self.path = path

        #os.chdir(self.path)
        #liste = os.listdir()

        #for i in liste:

        im = cv2.imread(self.image)


        c=0
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
     
                if im[x,y][0] == 255 and\
                   im[x,y][1] == 255 and\
                   im[x,y][2] == 255:
                    liste[1][c].append((x,y))
            c+=1

        print(liste[1])
        return liste[1]

    def liste(self, liste):
        liste_x = conteneur.conteneur(self)

        liste_y = []
   
        
        for i in liste:
            if i == []:
                pass
            else:
                for j in i:  
                    liste_y.append(j[1])

        counter = dict(Counter(liste_y))


        compteur = 0
        for cle, valeur in counter.items():
            if valeur > 4:
                liste_x[2][compteur].append(cle)
                compteur +=1


        return liste_x[2]

        
    def traitement_liste(self, liste, liste2, image):
        liste_x = conteneur.conteneur(self)
        self.image = image
        
        im = cv2.imread(self.image)
        self.liste2 = liste2
        self.liste = liste

        c = 0
        for i in self.liste:
            if i == []:
                pass
            else:
                print(i[0])

        c1=0
        for i in self.liste2:
            for j in i:
                for k in self.liste:
                    if k == []:
                        pass
                    else:
                        if j[1] == k[0]:
                            liste_x[3][c1].append(j)
                            c1+=1

        print(liste_x[3])










##
##
##                print("c'est rangées possèdent une droite")
##                print(liste2[i[0]])
##                for pix in liste2[i[0]]:
##                    print("nous dessinons :", pix)
##                    print(pix[0])
##                    im[pix[0], pix[1]] = 0,0,255
##                    
##
##            c+=1
##
##        im[10,10] = 255,0,255
##        im[13,10] = 255,0,255
##        im[16,10] = 255,0,255
##        im[19,10] = 255,0,255
##        im[21,10] = 255,0,255
##        cv2.imwrite("coucou.png", im)
##








if __name__ == "__main__":


    path1 = r"C:\Users\jeanbaptiste\coatis\edge1"


    image = "1.jpg"

    essais2 = essais2()
    liste = essais2.droite(path1, image)
    liste2 = essais2.liste(liste)
    essais2.traitement_liste(liste2, liste, image)





