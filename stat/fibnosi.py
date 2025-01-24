def fibinoci(n):
    fib_sequnce = [0, 1]
    while len(fib_sequnce) < n:
        fib_sequnce.append(fib_sequnce[-1] + fib_sequnce[-2])
    return fib_sequnce

n = 10
print(f"Fibinoci sequence of {n} is {fibinoci(n)}")
