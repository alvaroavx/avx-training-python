print("=| Hola, este es la tarea 1 |=\n")

item_1 = input("Ingrese la descripcion del item 1: ")
cantidad_1 = int(input("Ingrese la cantidad de items: "))
precio_1 = float(input("Ingrese el precio unitario: "))
subtotal_1 = cantidad_1 * precio_1

item_2 = input("\nIngrese la descripcion del item 2: ")
cantidad_2 = int(input("Ingrese la cantidad de items: "))
precio_2 = float(input("Ingrese el precio unitario: "))
subtotal_2 = cantidad_2 * precio_2

item_3 = input("\nIngrese la descripcion del item 3: ")
cantidad_3 = int(input("Ingrese la cantidad de items: "))
precio_3 = float(input("Ingrese el precio unitario: "))
subtotal_3 = cantidad_3 * precio_3

print("=| Sub Totales |=")
print(f"\nSubtotal item {item_1}: {subtotal_1}")
print(f"Subtotal item {item_2}: {subtotal_2}")
print(f"Subtotal item {item_3}: {subtotal_3}")

IVA = 0.19
subtotal = subtotal_1 + subtotal_2 + subtotal_3
iva = subtotal * IVA
total = subtotal + iva

print("+--------+")
print("+-BOLETA-+")
print("+--------+")
print(f"SUBTOTAL: {subtotal:.2f}")
print(f"IVA 19%: {iva:.2f}")
print(f"TOTAL: {total:.2f}")


















