import time

def fibonacci_iterativo(n):
    if n < 0:
        return "No existe para números negativos"

    if n == 0:
        return 0

    if n == 1:
        return 1

    anterior = 0
    actual = 1

    for i in range(2, n + 1):
        siguiente = anterior + actual
        anterior = actual
        actual = siguiente

    return actual

def fibonacci_recursivo(n):
    if n < 0:
        return "No existe para números negativos"

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

print("========================================")
print("       SERIE DE FIBONACCI")
print("========================================")

while True:

    try:
        n = int(input("\nIngresa el valor de n: "))

        if n < 0:
            print("Por favor, introduce un número mayor o igual a 0.")
            continue

        break

    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

inicio_iterativo = time.perf_counter()

resultado_iterativo = fibonacci_iterativo(n)

fin_iterativo = time.perf_counter()

tiempo_iterativo = fin_iterativo - inicio_iterativo


if n <= 35:

    inicio_recursivo = time.perf_counter()

    resultado_recursivo = fibonacci_recursivo(n)

    fin_recursivo = time.perf_counter()

    tiempo_recursivo = fin_recursivo - inicio_recursivo

else:

    resultado_recursivo = "No ejecutado (n demasiado grande)"
    tiempo_recursivo = 0

print("\n========================================")
print("             RESULTADOS")
print("========================================")

print(f"\nValor de n: {n}")

print("\n--- Método Iterativo ---")
print(f"Resultado: {resultado_iterativo}")
print(f"Tiempo de ejecución: {tiempo_iterativo:.10f} segundos")


print("\n--- Método Recursivo ---")

if n <= 35:
    print(f"Resultado: {resultado_recursivo}")
    print(f"Tiempo de ejecución: {tiempo_recursivo:.10f} segundos")
else:
    print(resultado_recursivo)

if n <= 35 and tiempo_iterativo > 0:

    print("\n========================================")
    print("             COMPARACIÓN")
    print("========================================")

    if tiempo_recursivo > tiempo_iterativo:
        veces = tiempo_recursivo / tiempo_iterativo

        print(
            f"\nEl método recursivo tardó aproximadamente "
            f"{veces:.2f} veces más que el iterativo."
        )

    else:
        print("\nLos tiempos son muy similares en esta ejecución.")

print("\nPrograma terminado.")
