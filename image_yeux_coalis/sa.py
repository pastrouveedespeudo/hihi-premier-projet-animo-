import cv2
import os
from PIL import Image

os.chdir(r"C:\Users\jeanbaptiste\coatis\museau\yeux_image\p")
liste = os.listdir()
print(liste)

c=0
for i in liste:
    if i =="sa.py":
        pass
    else:
        im = Image.open(i).convert("LA")
        a = str(c) + ".png"
        im.save(str(a))
        c+=1
