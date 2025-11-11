# TRY EXCEPT
try:
    txt = input("ingrese un numero:")
    numero = int(txt)
except ValueError:
    print("Dato no numérico.")

# 1) Reintento hasta valor válido o enter para salir
while True:
    v = input("Número (enter fin): ").strip()
    if v == "":
        break
    try:
        n = float(v)             # intenta convertir
    except ValueError:
        print("⚠️ No numérico, intenta de nuevo.")
        continue                  # vuelve a pedir (verás esto en S3 también)
    print(f"OK: {n:.2f}")

# 2) Patrón con else/finally (solo mostrar si te lo preguntan)
txt = input("Divisor: ").strip()
try:
    d = float(txt)
    r = 10 / d
except ValueError as e:
    print("No numérico.")
except ZeroDivisionError as e:
    print("División por cero.")
else:
    print(f"Resultado: {r:.2f}")  # solo si no hubo error
finally:
    pass  # lugar típico para cerrar recursos, archivos, etc.



# IF ELSE
edad_texto = input("Edad: ").strip()
if edad_texto.isdigit():
	print("Es un numero")
	edad = int(edad_texto)
	if edad <= 0:
		print("edad invalida")
	elif edad < 18:
		print("menor de edad")
	elif edad < 65:
		print("adulto")
	else:
		print("mayor de edad")
else:
	print("No es un numero")




# EXPRESION CONDICIONAL TERNARIA
monto = float(input("Monto: "))
exento = input("¿Exento? (s/n) ").lower().strip()

total = monto if exento == "s" else monto * 1.19
print(f"Total: {total:.2f}")

# Más ejemplos puntuales:
nota = float(input("Nota (0–7): "))
estado = "Aprobado" if nota >= 4 else "Reprobado"
print(f"Estado: {estado}")

edad = int(input("Edad: "))
categoria = "Mayor" if edad >= 18 else "Menor"
print(f"Categoría: {categoria}")




# COMPARACION ENTRE IFS:
# Ternario
tarifa = 0 if exento == "s" else monto * 0.19

# If/else clásico (idéntico resultado, a veces más claro)
if exento == "s":
    tarifa = 0
else:
    tarifa = monto * 0.19




# COMBINAR CONDICIONES
usuario = input("Usuario: ").strip().lower()
clave = input("Clave: ").strip()
if(usuario == "admin" or usuario == "soporte") and clave == "1234":
	print("Acceso permitido")
else:
	print("Acceso denegado")


s = input("Texto (2–20 chars, no solo espacios): ")

valido_largo = len(s.strip()) >= 2 and len(s) <= 20
solo_letras  = s.replace(" ", "").isalpha()

if valido_largo and solo_letras:
    print("OK")
else:
    print("Inválido")

# VALIDACIONES UTILES
# 1) Validación de rango
x = int(input("x: "))
if 0 <= x <= 100:    # comparaciones encadenadas
    print("En rango")

# 2) Texto no vacío y forma
s = input("Nombre: ")
ok = (2 <= len(s.strip()) <= 30) and s.replace(" ", "").isalpha()
print("OK" if ok else "Inválido")

# 3) Combinación con 'not' (De Morgan)
#  No (A y B)  ≡  (No A) o (No B)
edad = int(input("Edad: "))
if not (0 <= edad <= 120):
    print("Edad fuera de rango")
# equivalente (más explícito):
if edad < 0 or edad > 120:
    print("Edad fuera de rango")

# DEMO CORTOCIRCUITO
def L(msg):
    print(msg); return True

def F(msg):
    print(msg); return False

print("\nAND:")
L("A") and L("B")        # imprime A y B
F("A") and L("B")        # imprime A y NO evalúa B

print("\nOR:")
L("A") or L("B")         # imprime A y NO evalúa B
F("A") or L("B")         # imprime A y B

# WHILE
dato = input("Ingrese algo (enter para terminar):")
while dato != "":
	print("Recibi: " + dato)
	dato = input("Ingrese algo (enter para terminar):")
print("FIN")

while True:
	dato = input("Ingrese algo (enter para terminar):")
	if dato == "":
		break
	print("Recibi: " + dato)
print("FIN")

total = 0.0
while True:
    s = input("Número (enter para terminar): ").strip()
    if s == "":
        break
    total += float(s)
print(f"Total: {total:.2f}")

#Estructura general (sin break)
# Patrón A: leo → while → proceso → leo
dato = input("Ingrese algo (enter para terminar): ")
while dato != "":
    print("Leí:", dato)
    dato = input("Ingrese algo (enter para terminar): ")
print("Fin del programa.")

#Estructura con break
# Patrón B: while True → leo → si centinela: break → proceso
while True:
    dato = input("Ingrese algo (enter para terminar): ")
    if dato == "":
        break
    print("Leí:", dato)
print("Fin del programa.")


# FOR
for letra in "hola":
	print(letra)
	
frutas = ["manzana", "platano", "naranja"]
for fruta in frutas:
	print(f"- {fruta.upper()}")
     
frutas = ["manzana", "pera", "uva"]
for f in frutas:
    print(f"- {f.title()}")
    print(f"- {f}")


texto = input("Frase: ")
vocales = "aeiouáéíóú"
contador = 0
for ch in texto.lower():
    if ch in vocales:
        contador = contador + 1
print("Vocales:", contador)


nombres = ["Ana", "Luis", "Bárbara"]
for nombre in nombres:
    print(nombre.title())


for letra in "hola":
    print(letra)

# FOR IN RANGE

for i in range(1, 6):   # 1..5
    print(i)


# Pares de 2 a 10
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Cuenta regresiva
for i in range(5, 0, -1):
    print(i, end=" ")

for i in range(1, 6):  # 1..5
    print(i)

# Pares de 2 a 10
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Cuenta regresiva 5..1
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Repetir N veces (0..N-1)
n = int(input("Veces: "))
for _ in range(n):
    print("Hola")

# Tabla de multiplicar (1..10)
num = int(input("Número: "))
for i in range(1, 11):
    print(f"{num} x {i:>2} = {num*i:>3}")


# FOR ELSE
nums = [2, 4, 6, 9, 10]
for n in nums:
    if n % 2 != 0:
        print("Encontré impar:", n)
        break
else:
    print("Todos eran pares")

# ¿Es primo? (versión simple)
n = int(input("n: "))
if n < 2:
    print("No primo")
else:
    for d in range(2, n):
        if n % d == 0:
            print(f"Compuesto (divisible por {d})")
            break
    else:
        print("Primo")

    
# Buscar un número en la lista
numeros = [1, 3, 5, 7, 9]
buscar = 4

for n in numeros:
    if n == buscar:
        print("Encontrado!")
        break
else:
    print("No está en la lista.")


# WHILE ELSE
intentos = 3
while intentos > 0:
    clave = input("Clave: ")
    if clave == "1234":
        print("Acceso"); break
    intentos -= 1
else:
    print("Bloqueado por intentos")


intentos = 3
while intentos > 0:
    clave = input("Contraseña: ")
    if clave == "python":
        print("Acceso permitido")
        break
    intentos -= 1
else:
    print("Cuenta bloqueada")
