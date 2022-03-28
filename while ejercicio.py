suma=0
opc='s'
while opc == 's' or opc =='S':
    num = float(input("Introduce un numero: "))
    suma+=num
    opc = input("Desea untroducir otro numero? S/N: ")
print("La suma es: ", suma)