"""
Ejercicio 2 — Inventario y carrito (zip + set + lista + tupla)
    Con listas de productos y precios, crea un inventario; 
    procesa un pedido con duplicados y productos desconocidos, 
    genera un carrito limpio y un snapshot inmutable, y calcula totales.

Pasos
- A partir de productos y precios (mismo largo), arma un diccionario con zip.
- Toma un pedido con duplicados/casos distintos; normaliza (title()), obtén sets: en_catalogo (intersección) y fuera (diferencia).
- Construye un carrito (lista) respetando el orden del pedido original pero saltando los que no están en catálogo; calcula el total usando el dict.
- Crea un snapshot (tupla) del carrito final.
- Actualiza precio de un producto en el dict, recalcúla y usa get para evitar errores en consultas.
"""

# Datos iniciales
productos = ["Manzana", "Pera", "Plátano", "Durazno"]
precios = [500, 700, 300, 800]

# Crea el inventario con zip() y dict():
inventario = dict(zip(productos, precios))
print("Inventario:", inventario)

# Pedido del cliente
pedido = ["pera", "pera", "manzana", "kiwi", "plátano", "PLÁTANO", "uva"]
# Normaliza mayúsculas/minúsculas:
pedido_norm = [p.title() for p in pedido]
print("Pedido normalizado:", pedido_norm)

# Conjuntos para ver qué existe o no
en_catalogo = set(pedido_norm) & set(productos)
fuera_catalogo = set(pedido_norm) - set(productos)

print("En catálogo:", en_catalogo)
print("Fuera de catálogo:", fuera_catalogo)

# Construye el carrito válido y calcula el total
carrito = [p for p in pedido_norm if p in inventario]
total = sum(inventario[p] for p in carrito)
print("Carrito limpio:", carrito)
print("Total:", total)

# Crea un snapshot inmutable y actualiza precios
snapshot = tuple(carrito)
print("Snapshot (tupla):", snapshot)

# Actualizar un precio
inventario["Pera"] = 900
nuevo_total = sum(inventario.get(p, 0) for p in carrito)
print("Nuevo total (tras actualización):", nuevo_total)
