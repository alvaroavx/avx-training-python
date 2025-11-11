"""Generador de Boleta Simple (S1)
Pide 3 ítems, calcula subtotal, IVA 19% y total, y muestra una boleta formateada.
"""

IVA = 0.19

def total_linea(cantidad: int, precio_unit: float) -> float:
    """Devuelve total de línea = cantidad * precio_unit."""
    return cantidad * precio_unit

# --- Captura de datos (puedes repetir 3 veces este bloque) ---
desc1 = input("Descripción 1: ").strip()

try:
    cant1 = int(input("Cantidad 1: ").strip())
    prec1 = float(input("Precio unitario 1: ").strip())
except ValueError:
    print("⚠️ Dato inválido. Usa números válidos para cantidad y precio.")
    raise SystemExit(1)

# (Repite para desc2/cant2/prec2 y desc3/cant3/prec3)

# --- Cálculos ---
t1 = total_linea(cant1, prec1)
# t2 = ...
# t3 = ...
subtotal = t1  # + t2 + t3
iva = subtotal * IVA
total = subtotal + iva

# --- Salida formateada ---
print("\nBOLETA")
print(f"{'Descripción':<20}{'Cant.':>6}{'P.Unit':>12}{'Total':>12}")
print("-" * 50)
print(f"{desc1:<20}{cant1:>6}{prec1:>12.2f}{t1:>12.2f}")
# print(f"{desc2:<20}{cant2:>6}{prec2:>12.2f}{t2:>12.2f}")
# print(f"{desc3:<20}{cant3:>6}{prec3:>12.2f}{t3:>12.2f}")
print("-" * 50)
print(f"{'SUBTOTAL':<20}{subtotal:>30,.2f}")
print(f"{'IVA 19%':<20}{iva:>30,.2f}")
print(f"{'TOTAL':<20}{total:>30,.2f}")
