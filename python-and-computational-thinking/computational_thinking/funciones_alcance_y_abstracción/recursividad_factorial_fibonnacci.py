import sys

print(sys.getrecursionlimit())
# sys.setrecursionlimit(n) #es el límite a establecer

def factorial(n):
    """Calcula el factorial de n.

    :param n int > 0:
    :return n!:
    """
    if n == 1:
        return 1
    return n * factorial(n -1)

n = int(input('Escribe un entero: '))

print(factorial(n))

#Aunque la definición es muy sencilla, es también bastante ineficiente.
def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)