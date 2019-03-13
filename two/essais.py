import os
import cv2
import time
import shutil
from conteneur_de_liste import *
import numpy as np
from PIL import Image, ImageDraw, ImageChops
import time



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

        im[47,106] = 0,0,255
        im[47,107] = 0,0,255
        im[47,110] = 0,0,255
        im[47,127] = 0,0,255

        
        #cv2.imshow("ypo.jpg", im)
        return occurence





    def grigri(self, truk, image):
        self.truk = truk
        self.image = image
        
        a=conteneur.conteneur(self)
                
        liste = []
        liste.append(self.truk)
        
        rangée = 0
        

        x = 0

        for i in liste[0]:
            try:
                a[1][rangée].append(i)
                if liste[0][x][0] != liste[0][x+1][0]:
                    rangée+=1
            
            except:
                pass
            finally:
                x+=1
               
        im = cv2.imread(self.image)
        c = 0
        for i in a[1][24]:
            if i == []:
                pass
            else:
                print(i)
                print(len(a[1][5]))
                im[i[0], i[1]] = 0,0,255
                c+=1
        
        cv2.imshow("image.jpg", im)
        #if y est a coté on compte pas !











if __name__ == "__main__":
    



    yo = yo()

    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()



    pos_im=yo.recup_pixel(liste_dossier[0])
    yo.grigri(pos_im,liste_dossier[0])






































        










