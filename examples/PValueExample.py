from Metrics3D import Metrics3D

metric = Metrics3D()

print(metric.p_value('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent'))

print(metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent'))

print(metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=100))