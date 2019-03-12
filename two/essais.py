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
    
    liste_position = [[],[]]


    yo = yo()
   
    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()



        
    pos_im=yo.recup_pixel(liste_dossier[0])
    liste_position.append(pos_im)
       
    pos_im=yo.recup_pixel(liste_dossier[1])
    liste_position.append(pos_im)
    

    print(liste_position[-1])
    print(liste_position[-2])


    com = 0
    for i in liste_position[-1]:
        com+=1

    print(com)
    oyé = 0
    c=0
    while oyé < com:
        for i in liste_position[-1]:
      
            #print("(", liste_position[-1][c][0], liste_position[-1][c][1], ")",  i[0], i[1])
            pass

        c+=1

    oyé +=1
    print(oyé)



#trouve un autre truk c trop long


#ok c impossible c tj pas fini alors pour 25 images c mort, bon ben chai pas









