#Librerias
import numpy as np
from math import e

#Funciones
def f2(w,k):
    t = k/5
    return ((w[0] + t*w[1] - e**t)**2 + (w[2] + w[3]*np.sin(t) - np.cos(t))**2)

def F2(w,m):
    #if len(w) != 4:
    #    raise ValueError("Largo de w no es 4")
    return sum(f2(w,k)**2 for k in range(1,m+1))


#sum(f2([0,0,0,0],k)**2 for k in range(900))
#sum(f2([0,0,0,0],k)**2 for k in range(10000+1))

def gradF2(w,m):
    F_1 = sum(4*f2(w,k)*(w[0]+k*w[1]/5-e**(k/5)) for k in range(1,m+1))
    F_2 = sum(4*(k/5)*f2(w,k)*(w[0]+k*w[1]/5-e**(k/5)) for k in range(1,m+1))
    F_3 = sum(4*f2(w,k)*(w[2]+w[3]*np.sin(k/5)-np.cos(k/5)) for k in range(1,m+1))
    F_4 = sum(4*np.sin(k/5)*f2(w,k)*(w[2]+w[3]*np.sin(k/5)-np.cos(k/5)) for k in range(1,m+1))
    return [F_1,F_2,F_3,F_4]

def gradf2(w,k):
    t = k/5
    f_1 = 4*f(w,k)*(w[0]+t*w[1]-e**t)
    f_2 = 4*t*f(w,k)*(w[0]+t*w[1]-e**t)
    f_3 = -2*f(w,k)*(w[2]+w[4]*np.sin(t)-np.cos(t))
    f_4 = -4*np.sin(t)*f(w,k)*(w[2]+w[4]*np.sin(t)-np.cos(t))
    return [f_1,f_2,f_3,f_4]

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
    while i < imax and tol < err:
        i = i+1
        n1 = np.linalg.norm(gradf2(w,m))
        k = np.random.randint(1,m)
        w = w - lr*gradf2(w,k)
        n2 = np.linalg.norm(gradf2(w,m))
        err = np.abs(n1-n2)
    print("Punto Final",w)
    print("Iteración",i)
    print("Error",err)
    return w
