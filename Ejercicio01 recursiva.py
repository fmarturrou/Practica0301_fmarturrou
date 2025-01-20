import time


def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def medir_tiempo(funcion, n):
    start_time = time.time()
    funcion(n)
    end_time = time.time()
    return end_time - start_time


valores_n = [1, 10, 20, 30, 40]


for n in valores_n:
    tiempo_recursivo = medir_tiempo(fibonacci_recursivo, n)
    print(f"n = {n}")
    print(f"Tiempo recursivo: {tiempo_recursivo:.6f} segundos")
    print('-' * 40)