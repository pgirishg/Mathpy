import numpy as np
import scipy.integrate as quad

# define the function to be integrated
def f(x):
    return x**2

#calulate the integral
area,error=quad.quad(f,0,1)
print(f"area under the curve y=x**2 from x=0 to x=1 {area}")