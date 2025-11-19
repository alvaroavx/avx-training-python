# P1. es_par(n) y es_multiplo(n, m)
# (Funciones booleanas simples)
def es_par(n: int) -> bool:
    """Retorna True si n es par, False si no."""
    return n % 2 == 0


def es_multiplo(n: int, m: int) -> bool:
    """Retorna True si n es múltiplo de m."""
    if m == 0:
        raise ValueError("m no puede ser 0")
    return n % m == 0

# asserts
assert es_par(8) is True
assert es_par(7) is False
assert es_par(0) is True
assert es_multiplo(12, 3) is True
assert es_multiplo(10, 4) is False
assert es_multiplo(15, 5) is True

# Pruebas rápidas
print(es_par(8))       # True
print(es_par(7))       # False
print(es_multiplo(12, 3))  # True
print(es_multiplo(10, 4))  # False


# P2. limpia_nombre(s)
# (Normalización simple)
def limpia_nombre(s: str) -> str:
    """Limpia un nombre: elimina espacios y aplica formato título."""
    if not isinstance(s, str):
        raise TypeError("Debe recibir un string")
    return s.strip().title()

# asserts
assert limpia_nombre("  alVax  ") == "Alvax"
assert limpia_nombre("LAURA TORRES") == "Laura Torres"
assert limpia_nombre(" juan perez") == "Juan Perez"

# Pruebas
print(limpia_nombre("   alvax   "))   # "Alvax"
print(limpia_nombre("LAURA torres"))  # "Laura Torres"
print(limpia_nombre("  juan perez"))  # "Juan Perez"


# *P3. promedio_seguro(nums)
# (Ignora valores inválidos: None, strings y no-numéricos)
def promedio_seguro(*nums: float) -> float:
    """Calcula el promedio ignorando None, strings y otros no-numéricos."""
    limpios = []

    for n in nums:
        if isinstance(n, (int, float)):
            limpios.append(n)

    if not limpios:
        raise ValueError("No hay valores numéricos válidos")

    return sum(limpios) / len(limpios)

# asserts
assert promedio_seguro(5, 7, 6) == 6.0
assert promedio_seguro(10, None, "x", 20) == 15.0
assert round(promedio_seguro(3.5, 4.5), 1) == 4.0

# Pruebas
print(promedio_seguro(5, 7, 6))             # 6.0
print(promedio_seguro(10, None, "x", 20))   # 15.0
print(promedio_seguro(3.5, 4.5))            # 4.0


# P4. Docstring + type hints para una función propia
# (Ejemplo para mostrar la estructura completa)
def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calcula la distancia entre dos puntos en el plano.

    Parámetros:
        x1, y1: Coordenadas del primer punto.
        x2, y2: Coordenadas del segundo punto.

    Retorna:
        float: Distancia euclidiana.
    """
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2) ** 0.5

# asserts
assert distancia(0, 0, 3, 4) == 5.0
assert round(distancia(1, 1, 4, 5), 2) == 5.0
assert distancia(2, 2, 2, 2) == 0.0

# Prueba
print(distancia(0, 0, 3, 4))  # 5.0