#DISCLAIMER!: jag glömde göra ett eget repo så majoriteten av mina commits kommer att ligga med rästen av mina övningsuppgifter.





import random
gissningar = 14 #11



ord = ['Äpple', 'Grekland', 'flaggstång', 'eller']

ord2 = random.choice(ord)

ord2 = ord2.lower()

ord3 = len(ord2)

print(f"ordet innehåller {ord3}st bokstäver")
#MILSTOLPE!


while True:
    gissning = input("vill du gissa på en bokstav eller ett ord:")
    if gissning == "bokstav":
        gissning3 = input("Bokstav: ")
        if gissning3 not in ord2:
            gissningar = gissningar-1
            print(f"Boksaven finns inte i ordet. Du har {gissningar} gissningar kvar")
        else: 
            for idx,letter in enumerate(ord2):
                if letter == gissning3:
                    print(f" Bokstaven finns i ordet och ligger på plats {idx+1} ")

         #flytta upp till där gissat rätt
        if gissningar == -1:
            print("Du blev hängd!")
            break

    if gissning == "ord":
        gissning2 = input("Vilket ord: ")
        if gissning2 != ord2:
            gissningar = gissningar - 1
            print(f"Fel! du har {gissningar} gissningar kvar")
            if gissningar == 0:
                print("Du blev hängd!")
                break
        else:
            print("Du vann!")
            break
            #varför tar den bort 2 gissningar??

#MILSTOLPE





#grafik + feler+ __ _ _




#