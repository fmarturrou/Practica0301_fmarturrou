import datetime

start_time = datetime.datetime.now()
def fibonacci_recursivo_memorizado(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_recursivo_memorizado(n - 1, memo) + fibonacci_recursivo_memorizado(n - 2, memo)
    return memo[n]

end_time = datetime.datetime.now()

n = 99
print(f"Fibonacci recursivo de {n}: {fibonacci_recursivo_memorizado(n)}")
print("El tiempo de ejecución es:", end_time - start_time)