#Hangman 
import os
h1="(o,o)"
h2="  |"
h3=" /| "
h4=" /|\ "
h5=" /  "
h6=" / \ "
a="___"
b="  |"
h0=a+"\n"+b
status=""
cw="___"
cw2=["_","_","_"]

print("Welcome to play hangman game")
words=["chess","tag","checkers","backgammon","dixit"]
hak=len(words[1])

while (hak>0):
    print("You have,",hak,"chance\n\n")
    print(cw.upper())
    l=input("\n Write a letter")
    word=""
    y=0
    for x in range (len(words[1])): 
        if words[1][x:x+1]==l:
            word=word+l
        else:
            word=word+"_" 
            y=y+x

    if y==len(words[1]):
        hak-=1
    if hak==3:
        status=h0
    if hak==2:
        status=h0+"\n"+h1+"\n"+h2
    if hak==1:
        status=h0+"\n"+h1+"\n"+h2+"\n"+h4
    if hak==0:
        status=h0+"\n"+h1+"\n"+h2+"\n"+h4+"\n"+h6
    
    for x in range (len(words[1])):
        if (cw[x:x+1]=="_") and (word[x:x+1]!="_"):
            cw2[x]=word[x]

    cw=cw2[0]+cw2[1]+cw2[2]
    
    
    os.system("cls")
    print(status)
    
    
    if hak==0:
        print("GAME OVER")
        print("Answer is TAG")




if (cw==cw2) and hak==0:
    print("lol")





