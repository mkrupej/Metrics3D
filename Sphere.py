class Sphere(object):

    def __init__(self, center, radius):
        self.c = center
        self.r = radius

    def __contains__(self, p):
        if (p.x-self.c.x) ^ 2 + (p.y-self.c.y) ^ 2 + (p.z-self.c.z) ^ 2 < self.r ^ 2:
            return True
        else:
            return False


class Point(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
