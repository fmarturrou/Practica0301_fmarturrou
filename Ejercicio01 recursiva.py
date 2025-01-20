import datetime

start_time = datetime.datetime.now()
def fibonacci_recursivo_memorizado(n, memo={0: 0, 1: 1}):
    # Si n no es un número entero, lo redondeamos al número entero más cercano
    n = round(n)
    
    # Si n no está en el diccionario memo, calculamos el valor
    if n not in memo:
        memo[n] = fibonacci_recursivo_memorizado(n - 1, memo) + fibonacci_recursivo_memorizado(n - 2, memo)
    
    return memo[n]


end_time = datetime.datetime.now()

n = 99
print(f"Fibonacci recursivo de {n}: {fibonacci_recursivo_memorizado(n)}")
print("El tiempo de ejecución es:", end_time - start_time)