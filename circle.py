from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * self.radius * pi

    @property
    def area(self):
        return pi * self.radius**2
