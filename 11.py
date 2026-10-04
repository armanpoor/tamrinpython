from datetime import datetime

halat = int(input("halat 1 ya 2: "))

def shartha(zaman):
    if zaman>0 and zaman<=6:
        print("Nime Shab Bekheyr!")

    elif zaman>6 and zaman<=12:
        print("Sobh Bekheyr!")
        
    elif zaman>12 and zaman<=18:
        print("Ba'ad Az Zohr Bekheyr!")
        
    elif zaman>18 and zaman<=24:
        print("Shab Bekheyr!")
    else:
        print("Sara khanoom loftn addy dar bazeye 0 ta 24 vared konid!")


if halat==1:
    zaman1 = int(input("Sara Alan Sa'at Chande: "))
    shartha(zaman1)
elif halat==2:
    now = datetime.now()
    zaman2 = now.hour
    shartha(zaman2)