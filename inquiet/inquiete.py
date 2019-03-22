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

        if parcours_im != []:
            return parcours_im, True
        return parcours_im


    def pts_blanc2(self, image):
        self.image = image

        img = cv2.imread("bbb.png")
                    
        parcours_im = [(x,y) for x in range(img.shape[0]-3) for y in range(img.shape[1]-3)\
                       if img[x,y].all() == np.array([255,255,255]).all() and\
                       img[x+1,y].all() == np.array([255,255,255]).all() and\
                       img[x+1,y+1].all() == np.array([255,255,255]).all() and\
                       img[x+1,y+2].all() == np.array([255,255,255]).all() and\
                       img[x+1,y+3].all() == np.array([255,255,255]).all()]
        
        print(parcours_im)
        
 
        if parcours_im != []:
            return parcours_im, True
        
        return parcours_im



    def pos_bout_de_queue(self, size_im, temps1, temps2):
        self.size_im = size_im
        self.temps1 = temps1
        self.temps2 = temps2

        moitié = int(round(self.size_im[2] / 2))#ou math.ceil() mais 5.1 -> 6

        if self.temps1[0] or self.temps2[0] < moitié and\
           moitié > self.temps1[0] or self.temps2[0]:
            return True
        else:
            return False
        #le L a changé de place
   
    def pos_droite(self):
        pass












    def dessin(self, pts, save):
        self.pts = pts
        self.save = save

        img = cv2.imread("traitement_image2.png")

        x = 26
        y = 96

        img[x,y] = 0,0,255
        img[x+1,y] = 0,0,255
        img[x+2,y] = 0,0,255
        img[x+2,y+1] = 0,0,255
        img[x+2,y-2] = 0,0,255
        img[x+2,y-3] = 0,0,255
        cv2.imwrite(self.save, img)

        
    def dessin2(self, pts, save):
        self.pts = pts
        self.save = save

        img = cv2.imread("traitement_image2.png")
        x = 27
        y=86
        img[x,y] = 0,0,255
        img[x+1,y] = 0,0,255
        img[x+1,y+1] = 0,0,255
        img[x+1,y+2] = 0,0,255
        img[x+1,y+3] = 0,0,255
        
        img[x+1,y+3:y+30] = 0,0,255



        cv2.imwrite(self.save, img)









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
    notre_pts1 = pts.pts_blanc(IMG_EDGE)
    notre_pts2 = pts.pts_blanc2(IMG_EDGE2)
    



    queue_a_changé_de_pos = pts.pos_bout_de_queue(hauteur_largeur,notre_pts1[0], notre_pts2[0])








    #pts.dessin(notre_pts1,"traitement_image1.png")
    #pts.dessin2(notre_pts1,"traitement_image1.png")





    #if notre_pts1[1] and notre_pts2[1]  and queue_a_changé_de_pos == True:
    
    #and ya une droite aux deux qui dont de par et dotre
    #du centre de limage
     #    print("lanimal est inquiet !")



#faut imaginer que c en vrai:
    #du coup en vrai ben c une boucle du coup c par fonction/fonction





















