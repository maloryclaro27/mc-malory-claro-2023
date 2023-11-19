import operator
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np
x = [1,3,5,7,9,11,13,15]
y = [8.5,13,15,16,17,17.5,18,19]

plt.plot(x,y)
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""MINIMOS CUADRADOS

"""

import operator
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np
x = [1,3,5,7,9,11,13,15]
y = [2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
xy = list(map(operator.mul, x, y))

x2 = [1,3,5,7,9,11,13,15]
for i in range(0,len(x)):
	x2[i]=x2[i]*x2[i]

promy = statistics.mean(y)
promx = statistics.mean(x)

a1 = ((len(x))*(sum(xy))-(sum(x))*(sum(y)))/((len(x))*(sum(x2))-(sum(x))**2)
a0 = promy - (a1)*promx
print("a1 = ", a1)
print("a0 = ", a0)

x = np.arange(0,10,1)
y = (a1)*(x)+(a0)
plt.plot(x,y)
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""MODELO EXPONENCIAL"""

x = [1,3,5,7,9,11,13,15]
y = [2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
lny = np.log(y)
xlny = xy = list(map(operator.mul, x, lny))

x2 = [1,3,5,7,9,11,13,15]
for i in range(0,len(x)):
	x2[i]=x2[i]*x2[i]

promlny = statistics.mean(lny)
promx = statistics.mean(x)

a1 = ((len(x))*(sum(xlny))-(sum(x))*(sum(lny)))/((len(x))*(sum(x2))-(sum(x))**2)
a0 = promlny - (a1)*promx
print("a1 = ", a1)
print("a0 = ", a0)

alfa = (math.e)**a0
beta = a1

x = np.arange(0,10,1)
y = (alfa)*((math.e)**(beta*x))
plt.plot(x,y)
plt.plot(x,y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""RAZÓN DE CRECIMIENTO"""

#definir listas
x = [1,3,5,7,9,11,13,15]
y = [2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]

x1 = [1,3,5,7,9,11,13,15]
for i in range(0,len(x)):
	x1[i]=1/x1[i]
sumx1 = sum(x1)
promx1 = statistics.mean(x1)

y1 = [2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
for i in range(0,len(x)):
	y1[i]=1/y1[i]

x1y1 = list(map(operator.mul, x1, y1))

x2 = x1
for i in range(0,len(x)):
	x2[i]=x2[i]*x2[i]
sumx2 = sum(x2)

promy1 = statistics.mean(y1)
#operaciones
a1 = ((len(x))*(sum(x1y1))-(sumx1)*(sum(y1)))/((len(x))*(sumx2)-(sumx1)**2)
a0 = promy1 - (a1)*promx1
print("a1 = ", a1)
print("a0 = ", a0)

alfa = 1/a0
beta = a1/a0

x = np.arange(0,10,1)
y = (alfa)*(x/(beta))
plt.plot(x,y)
plt.plot(x,y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""ECUACIÓN DE POTENCIAS"""

#definir listas
x = [1,3,5,7,9,11,13,15]
y = [2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
lnx = np.log10(x)
sumlnx = sum(lnx)
promx = statistics.mean(lnx)
lny = np.log10(y)

xy = list(map(operator.mul, lnx, lny))

for i in range(0,len(x)):
	lnx[i]=lnx[i]*lnx[i]
sumlnx2 = sum(lnx)

promy = statistics.mean(lny)
#operaciones
a1 = ((len(x))*(sum(xy))-(sumlnx)*(sum(lny)))/((len(x))*(sumlnx2)-(sumlnx)**2)
a0 = promy - (a1 * promx)
print("a1 = ", a1)
print("a0 = ", a0)

alfa = 10**(a0)
beta = a1

x = np.arange(0,10,1)
y = (alfa)*(x**beta)
x1 = np.arange(0,10,0.1)
y1 = (alfa)*(x1**beta)
plt.plot(x1,y1)
plt.plot(x,y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""RTA: EL ÚLTIMO CÓDIGO (ECUACIÓN DE POTENCIAS) SE AJUSTA MUCHO MÁS DE UNA MANERA VISUAL"""
