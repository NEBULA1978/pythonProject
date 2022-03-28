#ejempo de lo que seria un do while c++
#la instruccion esta antes del ciclo y despues enmedio while

num = int(input("Introduce un numero positivo: "))


while num < 0 :
    print("Debe introduce un numero positivo")
    num = int(input("Introduce un numero positivo:"))

print("El numero: ", num, " es positivo")