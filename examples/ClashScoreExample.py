from Metrics3D import Metrics3D

metric = Metrics3D()

print(metric.clash_score('pdb/pdb1ehz.ent', distance=5))

print(metric.clash_score('pdb/pdb1ehz.ent', distance=5, residue_seq_id=56, radius=10))
