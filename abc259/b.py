import numpy as np
import math
from math import cos, sin

a, b, d = map(int, input().split())
d = math.radians(d)
x = np.array([a, b])
m = np.array([[cos(d), sin(d)], [-sin(d), cos(d)]])

x = list(np.dot(x, m))
print(*x)