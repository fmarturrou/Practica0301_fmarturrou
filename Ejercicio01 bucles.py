import datetime

start_time = datetime.datetime.now()
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

end_time = datetime.datetime.now()

n = 99
print(f"Fibonacci iterativo de {n}: {fibonacci_iterativo(n)}")
print("El tiempo de ejecución es:", end_time - start_time)