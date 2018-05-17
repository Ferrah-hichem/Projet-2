print("\t\t BIENVENU DANS LE JEU DE NIM , AMUSEZ VOUS BIEN ;)")
from fonctions import *
a=True
w=1
while a==True:
    if w==1:
        p1=input("Veuillez entrer le nom du joueur 1 :")
        p2=input("Veuillez entrer le nom du joueur 2 :")
    sc=0
    from random import randint
    NT=randint(3,7)
    LT=[]
    i=0
    while i<=NT-1:
        LT.append(randint(5,23))
        i=i+1
    gameboard(LT,NT,p1,p2)
    b=0
    while sum(LT)>1:
        b=b+1
        if b%2==1:
            print("\n\tTour de",p1,"\n",)
        else:
            print("\n\tTour de",p2,"\n",)
        s=input("Entrez une valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!")
        y=test_sti(s)
        while y==False:
            print("\t Commande Inconnu , Repetez sous la forme n-m  \n")
            s=input("Entrez une valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!")
            y=test_sti(s)
        k=sti(s)
        k=valid(k,NT,LT)
        LT[k[0]-1]=LT[k[0]-1]-k[1]
        gameboard(LT,NT,p1,p2)
    nbCoup1=b//2+1
    nbCoup2=b//2
    i=1
    if b%2==0:
        if sum(LT)==0:
            while i<=nbCoup1:
                sc=sc+i*(10**i)
                i=i+1
            print(p1," a gagné,avec un score de : ",sc,"BRAVO!")
            p=p1
        else:
            while i<=nbCoup2:
                sc=sc+i*(10**i)
                i=i+1
            print(p2," a gagné,avec un score de : ",sc,"BRAVO!")
            p=p2
    else:
        if sum(LT)==0:
            while i<=nbCoup2:
                sc=sc+i*(10**i)
                i=i+1
            print(p2," a gagné, avec un score de : ",sc,"BRAVO!")
            p=p2
        else:
            while i<=nbCoup1:
                sc=sc+i*(10**i)
                i=i+1
            print(p1," a gagné, avec un score de : ",sc,"BRAVO!")
            p=p1
    add_player(p,sc)
    hall_of_fame() 
    print("\n---------->Voulez vous jouer à une nouvelle partie ?<----------")
    s=input("-> Entrez la valeur '1' pour relancer le jeu ou entrez la valeur '2' pour jouer à une nouvelle manche (les noms resteront inchangé), si vous entrez une autre valeur le jeu s'arrete ")
    if s=='1':
        print("---------->Veuillez entrez les Noms des nouveaux joueurs<----------")
        a=True
        w=1
    elif s=='2':
        print("---------->Nouvelle manche est lancée<----------\n")
        a=True
        w=2
    else:
        a=False
 
