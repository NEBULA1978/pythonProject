precio = float(input("Digite el precio: "))
a = input("a -> ")
b = input("b -> ")

descuento = precio * 0.15
precio_final = precio - descuento

print(f"El precio final a pagar es de €{precio_final:.2f}")
