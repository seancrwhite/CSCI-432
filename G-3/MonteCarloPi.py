import matplotlib.pyplot as plt
import random
import math

def monteCarloPi(a, n):
    """
    Calculates the value of pi and creates a graph

    Input
    -------
    a - length of the side of the square
    n - number of points
    """
    r = 0.5 * a
    n_c = 0

    for i in range(n):
        x = random.uniform(0, a)
        y = random.uniform(0, a)

        if(math.sqrt((x - r)**2 + (y - r)**2) <= r): # Pythagorean identity
            n_c += 1

    return (4 * n_c)/n

vals = []

for i in range(1,10):
    val = monteCarloPi(1000,i*100)
    vals.append(val)

plt.plot(range(1,10),vals)
plt.show()
