import time


def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def medir_tiempo(funcion, n):
    start_time = time.time()
    funcion(n)
    end_time = time.time()
    return end_time - start_time


valores_n = [1, 10, 20, 30, 40]


for n in valores_n:
    tiempo_iterativo = medir_tiempo(fibonacci_iterativo, n)
    print(f"n = {n}")
    print(f"Tiempo iterativo: {tiempo_iterativo:.6f} segundos")
    print('-' * 40)