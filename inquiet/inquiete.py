import cv2
from PIL import Image
import numpy as np

class image:

    def nb(self, image, save):

        self.save = save
        self.image = image
        
        img = Image.open(self.image).convert("LA")
        img.save(save)

    def filtre(self, image, save):
        self.save = save
        self.image = image

        img = cv2.imread(self.image)
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        gray = cv2.bilateralFilter(im2, 11, 17, 17)
        edged = cv2.Canny(gray, 30, 200)
        
        cv2.imwrite(self.save, edged)


class chercher_pts:


    def centre_image(self, image):
        self.image = image

        img = cv2.imread(self.image)
        centre_x = img.shape[0] / 2

        largeur = img.shape[0]
        hauteur = img.shape[1]

        return centre_x, largeur, hauteur

    def pts_blanc(self, image):
        self.image = image

        img = cv2.imread(self.image)

        parcours_im = [(x,y) for x in range(img.shape[0]-3) for y in range(img.shape[1]-3)\
                       if img[x,y].all() == np.array([255,255,255]).all() and\
                       img[x+1,y].all() == np.array([255,255,255]).all() and\
                       img[x+2,y].all() == np.array([255,255,255]).all() and\
                       img[x+2,y-1].all() == np.array([255,255,255]).all() and\
                       img[x+2,y-2].all() == np.array([255,255,255]).all() and\
                       img[x+2,y-3].all() == np.array([255,255,255]).all()]
        print(parcours_im)

        return parcours_im


            

    def pos_bout_de_queue(self, pts):
        self.pts = pts
        im = cv2.imread("yo.png")
        liste = []
        
        for i in liste:
      
            im[i[0], i[1]] = 0,255,255
        x=26
        y = 96
        im[x,y] = 255,0,255
        
        im[x+1,y] = 255,0,255
        
        im[x+2,y] = 255,0,255
        im[x+2,y-1] = 255,0,255
        im[x+2,y-2] = 255,0,255
        im[x+2,y-3] = 255,0,255
        cv2.imshow("yo.png", im)
        cv2.imwrite("ya.png", im)
    def pos_droite(self):
        pass

































    

if __name__ == "__main__":

    IMG = "a.jpg"
    IMG_NB = "aa.png"
    
    IMG2 = "b.jpg"
    IMG2_NB = "bb.png"

    IMG_EDGE = "aaa.png"
    IMG_EDGE2 = "bbb.png"
    
    image = image()
    
    image.nb(IMG, IMG_NB)
    image.nb(IMG2, IMG2_NB)


    image.filtre(IMG_NB, IMG_EDGE)
    image.filtre(IMG2_NB, IMG_EDGE2)


    pts = chercher_pts()
    
    hauteur_largeur = pts.centre_image(IMG_EDGE)
    notre_pts = liste_pts_blanc = pts.pts_blanc(IMG_EDGE)
    
    pts.pos_bout_de_queue(notre_pts)































