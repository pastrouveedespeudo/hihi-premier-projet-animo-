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
        for i in a[1]:
            if i == []:
                pass
            else:
                if len(a[1][c]) > 10:
                    for i in a[1][c]:
                        im[i[0], i[1]] = 0,0,255
                        
                    print("rangée :", c)
                    
                
                c+=1

        #cv2.imshow("image.jpg", im)
        cv2.imwrite("recup.jpg", im)


        
        im_recup = cv2.imread("recup.jpg")
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if im[x,y][0] == 255 and im[x,y][1] != 255 and im[x,y][2] != 255:
                    im[x,y] = 0,0,0

        
        cv2.imshow("image.jpg", im_recup)
        cv2.imwrite("recup2.png", im)
        shutil.move("recup2.png", r"C:\Users\jeanbaptiste\coatis")



    def obtenir_pts_blanc(self):

        os.chdir(r"C:\Users\jeanbaptiste\coatis")
        im = cv2.imread("recup2.png")
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                try:
                    if im[x+1,y].all() == np.array([0,0,255]).all() and\
                        im[x+1,y].all() == np.array([0,0,255]).all():
                        pass
                    else:
                        im[x,y] = 0,0,0
                except:
                    pass
        cv2.imwrite("recup2.jpg", im)

if __name__ == "__main__":
    

    yo = yo()

    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()



    pos_im=yo.recup_pixel(liste_dossier[0])
    yo.grigri(pos_im,liste_dossier[0])
    yo.obtenir_pts_blanc()


#bon a la base je voulais ca mais je comprend pas comment ca se fait qu'il est 4 petit pts blanc au milieu voir si ca marche
#avec toutes les images... et pk y'a des pts blanc qu ireste


































        










