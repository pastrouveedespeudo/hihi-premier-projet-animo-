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


    def pts_blanc2(self, image):#faut reduire et mettre d'autre tailles  merde enfete je sais faire que crochet crochet instruction
                                #C PAS DU TOUT COMME DANS LES SOLUCES pfffffff
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




    def pos_bout_de_queue(self):
        pass

   
    def pos_droite(self):
        pass



    def dessin(self, pts, save):
        self.pts = pts
        self.save = save

        im = cv2.imread(self.save)
  
        for i in self.pts:
            x = i[0]
            y = i[1]
            try:
                im[x,y] = 255,0,255
                im[x+1,y] = 255,0,255
                im[x+2,y] = 255,0,255
                im[x+2,y-1] = 255,0,255
                im[x+2,y-2] = 255,0,255
                im[x+2,y-3] = 255,0,255

                #cv2.imwrite(self.save, im)
            except:
                print("pas de pts")


##
##       
##        
##        img[x,y] = 0,0,255
##        img[x+1,y] = 0,0,255
##        img[x+2,y] = 0,0,255
##        img[x+2,y+1] = 0,0,255
##        img[x+2,y+2] = 0,0,255
##        img[x+2,y+3] = 0,0,255























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
    
    pts.pos_bout_de_queue()


    pts.dessin(notre_pts1,"traitement_image1.png")
    pts.dessin(notre_pts2, "traitement_image2.png")

    if notre_pts1[1] and notre_pts2[1] == True: #and ya une droite aux deux qui dont de par et dotre
                                                        #du centre de limage
        print("lanimal est inquiet !")



#faut imaginer que c en vrai:
    #du coup en vrai ben c une boucle du coup c par fonction/fonction





















