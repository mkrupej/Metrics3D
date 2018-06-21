from Metrics3D import Metrics3D
from loader.PDBLoader import *

metric = Metrics3D()

pdb_loader = PDBLoader()

print(metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))

print(metric.rmsd('pdb/pdb4tra.ent', 'pdb/pdb6tna.ent'))