from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['x', 'y', 'r'])

p = Point(1,2)
print p.x
print p.y

c = Circle(1,1,1)
print c.x
print c.y
print c.r
