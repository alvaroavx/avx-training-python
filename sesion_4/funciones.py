
#############################
## FUNCIONES VS PARAMETROS ##
#############################

# Ejemplo básico
def sumar(a, b):   # a y b son parámetros
    return a + b

sumar(3, 5)        # 3 y 5 son  argumentos

# Con argumentos por nombre (keyword arguments)
def presentar(nombre, ciudad):
    print(f"{nombre} es de {ciudad}")

presentar(nombre="Diego", ciudad="Rancagua")
presentar(nombre="Alejandra", ciudad="Iquique")
presentar(nombre="Carlos", ciudad="Santo Domingo")

# Con valores por defecto
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}")

saludar()            # usa el valor por defecto "amigo"
saludar("Laura")       # "Laura" es el argumento

# Con args
def total(*numeros):   # numeros parámetro especial (tupla)
    return sum(numeros)

total(5, 10, 15)
total(5, 10)
total(5, 10, 15, 20, 25, 40)

# Con kwargs
def config(**opciones):   # opciones parámetro dict
    return opciones

config(debug=True, modo="dev")
config(valor1="1", valor2="Casa", valor3=[1,2,3], valor4=True)
# argumentos: debug=True, modo="dev"

# Combinacion
def demo(x, *args, **kwargs):
    print("x:", x)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, 4, modo="dev", debug=True)
# parámetros normales → *args → parámetros keyword → **kwargs
# def f(a, b=0, *args, modo="dev", **kwargs):


######################################
## RETURN, VALORES MULTIPLES Y NONE ##
######################################

def dividir(a, b):
    if b == 0:
        return None, "División por cero"
    return a / b, None
res, err = dividir(10, 2)

def dividir(a, b):
    try:
        if b == 0:
            return None, "División por cero"
        resultado = a / b
        return resultado, None
    except TypeError:
        return None, "Los valores deben ser números"
    except Exception as e:
        return None, f"Error inesperado: {e}"

# Pruebas
res, err = dividir(10, 2)
print(res, err)
res, err = dividir(10, 0)
print(res, err)
res, err = dividir("a", "b")
print(res, err)


# Normalizar notas: devuelve promedio, mínima, máxima
def resumen_notas(notas):
    if not notas:
        return None, None, None
    return sum(notas) / len(notas), min(notas), max(notas)

prom, lo, hi = resumen_notas([5.5, 6.0, 6.8])

#############################
## DOCSTRINGS & TYPE HINTS ##
#############################

def imc(peso: float, altura_m: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC).
    
    Parámetros:
        peso (float): Peso en kilogramos.
        altura_m (float): Altura en metros.
    
    Retorna:
        float: El IMC calculado como peso / (altura_m ** 2).
    """
    return peso / (altura_m ** 2)

print(help(imc))

################################
## CAPTURAR ERRORES & ASSERTS ##
################################

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0")
    return a / b
assert dividir(10, 2) == 5.0  # prueba rápida

#def promedio_seguro(valores):
def promedio_seguro(valores: list[float]) -> float:
    # Error 1: no es una lista
    if not isinstance(valores, list):
        raise TypeError("La entrada debe ser una lista")

    # Error 2: lista vacía
    if not valores:
        raise ValueError("La lista no puede estar vacía")

    return sum(valores) / len(valores)

# Prueba rápida
assert promedio_seguro([10, 20, 30]) == 20.0