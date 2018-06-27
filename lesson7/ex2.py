class Point:
    x = 1
    y = 2

class A:
    pass


class B(A):
    pass


point_1 = Point
point_2 = Point
point_1.z = 5

print(point_1.z, point_1.x)