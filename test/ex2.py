import math

circle = float(input('please input area of circle'))
square = float(input('please input area of square'))

r = math.sqrt(circle/math.pi)
side = math.sqrt(square)

if 2 * r < side:
    print('ok')
else:
    print('not ok')
