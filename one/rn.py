


queue = 0.06
patte = 0.02
miaule = 0.09
dort = 0.02
pasmimi = -0.09

while True:

    compt = 0
    aa = True
    while aa:
        e = queue + patte + miaule + dort + pasmimi
        
        if e > 1:
            print(queue,patte,miaule,dort,pasmimi)
            
            aa = False

        queue+=0.01
        patte+=0.01
        miaule +=0.01
        dort+=0.01
        pasmimi+=0.01

        


    compt += 1


    print(compt)
    print("yooooooooooooooo")
