#Librerias
import numpy as np
#para usar euler
from math import e


## funcion 1
def y(k):
    Y=e**(k/10)+e**((k-1)/10)
    return Y
 # w vector de entrada w0 a w5
 # n = 6 cant de variables
 # a  parametro
def funcion(w,n,a):
  f=np.zeros(2*n)
  f[0]=w[0]-0.2
  for k in range(1,n):
      f[k]=np.sqrt(a)*(e**(w[k]/10)+e**(w[k-1]/10)-y(k))
  for k in range(n,2*n-1):
      f[k]=np.sqrt(a)*(e**(w[k-n+1]/10)-e**(-1/10))
  f11=0
  for i in range(0,n):
      f11=f11+(n-1+i+1)*w[i]
  f[11]=f11-1
  F=0
  for i in range(0,2*n):
      F=F+f[i]**2
  return F,f11
##f11 , F es la funcion escalar dentro del vector

w=np.zeros(6)
a=10**(-5)
n=6

[F,f11]=funcion(w,n,a)

#gradiente
def gradiente(w,n,a,f11):
    g=np.zeros(6)
    g[0]=2*(w[0]-0.2)+a/5*e**(w[0]/10)*(e**(w[1]/10)+e**(w[0]/10)-y(1))+2*f11*(6)*w[0]
    for k in range(1,n-1):
        g[k]=a/5*e**(w[k]/10)*(e**(w[k]/10)+e**(w[k-1]/10)-y(k))+a/5*e**(w[k]/10)*(e**(w[k+1]/10)+e**(w[k]/10)-y(k+1))+a/5*e**((w[k]-1)/10)*(e**((w[k]+1)/10)-1)+2*f11*2*(n-k)*w[k]
    g[5]=a/5*e**(w[5]/10)*(e**(w[5]/10)+e**(w[4]/10)-y(5))+a/5*e**((w[5]-1)/10)*(e**((w[5]+1)/10)-1)+2*f11*2*(n-5)*w[5]
    return g

g=gradiente(w,n,a,f11)
print(g)


imax=10000
alpha=0.01
tol=0.0001

def gradientedescendant(w,imax,tol,alpha):
    gd=np.zeros(6)
    i=0; 
    error=np.linalg.norm(gradiente(w,n,a,f11))
    if(error<tol):
        print("El valor ingresado es el minimo")
        return w
    else: 
      while (i<imax) and (error>tol):        
            w = w - alpha*gradiente(w,n,a,f11)
            i = i+1
            error=np.linalg.norm(gradiente(w,n,a,f11))
      print(i) #agregar mensajes al usuario
      print(error)

      return w 
   
gd=gradientedescendant(w,imax,tol,alpha)
print(gd)
