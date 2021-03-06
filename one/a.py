import cv2
from PIL import Image, ImageDraw, ImageChops
from matplotlib import pyplot as plt
import numpy as np
import os

class cam_cadre:
    pass


class image:

    def noir_blanc(self, image):#on change la taille de l'image ! et noir et blanc
        self.image = image

        img = Image.open(self.image).convert("LA")
        img = img.resize((100,100))
        img.save("noir_blanc.png")
        
        return "noir_blanc.png"



    def ouverture(self, image):
        self.image = image

        img = cv2.imread(self.image)
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        gray = cv2.bilateralFilter(im2, 11, 17, 17)
        edged = cv2.Canny(gray, 30, 200)
        
        cv2.imwrite("edged.jpg", edged)

        return "edged.jpg"



    def recadrage_haut_queue(self, image):
        self.image = image
       
        img = cv2.imread(self.image)

        y = 0
        x = 0
        w = img.shape[0]
        h = int(round(img.shape[1] / 100*30))

        crop_img = img[y:y+h, x:x+w]
        
        cv2.imshow("queue.jpg", crop_img)
        cv2.imwrite("edged.jpg", crop_img)



    def crop_image_couleur(self, image):
        self.image = image
        
        img = cv2.imread(self.image)

        y = 0
        x = 0
        w = img.shape[0]
        h = int(round(img.shape[1] / 100*30))

        crop_img = img[y:y+h, x:x+w]
        
        cv2.imshow("queue.jpg", crop_img)
        cv2.imwrite("crop_couleur.jpg", crop_img)

        return "crop_couleur.jpg"




    def pts_queue(self, edge):
        self.edge = edge

        img1 = cv2.imread("edged.jpg")
  
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):
                
                try:
                    a = img1[x,y] 

                    b = img1[x-1,y] 
                    c = img1[x-2,y] 

                    d = img1[x-3,y+1] 
                    
                    e = img1[x-4,y+2]
                    f = img1[x-4,y+3] 
                    g = img1[x-4,y+4]
                    h = img1[x-3,y+4]
                    i = img1[x-2,y+5] 

                    j = img1[x-4,y+4] 
                    
                    k = img1[x-3,y+4]
                    
                    l = img1[x-1,y+5] 
                    m = img1[x,y+5]

                    n = img1[x+1,y+5] 
                    o = img1[x+2,y+5]
                    p = img1[x+3,y+5] 
                    q = img1[x+4,y+5]
                    r = img1[x+5,y+5] 
                    s = img1[x+6,y+5]
                    t = img1[x+7,y+5]
                                        
                except:
                    pass
                    #pts trop loin

                if a.all() == np.array([255,255,255]).all() and\
                   b.all() == np.array([255,255,255]).all() and\
                   c.all() == np.array([255,255,255]).all() and\
                   d.all() == np.array([255,255,255]).all() and\
                   e.all() == np.array([255,255,255]).all() and\
                   f.all() == np.array([255,255,255]).all() and\
                   g.all() == np.array([255,255,255]).all() and\
                   h.all() == np.array([255,255,255]).all() and\
                   i.all() == np.array([255,255,255]).all() and\
                   j.all() == np.array([255,255,255]).all() and\
                   k.all() == np.array([255,255,255]).all() and\
                   l.all() == np.array([255,255,255]).all() and\
                   m.all() == np.array([255,255,255]).all() and\
                   n.all() == np.array([255,255,255]).all() and\
                   o.all() == np.array([255,255,255]).all() and\
                   p.all() == np.array([255,255,255]).all() and\
                   q.all() == np.array([255,255,255]).all() and\
                   r.all() == np.array([255,255,255]).all() and\
                   s.all() == np.array([255,255,255]).all() and\
                   t.all() == np.array([255,255,255]).all():
                    print("oui")

                    
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):              
 
                try:
                
                    a = img1[x,y]
                    b = img1[x-1,y] 

                    c = img1[x-2,y+1] 

                    d = img1[x-2,y+2] 
                    e = img1[x-2,y+3]  

                    f = img1[x-1,y+3]  
                    g = img1[x,y+3]  
                    h = img1[x+1,y+3] 


                    m = img1[x+2,y+4] 
                    n = img1[x+2,y+5] 
                    o = img1[x+1,y+5] 

                    p = img1[x+3,y-3] 

                    q = img1[x+2,y-2] 
                    r = img1[x+2,y-1] 
                    s = img1[x+1,y-1]
                    
                except:
                    pass
           
                        
                if a.all() == np.array([255,255,255]).all() and\
                   b.all() == np.array([255,255,255]).all() and\
                   c.all() == np.array([255,255,255]).all() and\
                   d.all() == np.array([255,255,255]).all() and\
                   e.all() == np.array([255,255,255]).all() and\
                   f.all() == np.array([255,255,255]).all() and\
                   g.all() == np.array([255,255,255]).all() and\
                   h.all() == np.array([255,255,255]).all() and\
                   m.all() == np.array([255,255,255]).all() and\
                   n.all() == np.array([255,255,255]).all() and\
                   o.all() == np.array([255,255,255]).all() and\
                   q.all() == np.array([255,255,255]).all() and\
                   r.all() == np.array([255,255,255]).all() and\
                   s.all() == np.array([255,255,255]).all():
                    print("ouais")
                            

        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):
                try:
                                

                    a = img1[x,y] 
                    b = img1[x-1,y+1]  

                    c = img1[x-1,y+2]  
                    d = img1[x-1,y+3]  

                    e = img1[x,y+4]  

                    f = img1[x+1,y+4] 
                    g = img1[x+2,y+4] 
                     
                    h = img1[x+1,y-1]
                    i = img1[x+1,y-2]
                    j = img1[x+3,y+4] 
                    k = img1[x+4,y+4] 
                    l = img1[x+5,y+4] 
                    m = img1[x+6,y+4] 

                except:
                    pass

                if a.all() == np.array([255,255,255]).all() and\
                   b.all() == np.array([255,255,255]).all() and\
                   c.all() == np.array([255,255,255]).all() and\
                   d.all() == np.array([255,255,255]).all() and\
                   e.all() == np.array([255,255,255]).all() and\
                   f.all() == np.array([255,255,255]).all() and\
                   g.all() == np.array([255,255,255]).all() and\
                   h.all() == np.array([255,255,255]).all() and\
                   i.all() == np.array([255,255,255]).all() and\
                   j.all() == np.array([255,255,255]).all() and\
                   k.all() == np.array([255,255,255]).all() and\
                   l.all() == np.array([255,255,255]).all() and\
                   m.all() == np.array([255,255,255]).all():
                    print("ouaisouais")

                    
        for x in range(img1.shape[0]):
            for y in range(img1.shape[1]):

                try:
                    a = img1[x,y] 
                    b = img1[x+1,y] 

                    c = img1[x+1,y-1]
                    d = img1[x+2,y-1] 


                    e = img1[x-1,y+1] 
                    f = img1[x-2,y+1] 

                    g = img1[x-3,y+2] 

                    h = img1[x-4,y+3] 
                    i = img1[x-4,y+4]
                    j = img1[x-4,y+5] 

                    k = img1[x-5,y+5]
                    l = img1[x-5,y+6] 
                    m = img1[x-5,y+7]

                    n = img1[x-4,y+7] 


                    o = img1[x-4,y+8] 
                    p = img1[x-3,y+9]
                    q = img1[x-2,y+9]


                    r = img1[x-3,y+9] 

                    s = img1[x-1,y+10]

                    t = img1[x,y+10] 
                    u = img1[x+1,y+10] 
                    v = img1[x+2,y+10] 
                    w = img1[x+3,y+10]

                except:
                    pass


                if a.all() == np.array([255,255,255]).all() and\
                   b.all() == np.array([255,255,255]).all() and\
                   c.all() == np.array([255,255,255]).all() and\
                   d.all() == np.array([255,255,255]).all() and\
                   e.all() == np.array([255,255,255]).all() and\
                   f.all() == np.array([255,255,255]).all() and\
                   g.all() == np.array([255,255,255]).all() and\
                   h.all() == np.array([255,255,255]).all() and\
                   i.all() == np.array([255,255,255]).all() and\
                   j.all() == np.array([255,255,255]).all() and\
                   k.all() == np.array([255,255,255]).all() and\
                   l.all() == np.array([255,255,255]).all() and\
                   m.all() == np.array([255,255,255]).all() and\
                   n.all() == np.array([255,255,255]).all() and\
                   o.all() == np.array([255,255,255]).all() and\
                   p.all() == np.array([255,255,255]).all() and\
                   q.all() == np.array([255,255,255]).all() and\
                   r.all() == np.array([255,255,255]).all() and\
                   s.all() == np.array([255,255,255]).all() and\
                   t.all() == np.array([255,255,255]).all() and\
                   u.all() == np.array([255,255,255]).all() and\
                   v.all() == np.array([255,255,255]).all() and\
                   w.all() == np.array([255,255,255]).all():
                    print("mouaismouais")











        
    def matches_toutes_images(self, image):
        self.image = image

        os.chdir(r"C:\Users\jeanbaptiste\coatis\queue_compa")
        liste = os.listdir()

        for i in liste:
            print(i)
        
 
            img1 = cv2.imread(self.image)
            img2 = cv2.imread(i)

            
            orb = cv2.ORB_create()
            
            kp1, des1 = orb.detectAndCompute(img1,None)
            kp2, des2 = orb.detectAndCompute(img2,None)
        
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
           
            matches = bf.match(des1,des2)
         
            matches = sorted(matches, key = lambda x:x.distance)

         
            #img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:500],100, flags=2)
            
            #plt.imshow(img3),plt.show()
         
            c = 0
            for match in matches:
                c+=1
            print(c)

     
        














if __name__ == "__main__":


    notre_image = "queue pts interro3.jpg"



    image = image()
    
    image_gris = image.noir_blanc(notre_image)
    edge = image.ouverture(image_gris)
    
    queue = image.recadrage_haut_queue(edge)

    
    crop_couleur = image.crop_image_couleur(notre_image)
    

    image.pts_queue(edge)



    image_ref = "crop_couleur.jpg"
    image.matches_toutes_images(image_ref)












