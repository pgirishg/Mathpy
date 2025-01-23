import cmath

#coefficients of the quadratic equation

a = 1
b = 5
c = 6

#calculate the discriminant
d = cmath.sqrt(b**2 - 4*a*c)

#find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print(f"soultion are {sol1} and {sol2}")

