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

    def bout_de_queue(self, image):
        self.image = image

        img = cv2.imread(self.image)

        parcours_im = [(x,y) for x in range(img.shape[0]) for y in range(img.shape[1])\
                       if img[x,y].all() == np.array([255,255,255]).all()]

        return parcours_im
        
    def nos_pts(self,liste):
        self.liste = liste
        print(self.liste)
        parcours_liste = [i for i in self.liste if i[0] + 1 and i[1]]

    @classmethod
    def operation(cls, entree, entree2):
        cls.entree = entree
        cls.entree2 = entree2
        a = 5
        aa = 10
        a = cls.entree + 1
        aa = cls.entree2

        bb = cc = aa
        
        b = c = d = e = f = a + 2
    
        dd = aa -1
        ee = aa -2 
        ff = aa - 3





##        if a, aa,b,bb,c,cc,d,dd,e,ee,f,ff:
##            return True
##        else:
##            return False


        f = lambda i: i + 1
        
        ff = [f(5) for i in range(2)]
        print(ff)
        
        for i in range(3):
        print(-i)
        

    def pos_bout_de_queue(self):
        pass

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
    pts.centre_image(IMG_EDGE)
    liste_pts_blanc = pts.bout_de_queue(IMG_EDGE)
    pts.nos_pts(liste_pts_blanc)
    pts.operation(1,2)
































