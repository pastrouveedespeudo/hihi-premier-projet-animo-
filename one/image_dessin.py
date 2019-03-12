import cv2
from PIL import Image, ImageDraw, ImageChops
from matplotlib import pyplot as plt
import numpy as np



im = cv2.imread("edged.jpg")
for x in range(im.shape[0]):
    for y in range(im.shape[1]):              

        try:
        
            a = im[x,y]
            b = im[x-1,y] 

            c = im[x-2,y+1] 

            d = im[x-2,y+2] 
            e = im[x-2,y+3]  

            f = im[x-1,y+3]  
            g = im[x,y+3]  
            h = im[x+1,y+3] 


            m = im[x+2,y+4] 
            n = im[x+2,y+5] 
            o = im[x+1,y+5] 

            p = im[x+3,y-3] 

            q = im[x+2,y-2] 
            r = im[x+2,y-1] 
            s = im[x+1,y-1]
            
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







      
x=10
y=10


a = im[x,y]=0,0,255
b = im[x-1,y] =0,0,255

c = im[x-2,y+1]=0,0,255 

d = im[x-2,y+2]=0,0,255 
e = im[x-2,y+3]=0,0,255  

f = im[x-1,y+3]=0,0,255  
g = im[x,y+3]  =0,0,255
h = im[x+1,y+3] =0,0,255


m = im[x+2,y+4]=0,0,255 
n = im[x+2,y+5]=0,0,255 
o = im[x+1,y+5]=0,0,255 

p = im[x+3,y-3]=0,0,255 

q = im[x+2,y-2]=0,0,255 
r = im[x+2,y-1] =0,0,255
s = im[x+1,y-1]=0,0,255
cv2.imwrite("ta.png", im)

















