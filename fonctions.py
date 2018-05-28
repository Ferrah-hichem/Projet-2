def gameboard(L,n,p1,p2): #fonction qui affiche la progression du jeu
    i=0
    j=0
    a=max(L)
    print("\t ",p1,end='')
    while j<=a or j<=5:
        print(".",end='')
        j=j+1
    print(" ",p2)
    while i<=n-1:
        print("\t",i+1,"|\t",end='')
        j=1
        while j<=L[i]:
            print("*",end='')
            j=j+1
        while j<=a:
            print(" ",end='')
            j=j+1
        print("\t|",L[i])
        i=i+1
def sti(b):#sti= string to int , fonction qui transforme une chaine sous la forme "n-m" tel que n est un nombre à un chiffre et m est un nombre à deux chiffre en une liste [n,m]
    a=[]
    if len(b)==3:
        a.append(int(b[0]))
        a.append(int(b[2]))
        return a
    elif len(b)==4:
        a.append(int(b[0]))
        c=int(b[2])*10+int(b[3])
        a.append(c)
        return a
    else:
        return 0

def test_sti(b):#fonction qui test la combinaison de modifications sur le nim
    i=0
    if len(b)==3:
        try:
            int(b[0])
            i=i+1
        except ValueError:
            return False
        try:
            int(b[2])
            i=i+1
        except ValueError:
            return False
        if b[1]!='-':
            return False
    elif len(b)==4:
        try:
            int(b[0])
            i=i+1
        except ValueError:
            return False
        try:
            int(b[2])
            i=i+1
        except ValueError:
            return False
        try:
            int(b[3])
            i=i+1
        except ValueError:
            return False
        if b[1]!='-':
            return False
    else:
        return False
    if i==2 or i==3:
        return True

def valid(k,NT,LT):#apres verifications de la syntaxe de la combinaison cette fonction test si les valeurs sont réelles ou pas
    if k==0:
        a=True
        print("\t\t Commande Inconnu !!! \n")
    else:
        if k[0]>NT:
            a=True
            print("\t \t Valeur de Tas inéxistant !!!\n")
        else:
            if k[1]>LT[k[0]-1] or k[1]==0:
                a=True
                print("\t \t Qte à enlever trop grande ou nulle !!! \n")
            else:
                 a=False
    while a==True:
        s=input("entrez une nouvelle valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!\t")
        j=test_sti(s)
        while j==False:
            print("\t\t Commande Inconnu !!! \n")
            s=input("entrez une nouvelle valeur du type n-m tel que n est le nombre tas et m le nombre de pierre a retirer du tas n SVP!\t")
            j=test_sti(s)
        k=sti(s)
        if k==0:
            a=True
            print("\t\t Commande Inconnu !!! \n")
        else:
            if k[0]>NT:
                a=True
                print("\t \t Valeur de Tas inéxistant !!!\n")
            else:
                if k[1]>LT[k[0]-1] or k[1]==0:
                    a=True
                    print("\t \t Qte à enlever trop grande ou nulle !!! \n")
                else:
                    a=False
    return k

def hall_of_fame():#fonction qui affiche le top 10 des meilleurs joueurs
    import pickle
    f=open('Scores','rb')
    names=pickle.load(f)
    scores=pickle.load(f)
    f.close()
    i=0
    print("-------------->TOP 10 DES MEILLEURS JOUEURS<--------------")
    while i<10 and i<len(scores):
        print("-------------->",i+1,")",names[i],".....",scores[i])
        i=i+1
    while i<10:
        print("-------------->",i+1,") (empty)")
        i=i+1

def add_player(p,s):#cette fonction permet d'ajouter un joueur et un score dans un fichier deja existant  , si le fichier n'existe pas elle va crée le fichier
    import pickle
    try:
        with open('Scores'):pass
        f=open('Scores','rb')
        names=pickle.load(f)
        scores=pickle.load(f)
        f.close()
        a=0
        j=0
        while j<len(scores):
            if scores[j]<s:
                if p==names[j]:
                    scores[j]=s
                    a=1
                    break
                else:
                    names.insert(j,p)
                    scores.insert(j,s)
                    a=1
                    break
            j=j+1
        if a==0:
            names.append(p)
            scores.append(s)
        f=open('Scores','wb')
        pickle.dump(names,f)
        pickle.dump(scores,f)
        f.close()
    except IOError:
        f=open('Scores','wb')
        pickle.dump([p],f)
        pickle.dump([s],f)
        f.close()
