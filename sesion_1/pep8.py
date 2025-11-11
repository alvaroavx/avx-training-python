# IDENTACION
# ==========
# Bien
if x > 5:
    hacer_algo()

def f(a, b, c,
      d, e):
    pass  # continuación alineada

# Mal (línea eterna y poco legible)
def f(a, b, c, d, e): pass

# TAMAÑO DE LINEA
# ===============
with open(ruta_muy_larga) as f1, \
     open(otra_ruta_larga, 'w') as f2:
    f2.write(f1.read())

# LINEAS Y ESPACIOS EN BLANCO
# ===========================
class A:
    def m1(self): ...
    
    def m2(self): ...
    
    
def util(): ...

# ESPACIOS EN BLANCO DONDE SI DONDE NO
# ====================================
# Bien
x = 5
if x == 5:
    pass
def f(por_defecto=5): ...

duplica( 2)
lista = [1, 2, 3]
print(x, y)

# Mal
x=5
if x==5: ...
def f(por_defecto = 5): ...
duplica( 2 )
lista [ 1 ]
print(x , y)

# No alinear artificialmente
a = 0
largo_nombre = 10
otra = 3

# CONVENCIONES DE NOMBRE
# ======================
CONSTANTE = 10

class MiClase:
    def mi_metodo(self, valor_inicial):
        return valor_inicial + CONSTANTE

# IMPORTS (ORDEN Y ORGANIZACION)
# ==============================
# Bien
import os
import sys

from collections import deque, defaultdict

# Mal
import os, sys
from collections import *

# COMAS AL FINAL DE LINEA
# =======================
tupla = (1,)
FICHEROS = [
    'a.txt',
    'b.txt',
]
