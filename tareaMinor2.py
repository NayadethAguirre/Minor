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

def gradF2(w,m): #con fi cuadrado
    F_1 = sum(4*f2(w,k)*(w[0]+(5/(k+1))*w[1]/5+np.exp(5/(k+1))) for k in range(1,m+1))
    F_2 = sum(4*(5/(k+1))*f2(w,k)*(w[0]+k*w[1]/5+np.exp(5/(k+1))) for k in range(1,m+1))
    F_3 = sum(4*f2(w,k)*(w[2]+w[3]*np.sin(5/(k+1))-np.cos(5/(k+1))) for k in range(1,m+1))
    F_4 = sum(4*np.sin(5/(k+1))*f2(w,k)*(w[2]+w[3]*np.sin(5/(k+1))-np.cos(5/(k+1))) for k in range(1,m+1))
    return np.array([F_1,F_2,F_3,F_4])


def gradf2(w,k): #con fi cuadrado
    t = 5/(k+1)
    f_1 = 4*f2(w,k)*(w[0]+t*w[1]-e**t)
    f_2 = 4*t*f2(w,k)*(w[0]+t*w[1]-e**t)
    f_3 = 4*f2(w,k)*(w[2]+w[3]*np.sin(t)-np.cos(t))
    f_4 = 4*np.sin(t)*f2(w,k)*(w[2]+w[3]*np.sin(t)-np.cos(t))
    return np.array([f_1,f_2,f_3,f_4])

def gradF22(w,m): #sin fi cuadrado
    F_1 = sum(2*(w[0]+(5/(k+1))*w[1]/5+np.exp((5/(k+1)))) for k in range(0,m))
    F_2 = sum(2*(5/(k+1))*(w[0]+(5/(k+1))*w[1]/5+np.exp((5/(k+1)))) for k in range(0,m))
    F_3 = sum(2*(w[2]+w[3]*np.sin((5/(k+1)))-np.cos((5/(k+1)))) for k in range(0,m))
    F_4 = sum(2*np.sin((5/(k+1)))*(w[2]+w[3]*np.sin((5/(k+1)))-np.cos((5/(k+1)))) for k in range(0,m))
    return np.array([F_1,F_2,F_3,F_4])

def gradf22(w,k): #sin fi cuadrado
    t = 5/(k+1)
    f_1 = 2*(w[0]+t*w[1]-e**t)
    f_2 = 2*t*(w[0]+t*w[1]-e**t)
    f_3 = 2*(w[2]+w[3]*np.sin(t)-np.cos(t))
    f_4 = 2*np.sin(t)*(w[2]+w[3]*np.sin(t)-np.cos(t))
    return np.array([f_1,f_2,f_3,f_4])

def GD(w,m,imax,tol,lr,f): #parametro f para especificar el gradiente usado
    i = 0
    err = np.linalg.norm(f(w,m))
    if err < tol:
        print("El punto ya es mínimo")
    else:
        while i < imax and tol < err:
            i = i+1
            w = w - lr*f(w,m)
            err = np.linalg.norm(f(w,m))
        print("Punto Final",w)
        print("Iteración",i)
        print("Error",err)
        return w

def SGD(w,m,imax,tol,lr,f): #parametro f para especificar el gradiente usado
    i = 0
    err=np.inf
    while i < imax and  tol < err :
        
        k = np.random.randint(0,m-1)
        err = np.linalg.norm(f(w,k))
        w = w - lr*f(w,k)
        i = i+1
    print("Punto Final",w)
    print("Iteración",i)
    print("Error",err)
    return w

#algoritmo SGD
#pregunta 2
w = np.array([0,0,0,0])
m = 500
imax = 10000
lr = 0.00001
tol = 0.0001
SGD(w,m,imax,tol,lr,f = gradf22)

#algoritmo GD sin cuadrados
#pregunta 2
w = np.array([0,0,0,0])
m = 500
imax = 10000
lr = 0.00001
tol = 0.0001
GD(w,m,imax,lr,tol, f = gradF22)
