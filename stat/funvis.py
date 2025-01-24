import numpy as np
import matplotlib.pyplot as plt

#define x vlues
x=np.linspace(0,20,100)

#define y values
y=np.sin(x)

#plot the function
plt.plot(x,y)
plt.title("sine function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()