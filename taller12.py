import math

def calcular_valor_estimado(x, n):
    valor_estimado = 0.0

    for i in range(n + 1):
        valor_estimado += ((-1) ** i) * (x ** i) / math.factorial(i)

    return valor_estimado

def calcular_error_aproximado(valor_real, valor_estimado):
    return abs((valor_real - valor_estimado) / valor_real) * 100

def main():
    x_real = 0.505
    valor_real = math.exp(-x_real)

    x_base = 0.5

    max_orden = 15

    print(f"Valor real de e^(-0.505): {valor_real}")

    for n in range(max_orden + 1):
        valor_estimado = calcular_valor_estimado(x_base, n)
        error_aproximado = calcular_error_aproximado(valor_real, valor_estimado)
        print(f"Aproximación de orden {n}: {valor_estimado}, Error relativo (%): {error_aproximado:.6f}")

if __name__ == "__main__":
    main()













