import copy
import matplotlib.pyplot as plt
def hilbert(t,n,m):
        #Cette fonction est la fonction d'hilbert de l'intervalle [0,1]
        #vers l'intervalle [0,1]^n
        #n et m sont des entier positifs , t est une chaine qui represente
        #un nombre binaire de longueur n*m
        #returns : array of floats
        L=[]
        G=[]
        Q=[]
        r=t
        for i in range(0,m*n,n):
            L.append(r[i:i+n])
        for i in range(m):
            j=n
            k=0
            while True:
                k=k+1
                if L[i][j-1] != L[i][-1]:
                    G.append(j)
                    break
                elif k>n:
                    G.append(n)
                    break
                else:
                    j = j - 1
        for i in range(m):
            if i==0 :
                a1 = (int(L[i][0], 2))
                Q.append([a1])
            else:
                a1 = (int(L[i][0], 2))
                a2 = (int(L[i-1][-1], 2))
                x = a1 ^ a2
                Q.append([x])
            for j in range(1,n):
                a1=(int(L[i][j], 2))
                a2=(int(L[i][j-1], 2))
                x=a1^a2
                Q[i].append(x)
        P=copy.deepcopy(Q)
        for i in range(1,m):
            if P[i][0]==0 :
                P[i][0]=1
            else :
                P[i][0]=0
            if P[i][n-G[i-1]]==0 :
                P[i][n-G[i-1]]=1
            else :
                P[i][n-G[i-1]]=0
        T=copy.deepcopy(P)
        def rotate(l, n):
            return l[-n:] + l[:-n]
        for i in range(1,m):
            x=0
            for j in range(i):
                x=G[j]-1+x
            x=x%n
            T[i]=rotate(T[i],x)
        S=copy.deepcopy(T)
        for i in range(1,m):
            for j in range(n):
                S[i][j]=(S[i-1][j])^(T[i][j])
        R = []
        for i in range(n):
            r = ""
            for j in range(m):
                r = r + str((S[j][i]))
            R.append(r)
        for i in range(len(R)):
            R[i]=parse_bin(R[i])

        return(R)
def parse_bin(s):
    #parse bin recoit comme entre un nombre binaire dans [0,1]
    #retourne la representation decimal de ce nombre
    #s:string , return:float
    temp=0
    for j in range(len(s)):
        temp=temp+(2**(-1-j))*int(s[j])
    return(temp)
    
def ap(t, n, m):
    #donne la representation binaire la plus proche
    #d'un decimale t dans [0,1] de longueur n*m
    #t : float , n,m: string , returns : string
    res = ""
    u = t
    for w in range(n * m):
        u = u * 2
        res = res + str(int(u))
        u = u - int(u)
    return (res)
X=[]
Y=[]
n=2 #dimension de la courbe 
m=5 #ordre de la courbe
nm=n*m
l=2**(nm) #nombre de points dans la courbe
for i in range(l):
    point=hilbert(ap(i/l,n,m),n,m)
    X.append(point[0])
    Y.append(point[1])
plt.plot(X,Y)
plt.show()
