import os
import cv2
import time
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageChops

#--GARDE TOUT LE PLUS EN GROS FAUT GENERALISER sinon pour la suite ca marchera pas
#tenserflow, hiroku me nique ma journée c fdp ? c enculé veulent pas sinstaller ben jvai faire moi meme
#mon reseau dossier neuronal mais pas avant davoir pris un encas

class image:

    def transformation(self, path, path_direction):
        self.path = path
        self.path_direction = path_direction
        
        os.chdir(self.path)
        path_direction = self.path_direction

        liste = os.listdir()

        c = 0
        for i in liste:

            img = cv2.imread(i)

            imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(imgray,127,255,0)
            im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            gray = cv2.bilateralFilter(im2, 11, 17, 17)
            edged = cv2.Canny(gray, 30, 200)


            y = 0
            x = 0
            w = edged.shape[0]
            h = int(round(edged.shape[1] / 100*30))

            crop_img = edged[y:y+h, x:x+w]
            

            nom_image = str(c)
            cv2.imwrite(nom_image + ".jpg", crop_img)
            shutil.move(nom_image + ".jpg", self.path_direction)
            
            c+=1

    
    def selection_queue(self, path, path_direction):

        self.path = path
        self.path_direction = path_direction



        os.chdir(self.path)
        liste = os.listdir()

        c = 0
        for i in liste:

            img = cv2.imread(i)

            y = 0
            x = 0
            w = img.shape[0]
            h = int(round(img.shape[1] / 100*30))

            crop_img = img[y:y+h, x:x+w]
            

            nom_image = str(c)
            cv2.imwrite(nom_image + ".jpg", crop_img)
            shutil.move(nom_image + ".jpg", self.path_direction)

            c+=1



    def recup_pixel(self, image):

        im = cv2.imread(image)

        occurence = []
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if im[x,y].all() == np.array([255,255,255]).all():
                   
                    occurence.append((x,y))


        return occurence



    #edged




if __name__ == "__main__":

    image = image()

    image.transformation(r"C:\Users\jeanbaptiste\coatis\images",
                         r"C:\Users\jeanbaptiste\coatis\edge1")

    
    image.selection_queue(r"C:\Users\jeanbaptiste\coatis\images",
                          r"C:\Users\jeanbaptiste\coatis\couleur1")
    


    os.chdir(r"C:\Users\jeanbaptiste\coatis\edge1")
    liste_dossier = os.listdir()

    liste_position = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                      [],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    c = 0
    for i in liste_dossier:
        pos_im = image.recup_pixel(i)
        liste_position[c].append(pos_im)

        c+=1
        
    

    for i in liste_position:
        if i == []:
            pass
        else:
            print(liste_position)


    #okokok pleins de dossier de chat
            #un chat, si y'a un ensemble de meme pixel on laisse
            #sinon on efface
    #faut creer des dossier auto de egede 
 
































    

