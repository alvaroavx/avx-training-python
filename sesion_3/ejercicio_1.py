"""
Ejercicio 1 — Asistencia, pagos y notas (todo junto). A partir de una lista “sucia” de nombres: 
    1) normaliza y deduplica, 
    2) cruza con pagos, 
    3) arma una lista ordenada editable, 
    4) congélala como tupla, 
    5) crea un diccionario de notas con zip, consulta/actualiza y recorre.

Pasos.
- Lista cruda con duplicados y espacios → set normalizado (title() + strip()).
- Con un set pagaron, muestra intersección (pagaron y asistieron) y diferencia (deben).
- Convierte el set a lista ordenada (mutable). Inserta "Invitado" al inicio y elimina "Ana" si existe.
- Congela la lista final en una tupla publicada.
- Crea un diccionario notas con zip(lista_sin_invitado, lista_de_notas); usa get, actualiza y recorre .items().
"""

nombres = [
    "ana", "Beto", "cami", "ANA", "beto  ", "  camila", "PEDRO", 
    "Ana", "Cami", "pedro ", "lucas", "Lucas ", "LUCAS"
]
pagos = [True, False, True, True, False, True, False]
notas = [6.5, 5.8, 7.0, 4.9, 6.2, 5.5, 6.8]

# 1) Normalizar y deduplicar (SET)
listado = []
for nombre in nombres:
    listado.append(nombre.strip().title())
asistentes = set(listado)
print("Asistentes únicos:", asistentes)

# 2) Cruce con pagos (SETS)
asistentes = list(sorted(asistentes))
asistentes = set(asistentes)
pagaron = set()

for nombre, pago in zip(asistentes, pagos):
    if pago:
        pagaron.add(nombre)
    print(f"-{nombre}: {"Pago al día" if pago else "Con deuda"}" )

print("Pagaron y asistieron:", asistentes & pagaron)
print("Asistieron y NO pagaron:", asistentes - pagaron)

# 5) Diccionario de notas (DICT) con zip
diccionario_notas = dict()
for asistente, nota in zip(asistentes, notas):
    print(f"-{asistente}: {nota}")
    diccionario_notas[asistente] = nota
print(diccionario_notas)





# 3) Lista ordenada editable (LIST)
lista = sorted(asistentes)               # orden alfabético
lista.insert(0, "Invitado")              # mutable
if "Ana" in lista:
    lista.remove("Ana")
print("Lista editable:", lista)

# 4) Congelar versión publicada (TUPLA)
publicada = tuple(lista)
print("Publicada (tupla):", publicada)

