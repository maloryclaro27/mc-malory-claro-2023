import statistics
import math
import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]
y = [2.2, 3, 4.5, 6, 8.5, 12]
lny = np.log(y)
xlny = x * lny

x2 = [2, 4, 6, 8, 10, 12]
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

print("Alfa: ", alfa)
print("Beta: ", beta)
print("Y = ", alfa, "* e ^", beta, "X")

x = np.arange(0,10,0.1)
y = (alfa)*((math.e)**(beta*x))
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
