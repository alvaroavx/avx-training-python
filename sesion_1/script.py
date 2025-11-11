import math, datetime, random, pathlib

# Introducción a Python
# =====================
print(f"Raíz cuadrada de 16 - {math.sqrt(16)}")
print(f"Fecha actual (AAAA-MM-DD) - {datetime.datetime.now().date()}")
print(f"Número aleatorio entero entre 1 y 6 - {random.randint(1, 6)}")
print(f"Ruta absoluta de la carpeta actual - {pathlib.Path('.').resolve()}")


# Mentalidad de programación
# ==========================
# Python
nombre = input("¿Tu nombre? ")
print(f"Hola, {nombre}")

print("Hola" + 5)
#Type Error

# REPL vs Script 
# ==============
#  desde REPL
2 + 2
"Hola".upper()
from math import sqrt
sqrt(16)
#  desde file
print("Hola, mundo")
nombre = input("¿Cómo te llamas? ")
print(f"¡Mucho gusto, {nombre}!")

# Entrada y salida básica de datos
# ================================
total = 1234.567
# print
print("Total:", total)                          # múlt. argumentos
print(f"Total formateado: {total:.2f}")         # f-string (2 decimales)
print(1, 2, 3, sep=" - ")                       # separador personalizado
print("sin salto", end=""); print(" en la misma línea")
# input
nombre = input("¿Nombre? ").strip()
edad = int(input("¿Edad? ").strip())
print(f"Hola {nombre}, en 5 años tendrás {edad + 5}.")
# try except
try:
    precio = float(input("Precio: ").strip())
except ValueError:
    print("Ingresa un número válido.")
else:
    print(f"Con IVA (19%): {precio * 1.19:.2f}")
# Comentario: 
def sumar(a: int, b: int) -> int:
    """Devuelve la suma de a y b.
    a y b deben ser números enteros.
    """
    return a + b
print(sumar(2, 3))
# help(sumar)  # muéstralo si quieres enseñar docstrings

# Tipos primitivos & operaciones
# ==============================
edad = int(input("Edad: "))
anhos = 5
print(f"En {anhos} años tendrás {edad + anhos}.")
# Operadores: Aritméticos
7/2  # 3.5     (división real)
7//2 # 3       (división entera)
7%2  # 1       (módulo)
2**3 # 8       (potencia)
# Comparación: == != < <= > >=
# Lógicos: and or not
# Error típico & solución:
print("Edad: " + 5)      # TypeError
print("Edad: " + str(5)) # OK
# Tipos y type()
a, b, c, d = 7, 3.5, "hola", True
print(type(a), type(b), type(c), type(d))
# Conversión correcta
n = int("42")         # OK
x = float("3.14")     # OK
s = str(123)          # "123"
# int("3.14") -> ValueError (coméntalo)
# f-strings útiles
precio = 1234.5
print(f"${precio:.2f}")   # $1234.50
print(f"{1000000:,}")     # 1,000,000 (separador miles)
# Operadores en acción
print(7/2, 7//2, 7%2, 2**5)   # 3.5  3  1  32
x = 10
print(0 < x < 20, (x % 2 == 0) and (x > 5))

# Depuracion de codigo
print("Hola" + 5)
# TypeError: can only concatenate str (not "int") to str
# FIX:
print("Hola " + str(5))
# o:
print(f"Hola {5}")


