import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    result = 0
    n = len(x_values)

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

x_values = np.array([0, 1, 2, 3, 4])
y_values = np.array([1, 0.2, 2, 4.2, 5])

grados = [1, 2, 3]

for grado in grados:
    resultado = lagrange_interpolation(x_values[:grado+1], y_values[:grado+1], 2.5)
    print(f"Grado {grado}: f(2.5) ≈ {resultado:.4f}")

coef_grado1 = np.polyfit(x_values[:2], y_values[:2], 1)
print(f"Polinomio de grado 1: {coef_grado1[0]:.4f} * x + {coef_grado1[1]:.4f}")

coef_grado2 = np.polyfit(x_values[:3], y_values[:3], 2)
print(f"Polinomio de grado 2: {coef_grado2[0]:.4f} * x^2 + {coef_grado2[1]:.4f} * x + {coef_grado2[2]:.4f}")
