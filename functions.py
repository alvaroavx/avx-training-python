
# TRY EXCEPT
def leer_float(mensaje: str) -> float | None:
    """Lee un float o devuelve None si el valor no es válido."""
    txt = input(mensaje).strip()
    try:
        return float(txt)
    except ValueError:
        print("⚠️ Dato no numérico.")
        return None
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
    print("⚠️ No numérico.")
except ZeroDivisionError as e:
    print("⚠️ División por cero.")
else:
    print(f"Resultado: {r:.2f}")  # solo si no hubo error
finally:
    pass  # lugar típico para cerrar recursos, archivos, etc.


# IF ELSE MAS SOFISTICADO CON FUNCIONES Y TRY EXCEPT
def clasificar_nota(txt: str) -> str:
    txt = txt.strip()
    if not txt:
        return "vacío"
    try:
        n = float(txt)
    except ValueError:
        return "no numérico"
    if n < 0 or n > 7:
        return "fuera de rango"
    if n < 4:
        return "insuficiente"
    if n < 6:
        return "bueno"
    return "excelente"

print(clasificar_nota(input("Nota (0–7): ")))


#WHILE 
def leer_total() -> None:
    """Suma números hasta línea vacía; ignora entradas inválidas."""
    total = 0.0
    cantidad = 0
    while True:
        s = input("Número (enter fin): ").strip()
        if s == "":
            break  # salida cuando el usuario termina
        try:
            v = float(s)
        except ValueError:
            print("⚠️ No numérico, se ignora.")
            continue  # (si quieres evitar continue hoy, elimina esta línea)
        total += v
        cantidad += 1
    print(f"n={cantidad} | total={total:.2f}")

leer_total()