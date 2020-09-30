import math

sin = math.sin
pi  = math.pi
n = int(input())

for i in range(n):
    x = float(i) / (n-1) * 2 * pi
    print(sin(x))
