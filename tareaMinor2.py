#Librerias
import numpy as np
from math import e
from decimal import Decimal


#pregunta 1
#Funciones
def f2(w,k):
    t = 5/(k+1)
    return ((w[0] + t*w[1] - e**t)**2 + (w[2] + w[3]*np.sin(t) - np.cos(t))**2)

def F2(w,m):
    #if len(w) != 4:
    #    raise ValueError("Largo de w no es 4")
    return Decimal(sum(f2(w,k)**2 for k in range(1,m+1)))


#sum(f2([0,0,0,0],k)**2 for k in range(900))
#sum(f2([0,0,0,0],k)**2 for k in range(10000+1))

def gradF2(w,m):
    F_1 = sum(4*f2(w,k)*(w[0]+k*w[1]/5-e**(k/5)) for k in range(1,m+1))
    F_2 = sum(4*(k/5)*f2(w,k)*(w[0]+k*w[1]/5-e**(k/5)) for k in range(1,m+1))
    F_3 = sum(4*f2(w,k)*(w[2]+w[3]*np.sin(k/5)-np.cos(k/5)) for k in range(1,m+1))
    F_4 = sum(4*np.sin(k/5)*f2(w,k)*(w[2]+w[3]*np.sin(k/5)-np.cos(k/5)) for k in range(1,m+1))
    return np.array([F_1,F_2,F_3,F_4])

def gradf2(w,k):
    t = 5/(k+1)
    f_1 = 4*f2(w,k)*(w[0]+t*w[1]-e**t)
    f_2 = 4*t*f2(w,k)*(w[0]+t*w[1]-e**t)
    f_3 = 4*f2(w,k)*(w[2]+w[3]*np.sin(t)-np.cos(t))
    f_4 = 4*np.sin(t)*f2(w,k)*(w[2]+w[3]*np.sin(t)-np.cos(t))
    return np.array([f_1,f_2,f_3,f_4])

def GD(w,m,imax,tol,lr):
    i = 0
    err = np.linalg.norm(gradF2(w,m))
    if err < tol:
        print("El punto ya es mínimo")
    else:
        while i < imax and tol < err:
            i = i+1
            w = w - lr*gradF2(w,m)
            err = np.linalg.norm(gradF2(w,m))
        print("Punto Final",w)
        print("Iteración",i)
        print("Error",err)
        return w
    
def SGD(w,m,imax,tol,lr):
    i = 0
    err=np.inf
    while i < imax and  tol < err :
        
        k = np.random.randint(0,m-1)
        err = np.linalg.norm(gradf2(w,k))
        #gradf2(w, k)
        
        w = w - lr*gradf2(w,k)
        i = i+1
    print("Punto Final",w)
    print("Iteración",i)
    print("Error",err)
    return w

#pregunta 2
w=np.array([0,0,0,0])
#gradf2(w,1000)
m=10000
imax=1000
lr=0.000001
tol=0.01
SGD(w,m,imax,tol,lr)
#gradf2(w,m)
#np.linalg.norm(gradF2(w,m))
