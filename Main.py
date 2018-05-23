from Bio.SVDSuperimposer import SVDSuperimposer

from Sphere import *
from PDBLoader import *
import Bio.PDB
import numpy
from MetricsRMSD import *

point = Point(1, 2, 3)

sphere = Sphere(point, 6)

loader = PDBLoader()

x = loader.get_atom_array(pdb_id='1EHZ')
y = loader.get_atom_array(pdb_id='1EVV')

print(len(x))
print(len(y))

sup = SVDSuperimposer()

# x = numpy.array([[51.65, -1.90, 50.07],[50.40, -1.23, 50.65],[50.68, -0.04, 51.54],[50.22, -0.02, 52.85]], 'f')
# y = numpy.array([[51.30, -2.99, 46.54],[51.09, -1.88, 47.58],[52.36, -1.20, 48.03],[52.71, -1.18, 49.38]], 'f')

sup.set(x, y)
sup.run()
print(sup.get_rms())

my_sup = MetricsRMSD()

my_sup.set(x, y)
my_sup.run_svd()
print(my_sup.get_rms())
