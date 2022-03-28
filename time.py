import math
import time



radio = float(input("radio -> "))
area = math.pi * radio**2
longitud = 2* math.pi * radio
a = input("a -> ")
b = input("b -> ")



t = 10
a, b = b , a
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
print(f"El area es: {area}")
print(f"La longitud de la circunferencia es: {longitud}")

while True:
    print(b)
    if b ==0:
        break
    t -= 1
    time.sleep(1)
print('Hecho')