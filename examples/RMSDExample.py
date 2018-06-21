from Metrics3D import Metrics3D

metric = Metrics3D()

print(metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))

print(metric.rmsd('pdb/pdb4tra.ent', 'pdb/pdb6tna.ent'))