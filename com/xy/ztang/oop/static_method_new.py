# -*-coding:utf-8-*-

"""
 @staticmethod 静态方法
"""
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_vaild(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_vaild(a, b, c):
        tri = Triangle(a, b, c)
        print(tri.perimeter())
        print(tri.area())
    else:
        print('can not create the triangle!')


if __name__ == '__main__':
    main()

