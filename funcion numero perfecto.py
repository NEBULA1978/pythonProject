def es_numero_perfecto(numero):
    suma = 0

    for i in range(1, numero):
        if numero % 1 == 0:
            suma += i
    return  suma == numero
    print(es_numero_perfecto(6))#1+2+3+4++6=16
    print(es_numero_perfecto(12))
    print(es_numero_perfecto(28))
    print(es_numero_perfecto(496))
    print(es_numero_perfecto(8128))