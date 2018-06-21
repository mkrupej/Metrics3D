from Metrics3D import Metrics3D
from loader.PDBLoader import *

metric = Metrics3D()

pdb_loader = PDBLoader()

#domyslnie inf jest liczony dla wszystkich par i stacking
print(metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv'))

#dostepne bp_type: 'all, 'all pairs', 'wc', 'nWc', 'stacking',
print(metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv', bp_type="all pairs"))

print(metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv', bp_type="stacking"))

print(metric.inf('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent', 'base_pair_mcannotate/4tna', 'base_pair_mcannotate/4tra', bp_type="wc"))

print(metric.inf('pdb/pdb4tna.ent', 'pdb/pdb6tna.ent', 'base_pair_mcannotate/4tna', 'base_pair_mcannotate/6tna', bp_type="nWc"))


#dla zwiazkow istniejacych nie trzeba podawac pliku mc_annotate, zbior par zostanie pobrany z serwera
print(metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))

print(metric.inf('pdb/pdb4tra.ent', 'pdb/pdb4tna.ent', bp_type="wc"))

print(metric.inf('pdb/pdb4tra.ent', 'pdb/pdb4tna.ent', bp_type="stacking"))
