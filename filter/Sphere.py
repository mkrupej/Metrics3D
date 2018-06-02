class Sphere(object):

    def __init__(self, center, radius):
        self.c = center
        self.r = radius

    def __contains__(self, p):
        if (p[0]-self.c[0]) ^ 2 + (p[1]-self.c[1]) ^ 2 + (p[2]-self.c[2]) ^ 2 < self.r ^ 2:
            return True
        else:
            return False
