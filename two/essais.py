import os
import cv2
import time
import shutil
from conteneur_de_liste import *
import numpy as np
from PIL import Image, ImageDraw, ImageChops




class yo :
    def recup_pixel(self, image):
        self.image = image

 
        liste = os.listdir()
        im = cv2.imread(self.image)

        occurence = []
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if im[x,y].all() == np.array([255,255,255]).all():
                   
                    occurence.append((x,y))

        im[7,104] = 255,0,255
        im[7,105] = 255,0,255
        im[7,106] = 255,0,255
        im[7,107] = 255,0,255
        cv2.imshow("ypo.jpg", im)
        return occurence






    def grigri(self, truk):
        self.truk = truk
        
        a=conteneur.conteneur(self)
                
        liste = []
        liste.append(self.truk)
        
        rangée = 0
        

        x = 0

        for i in liste[0]:
            try:
                if liste[0][x][0] != liste[0][x+1][0]:
                    rangée+=1
            
                a[1][rangée].append(i)
            except:
                pass
            finally:
                x+=1
               
            

        print(a[1][0])
        print(a[1][1])  















if __name__ == "__main__":
    



    yo = yo()
   
    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()



    pos_im=yo.recup_pixel(liste_dossier[0])
    yo.grigri(pos_im)


#soit tu prends la premier pos et ensuite tu cherches liaison par fraction

#soit tu cherches la queue cad une droite mais y'a pas toujours

#soit tu cherches le pont mais c pas tj le meme

#la queue en pont = 4 pts blanc




































        










