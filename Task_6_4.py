from math import cos, sin, atan, radians, degrees
from cmath import phase


class Point:

    def __init__(self, r=2**(1/2), phi=45.0):
        self.r = r
        self.phi = phi

    @classmethod
    def from_cartesian(cls, x, y):
        if y >= 0:
            return Point((x**2+y**2)**(1/2), degrees(phase(complex(x, y))))
        return Point((x ** 2 + y ** 2) ** (1 / 2), 360 + degrees(phase(complex(x, y))))

    def __repr__(self):
        return 'Point('+str(round(self.r, 2)) + \
                ', '+str(round(self.phi, 1)) + ')'

    def __str__(self):
        return '(r = '+str(round(self.r, 2)) + \
               ', phi = '+str(round(self.phi, 1))+')'

    def __add__(self, other):
        phi_1 = radians(self.phi)
        phi_2 = radians(other.phi)
        x1, x2 = self.r * cos(phi_1), other.r * cos(phi_2)
        y1, y2 = self.r * sin(phi_1), other.r * sin(phi_2)
        r_res = ((x1 + x2)**2 + (y1 + y2)**2)**(1/2)
        phi_res = degrees(atan((y1+y2)/(x1+x2)))
        return Point(r_res, phi_res)

    def __eq__(self, other):
        return self.phi == other.phi and self.r == other.r


p1 = Point(r=1, phi=0)
p2 = Point(r=1, phi=90)
p3 = p1 + p2
print(p3)

p = Point.from_cartesian(x=-17.5, y=0)
print(repr(p))

print(p1 == p1)
print(p1 == p2)
