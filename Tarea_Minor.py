#Librerias
import numpy as np
#para usar euler
from math import e


#funcion 1
def y(k):
    Y=e**(k/10)+e**((k-1)/10)
    return Y
 
def funcion(w,n,a):
  f=np.zeros(2*n)
  f[0]=w[0]-0.2
  for k in range(1,n):
      f[k]=np.sqrt(a)*(e**(w[k]/10)+e**(w[k-1]/10)-y(k))
  for k in range(n,2*n-1):
      f[k]=np.sqrt(a)*(e**(w[k-n+1]/10)-e**(-1/10))
  f11=0
  for i in range(0,n):
      f11=f11+(n-i+1)*w[i]
  f[11]=f11-1
  return f

w=np.zeros(12)
a=10**(-5)
n=6


funcion(w,n,a)

print("probando ");

print("probando branch");
print("funciona");
