print("\t\t BIENVENU DANS LE JEU DE NIM , AMUSEZ VOUS BIEN ;)")
from fonctions import * #on importe toutes les fonctions déja ecrit dans le fichier fonctions.py 
a=True #c'est la variable qu'on a choisi pour definir si le jeu est toujours en marche ou pas
w=1 #cette variables nous permet de savoir si c'est toujours les même joueurs qui jouent une nouvelle manche ou bien ils sont nouveaux
while a==True:
    if w==1:
        p1=input("Veuillez entrer le nom du joueur 1 :")#ajout du joueur 1
        p2=input("Veuillez entrer le nom du joueur 2 :")#ajout du joueur 1
    sc=0 #score du gagnant qui serait calculé a la fin , pour l'autre il recevera un 0
    from random import randint#import de la fonction randint qui nous fera créer des parties aléatoires
    NT=randint(3,7)#NT=Nombre de Tas aléatoire entier entre 3 et 7
    LT=[]#LT=Liste des tas
    i=0 #indice pour remplire nos tas
    while i<=NT-1:
        LT.append(randint(5,23))#remplir nos tas 1 à 1 avec un nombre de pierres entre 5 et 23
        i=i+1
    gameboard(LT,NT,p1,p2)#fonction qui affiche l'etat actuel du jeu
    b=0#variable qui permet de decider qui va jouer a chaque tour (nombre de tours total)
    while sum(LT)>1:#condition qui nous permet de savoir si le jeu n'est pas encore fini
        b=b+1
        if b%2==1:
            print("\n\tTour de",p1,"\n",) # on invite le joueur 1 a jouer
        else:
            print("\n\tTour de",p2,"\n",)#on invite le joueur 2 a jouer dans ce cas
        s=input("Entrez une valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!")
        y=test_sti(s)#on test si la combinaison entré n'est pas fausse
        while y==False:#si elle est fausse on le reinvite a joueur
            print("\t Commande Inconnu , Repetez sous la forme n-m  \n")
            s=input("Entrez une valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!")
            y=test_sti(s)#on test si la combinaison entré n'est pas fausse
        k=sti(s)#sti= string to int , fonction qui transforme une chaine sous la forme "n-m" tel que n est un nombre à un chiffre et m est un nombre à deux chiffre en une liste [n,m]
        k=valid(k,NT,LT)#ici on teste si le nombre de tas existe ou bien le nombre de pierre a retirer n'est pas superieur au nombre de pierres du tas choisi, elle invite aussi le joueur a rejouer si elle est toujour éronné 
        LT[k[0]-1]=LT[k[0]-1]-k[1]#ici on soustrait le nombre de pierres entré du nombre de tas choisi
        gameboard(LT,NT,p1,p2)#on affiche l'etat du jeu apres modifications
    nbCoup1=b//2+1#nombre de coups du jouer 1
    nbCoup2=b//2#nombre de coups du jouer 2
    i=1
    if b%2==0:#ici on test qui des deux joueurs a joué le dernier
        if sum(LT)==0:#ici on test si le jeu est terminé avec le nombre de pierres total egal à 1 ou 0
            while i<=nbCoup1:#dans ce cas la le joueur 1 a gagné on lui calcule son score
                sc=sc+i*(10**i)
                i=i+1
            print(p1," a gagné,avec un score de : ",sc,"BRAVO!")#on affiche que le joueur 1 a gagné
            p=p1#cette variable nous permet de sauvegarder le nom du joueur gagnant
        else:#les memes commentaire que le bloc précedent avec le joueur 1
            while i<=nbCoup2:
                sc=sc+i*(10**i)
                i=i+1
            print(p2," a gagné,avec un score de : ",sc,"BRAVO!")
            p=p2
    else:#les memes commentaires des 2 blocs précedent sauf que c'est le contraire a chaque cas
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
    add_player(p,sc)#on ajoute le joeur gagnant  et son score dans cette partiedans un fichier (si son score est meilleur que ces précedent ou bien si c'est sa premiere partie)  
    hall_of_fame()#on affiche le top 10 des meilleur joueurs ayant joué à cette version du jeu
    print("\n---------->Voulez vous jouer à une nouvelle partie ?<----------")# a partir d'ici on invite les joueurs s'ils veulent rejouer
    s=input("-> Entrez la valeur '1' pour relancer le jeu ou entrez la valeur '2' pour jouer à une nouvelle manche (les noms resteront inchangé), si vous entrez une autre valeur le jeu s'arrete ")
    if s=='1':#si la nouvelle partie concerne d'autres joueurs
        print("---------->Veuillez entrez les Noms des nouveaux joueurs<----------")
        a=True
        w=1
    elif s=='2':#si la nouvelle partie concerne les mêmes joueurs
        print("---------->Nouvelle manche est lancée<----------\n")
        a=True
        w=2
    else:#si ils veulent quitter le jeu
        a=False
 
