# ====== #
# LISTAS #
# ====== #
tareas = ["limpiar", "comer"]
tareas.append("dormir")
tareas.remove("comer")
print(tareas[:2])          # slicing
print(sorted([3,1,2]))     # [1,2,3] (no modifica la original)


# ====== #
# TUPLAS #
# ====== #
p = ("Ana", 6.0)     # tupla
x, y = (10, 20)      # unpack
uno = (1,)           # tupla de 1 elemento (la coma importa)
def min_max(a,b,c): return (min(a,b,c), max(a,b,c))
print(min_max(3,8,1))  # (1, 8)


# ====== #
# DICCIONARIOS #
# ====== #
precios = {"A": 1000, "B": 2500}
print(precios.get("C", "no existe"))
for k, v in precios.items():
    print(k, v)
precios.setdefault("C", 1500)  # solo si no existe


# ====== #
# SET #
# ====== #
a = set("abracadabra")
b = set("barco")
print(a & b, a | b, a - b)
nums = [1,2,2,3,3]
print(list(set(nums)))   # [1,2,3] (orden no garantizado)
