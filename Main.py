from Sphere import *
from PDBLoader import *

point = Point(1, 2, 3)

sphere = Sphere(point, 6)

loader = PDBLoader()

loader.get_structure('1D3Z')
loader.get_structure('1UBQ')