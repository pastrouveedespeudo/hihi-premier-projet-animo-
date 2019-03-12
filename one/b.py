import cv2
import time
import numpy as np
from PIL import Image, ImageDraw, ImageChops


class yo:
    
    def selection_queue(image):
        pass
        

    def ouverture(image, image2):
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

    yo.ouverture("edged.jpg", "edged2.jpg")

