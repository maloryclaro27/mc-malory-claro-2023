import numpy as np
import matplotlib.pyplot as plt

def regresion_lineal_minimos_cuadrados(x, y):
    X = np.column_stack((np.ones_like(x), x))

    beta = np.linalg.inv(X.T @ X) @ X.T @ y

    return beta

def graficar_regresion_lineal(x, y, beta):
    plt.scatter(x, y, label='Datos')

    x_regresion = np.linspace(min(x), max(x), 100)
    y_regresion = beta[0] + beta[1] * x_regresion
    plt.plot(x_regresion, y_regresion, color='red', label='Regresión Lineal')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([7, 5, 6, 3, 4, 2.5, 2, 0.5])

beta = regresion_lineal_minimos_cuadrados(x, y)

print(f"Coeficiente beta0 (intercepto): {beta[0]}")
print(f"Coeficiente beta1 (pendiente): {beta[1]}")

graficar_regresion_lineal(x, y, beta)



