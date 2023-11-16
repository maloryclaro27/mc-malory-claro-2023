import numpy as np
import matplotlib.pyplot as plt

while True:
  n = int(input("Ingrese el número de puntos: "))
  if n < 5:
    print("El numero de puntos debe ser mayor a 5")
  elif n >= 5:
    break
    
x = []
y = []

for i in range(n):
    x_i, y_i = map(float, input(f"Ingrese el punto {i+1} (x, y): ").split())
    x.append(x_i)
    y.append(y_i)

while True:
  grado = int(input("Ingrese el grado del polinomio (mayor o igual a 2): "))
  if grado < 2:
    print("El grado debe ser mayor o igual a 2")
  elif grado >= 2:
    break

modelo = np.poly1d(np.polyfit(x, y, grado))

x_line = np.linspace(min(x), max(x), 100)
y_line = modelo(x_line)
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()
