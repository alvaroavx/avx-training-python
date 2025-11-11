# Comentario: esta función suma dos números
def sumar(a: int, b: int) -> int:
    """Devuelve la suma de a y b."""
    return a + b

x = int(input("Número 1: ").strip())
y = int(input("Número 2: ").strip())

print("Suma:", sumar(x, y))                     # múlt. args
print(f"Suma formateada: {sumar(x, y):,}")      # con separador de mileszxcvxz
