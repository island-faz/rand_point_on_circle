#import matplotlib.pyplot as plt
from math import pi, cos, sin
from random import random

def rand_point(x, y, r):
    rand_angle = random() * 2 * pi
    return (x + cos(rand_angle) * r, y + sin(rand_angle) * r)

print(rand_point(0,0,10))

#xy = [rand_point(0,0,10) for _ in range(30)]

#print(xy)
#plt.scatter(*zip(*xy))
#plt.grid(color='k', linestyle=':', linewidth=1)
#plt.axes().set_aspect('equal', 'datalim')
#plt.show()