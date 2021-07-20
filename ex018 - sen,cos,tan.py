import math
x = float(input('digite o angulo: '))
cos = math.cos(math.radians(x))
sen = math.sin(math.radians(x))
tan = math.tan(math.radians(x))
print(f'cosseno é {cos:.2f}\n'
      f'seno é {sen:.2f}\n'
      f'tangente é {tan:.2f}')
