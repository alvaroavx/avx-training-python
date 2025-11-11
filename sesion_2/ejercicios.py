
# Ejercicio 1 — Clasificador de números
"""
    Pide al usuario un número y muestra:
    Si es “Positivo”, “Negativo” o “Cero”. Si es par o impar.
    Usa: if / elif / else, operadores lógicos (and / or), y módulo %.
"""
try:
    # Pedir numero 
	numero = int(input("Ingresa un número entero: "))
	# Determinar si es positivo, negativo o cero
	if numero > 0:
		print("número positivo.")
	elif numero < 0:
		print("número negativo.")
	else:
		print("número es cero.")
	# Determinar si es par o impar
	print("Par" if numero % 2 == 0 else "Impar")
except:
	print("Numero ingresado invalido")


# Ejercicio 2 - Contador de nombres
"""
    Pide nombres hasta que el usuario deje vacío el campo. 
    Al final muestra cuántos ingresó.
    Usa: while con centinela (""), y un contador.
"""
# SIN BREAK
contador = 0
dato = input("Ingrese nombre :")
while dato != "":
    contador += 1
    dato = input("Ingrese nombre :")
print(contador)
# CON BREAK
contador = 0
while True:
	dato = input("Ingrese nombre :")
	if dato == "":
		break
	contador += 1
print(f"Se ingresaron {contador} nombres")


# Ejercicio 3 — Promedio de notas
"""
    Solicita notas hasta que el usuario escriba “fin”. 
    Ignora entradas vacías o no numéricas. 
    Muestra el promedio final o un mensaje si no se ingresaron notas.
    Usa: while True, break, try/except, validación con .isdigit().
"""
total = 0
contador = 0
while True:
	entrada = input("Nota (fin para salir): ").strip()
	if entrada.lower() == "fin":
		break
	try:
		nota = float(entrada)
		if nota >= 1.0 and nota <= 7.0:
			total += nota
			contador += 1
		else:
			print("Nota fuera de rango")
	except ValueError:
		print("Entrada no válida, intenta de nuevo")
if contador > 0:
	print(f"Promedio: {total / contador:.2f}")
	#promedio = total / contador:.2f
	#print("Promedio: ", promedio)
else:
	print("No se ingresaron datos")