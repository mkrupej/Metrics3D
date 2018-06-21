from Metrics3D import Metrics3D

metric = Metrics3D()

print(metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))

print(metric.di('pdb/pdb4tra.ent', 'pdb/pdb6tna.ent'))

print(metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=100))

print(metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=1000))