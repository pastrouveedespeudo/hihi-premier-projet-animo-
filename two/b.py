import os
import cv2
import time
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageChops


class yo:
    
    def selection_queue(self):
        path_direction = r"C:\Users\jeanbaptiste\coatis\match_image_coul_raoul"
        os.chdir(r"C:\Users\jeanbaptiste\coatis\images")
        liste = os.listdir()

        c = 0
        for i in liste:

            img = cv2.imread(i)

            y = 0
            x = 0
            w = img.shape[0]
            h = int(round(img.shape[1] / 100*30))

            crop_img = img[y:y+h, x:x+w]
            
            cv2.imshow("queue.jpg", crop_img)

            nom_image = str(c)
            cv2.imwrite(nom_image + ".jpg", crop_img)

            shutil.move(nom_image + ".jpg", path_direction)

            c+=1

    def ouverture(self, image, image2):

        os.chdir(r"C:\Users\jeanbaptiste\coatis\match_image_coul_raoul")

        liste = os.listdir()
        nombre_image = len(liste)

        for i in range(nombre_image):
            pass
            
        im = cv2.imread(image)
        img = cv2.imread(image2)


        occurence = []
        c = 0
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                if im[x,y].all() == np.array([255,255,255]).all()\
                   and img[x,y].all() == np.array([255,255,255]).all():
                    im[x,y] = 0,0,255
                    img[x,y] = 0,0,255

                    occurence.append((x,y))
                    c+=1

        print(c)
        cv2.imwrite("matche.jpg", im)
        cv2.imwrite("matche1.jpg", img)
        print(occurence)




if __name__ == "__main__":

    yo = yo()
    
    yo.selection_queue()
    #yo.ouverture("edged.jpg", "edged2.jpg")
    








    

