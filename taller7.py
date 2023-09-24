import math

def evaluar_e(x):
    x = -x

    valor_aproximado = 1
    termino_actual = 1
    error_relativo_porcentual = 100
    epsilon = 0.00000001
    iteraciones = 0

    while abs(termino_actual) >= epsilon:
        termino_actual *= x / (iteraciones + 1)
        valor_aproximado += termino_actual
        iteraciones += 1

        if valor_aproximado != 0:
            error_relativo_porcentual = abs((valor_aproximado - math.exp(x)) / valor_aproximado) * 100

    print(f"El valor aproximado de e^-{x} es {valor_aproximado:.8f}")
    print(f"El último error aproximado relativo porcentual εa es {error_relativo_porcentual:.8f}%")
    print(f"El número de iteraciones realizadas es {iteraciones}")

evaluar_e(0.75)


