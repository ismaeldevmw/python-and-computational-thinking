# Argumentos de otras funciones
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

    return resultados

nums = [1, 2, 3]
print(aplicar_operacion(multiplicar_por_dos, nums))
# [2, 4, 6]

print(aplicar_operacion(sumar_dos, nums))
# [3, 4, 5]

# Funciones en expresiones
sumar = lambda x, y: x + y

print(sumar(2, 3))

# Funciones en estructuras de datos
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-2))

