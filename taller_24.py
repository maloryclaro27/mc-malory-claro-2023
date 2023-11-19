# PolinomiosLagrange.py
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

# TrazadoresCubicos.py
import numpy as np
from scipy.interpolate import CubicSpline

def trazadores_cubicos(x_values, y_values, x):
    cs = CubicSpline(x_values, y_values)
    return cs(x)

# Datos de la tabla
x_values = np.array([0, 1, 2, 3, 4, 5, 6])
y_values = np.array([2, 4, 5, 4, -3, 1, 12])

# Estimación para x = 4.75 utilizando Polinomio de Lagrange
x_estimado_lagrange = 4.75
y_estimado_lagrange = lagrange_interpolation(x_values, y_values, x_estimado_lagrange)

# Estimación para x = 4.75 utilizando Trazadores Cúbicos
x_estimado_trazadores = 4.75
y_estimado_trazadores = trazadores_cubicos(x_values, y_values, x_estimado_trazadores)

# Resultados
print(f"Estimación usando Polinomio de Lagrange para x = {x_estimado_lagrange}: {y_estimado_lagrange:.4f}")
print(f"Estimación usando Trazadores Cúbicos para x = {x_estimado_trazadores}: {y_estimado_trazadores:.4f}")

# Gráfica
import matplotlib.pyplot as plt

x_interp = np.linspace(min(x_values), max(x_values), 1000)
y_interp_lagrange = lagrange_interpolation(x_values, y_values, x_interp)
y_interp_trazadores = trazadores_cubicos(x_values, y_values, x_interp)

plt.plot(x_values, y_values, 'o', label='Datos')
plt.plot(x_interp, y_interp_lagrange, label='Polinomio de Lagrange', linestyle='--')
plt.plot(x_interp, y_interp_trazadores, label='Trazadores Cúbicos', linestyle='--')
plt.scatter([x_estimado_lagrange, x_estimado_trazadores], [y_estimado_lagrange, y_estimado_trazadores], color='red', marker='x', label='Estimación en x = 4.75')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
