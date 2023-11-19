def f(x):
    return 1.5 * x**3 - 3.5 * x**2 - 2 * x + 2

def biseccion(a, b, tolerancia=1e-8, max_iteraciones=1000):
    iteracion = 0

    while (b - a) / 2 > tolerancia and iteracion < max_iteraciones:
        c = (a + b) / 2

        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    valor_raiz = (a + b) / 2
    error_aproximado = (b - a) / 2

    return valor_raiz, error_aproximado, iteracion

a = -2
b = 2

raiz_aprox, error_aprox, iteraciones = biseccion(a, b)

print(f"Raíz aproximada: {raiz_aprox:.8f}")
print(f"Error aproximado: {error_aprox:.8f}")
print(f"Número de iteraciones: {iteraciones}")
