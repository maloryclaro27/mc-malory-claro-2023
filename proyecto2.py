import numpy as np
import matplotlib.pyplot as plt

n = int(input("Ingrese el número de puntos: "))
x = []
y = []
for i in range(n):
    x_i, y_i = map(float, input(f"Ingrese el punto {i+1} (x, y): ").split())
    x.append(x_i)
    y.append(y_i)

grado = int(input("Ingrese el grado del polinomio (mayor o igual a 2): "))

modelo = np.poly1d(np.polyfit(x, y, grado))

x_line = np.linspace(min(x), max(x), 100)
y_line = modelo(x_line)
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()
