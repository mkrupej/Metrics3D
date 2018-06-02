from loader.PDBLoader import *
from helper.PDBHelper import *

loader = PDBLoader()

first_structure = loader.get_atoms('1EHZ')
second_structure = loader.get_atoms('1EVV')

res1 = loader.parse_structure('1EHZ').get_residues()
res2 = loader.parse_structure('1EVV').get_residues()

for x, y in zip(res1, res2):
    print(x.get_id(), y.get_id())

print(len(get_intersection(first_structure, second_structure)))