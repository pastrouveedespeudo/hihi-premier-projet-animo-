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


        return occurence


if __name__ == "__main__":
    
    liste_position = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    liste_liaison = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                     [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    yo = yo()
   
    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()


    c = 0
    for i in liste_dossier:
        
        pos_im=yo.recup_pixel(i)
        liste_position[c].append(pos_im)
        c+=1

    

    x1 = 0
    y1 = 0
    liste_c = 0
    for i in liste_position:
        if i == []:
            pass
        else:
        
            liste = []

            d=0
            for j in i[0]:
        
                a = i[0][x1][0]
                b = i[0][y1][1]
             
                
                aa = a + j[0]
                bb = b + j[1]


                liste.append((aa,bb))

                d+=1
     
            liste_liaison[liste_c].append(liste)

            
            x1+=1
            y1+=1
            liste_c += 1

       

    print(liste_liaison)














