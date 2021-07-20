catop = float(input('digite o cateto oposto: '))
catadj = float(input('digite o cateto adjacente: '))
from math import hypot
hip = hypot(catop,catadj)
print(f'a hipotenusa é {hip}')