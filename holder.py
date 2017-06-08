import math 
import numpy as np
import time
def holder(f,a,b,Lip,alpha,epsilon):
    t=time.clock()
    k=0
    R0=[a,b]
    D0=[a,b]
    fopt0=f(D0[0])
    xopt0=a
    for i in range(1,len(D0)):
        if fopt0<f(D0[i]):
            fopt0=f(D0[i])
            xopt0=D0[i]
    list=[xopt0]
    F0=major(f,R0,Lip,alpha)
    x0=nombredor(F0,a,b)
    B0=F0(x0)
    Fopt0=B0
    if Fopt0-fopt0<epsilon :
        return(list[-1])
    else :
        L1=[[R0,B0,x0]]
    while L1!=[]:
        k=k+1
        h=0
        m=L1[0][1]
        for i in range(len(L1)):
            if m<L1[i][1]:
                m=L1[i][1]
                h=i
        # Selectionner le sous intervalle qu'est le plus probable de contenir le maximum
        part=[[L1[h][0][0],L1[h][2]],[L1[h][2],L1[h][0][1]]]
        del L1[h]
        # On divise l'intervalle de recherche active en deux sous intervalles
        for t in range(2):
            # construire F(h) sur Rh qui majore f
            Fh=major(f,part[t],Lip,alpha)
            x=nombredor(Fh,part[t][0],part[t][1])
            if f(x)>f(list[k-1]) :
                list.append(x)
            elif len(list)==k:
                list.append(list[k-1])
            else:
                list[k]=list[k-1]
            Bh=Fh(x)
            L1.append([part[t],Bh,x])
        Fopt2=L1[0][1]
        for i in range(len(L1)):
            Fopt2=max(Fopt2,L1[i][1])
        if (Fopt2-f(list[k])<epsilon) or (k>2000)  :
            print("ecart de",(Fopt2-f(list[k])))
            break
    print("run time was",(time.clock()-t))
    print(k)
    return(list[-1])
def major(f,R,Lip,alpha):
    #  cree une fonction concave qui majore la fonction f sur l'intervalle R
    low=R[0]
    up=R[1]
    F = lambda x: min(f(low)+Lip*((x-low)**(1/alpha)),f(up)+Lip*((up-x)**(1/alpha)))
    return(F)
def estimate(f,a,b,alpha,n,e):
    sample=[]
    k=0
    for i in range(n):
        x=(np.random.uniform(a,b))
        sample.append(x)
    for i in range(n):
        if (sample[i]+e)<b :
            k1=(abs(f(sample[i])-f(sample[i]+e)))/(np.power(e,alpha))
        else :
            k1=(abs(f(sample[i])-f(sample[i]-e)))/(np.power(e,alpha))
        k=max(k,k1)
        for j in range(i+1,n):
            if sample[i]!=sample[j]:
                k2=(abs(f(sample[i])-f(sample[j])))/(np.power(abs(sample[i]-sample[j]),alpha))
                k=max(k,k2)
    return(k)
