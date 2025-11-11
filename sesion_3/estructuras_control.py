# ========= #
# ENUMERATE #
# ========= #

# Ejemplo 1: nombres con índice
nombres = ["Ana", "Beto", "Cami"]
for i, nom in enumerate(nombres, start=1):
    print(f"{i}. {nom}")

#Ejemplo 2: detectar espacios en una frase
frase = input("Frase: ")
for pos, ch in enumerate(frase, start=1):
    if ch == " ":
        print(f"Espacio en posición {pos}")



# ========= #
# ZIP #
# ========= #
# Ejemplo 1: alumnos y notas
alumnos = ["Ana", "Beto", "Cami"]
notas   = [6.0, 5.5, 6.3]

for nom, nota in zip(alumnos, notas):
    print(f"{nom}: {nota}")
# Ejemplo 2: productos y precios (formato alineado)
productos = ["A", "B", "C", "D"]
precios   = [1000, 2500, 500]

for p, pr in zip(productos, precios):
    print(f"{p:<10}{pr:>8,.0f}")
