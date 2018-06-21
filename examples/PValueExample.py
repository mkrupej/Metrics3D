from Metrics3D import Metrics3D
from loader.PDBLoader import *

metric = Metrics3D()

pdb_loader = PDBLoader()

print(metric.p_value('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent'))

print(metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))