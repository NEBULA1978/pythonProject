#from math import pow
import math
import time
t = 10
while True:
    print(t)
    if t ==0:
        break
    t -= 1
    time.sleep(1)
print('Hecho')




x=5
y=4.33
z=9.87
a=-8



#Funcion

print ("El numero ", y, " Redondeando hacia Arriba es ",math.ceil(y))
print ("El numero ", y, " Redondeando hacia Abajo es ",math.floor(y))
print ("El valor absoluto de ", a, " es ",math.fabs(a))


print ("El factorial de ", x, " es ",math.factorial(x))



print ("El valor de ",x, " Elevado a la 4 es ",math.pow(x,4))
while True:
    print(x)
    if x ==0:
        break
    x -= 1
    time.sleep(1)
print('Hecho')


print ("La raiz cuadrada de ",z, " es ", math.sqrt(z))



print ("El Coseno de 90 es ",math.cos(90))
while True:
    print(y)
    if y ==0:
        break
    y -= 1
    time.sleep(1)
print('Hecho')

print ("El Seno de 90 es ",math.sin(90))
print ("El Tangente de 90 es ",math.tan(90))
print("El angulo 90 convertido de radianes a grados es ",math.degrees(90))
print("El angulo 90 convertido de grados a radianes es ",math.radians(90))
print("El valor de la constante Pi es ",math.pi)

