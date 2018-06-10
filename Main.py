from Metrics3D import Metrics3D
import time
import itertools

metric = Metrics3D()

startTime = time.time()
print(metric.clash_score('pdb/pdb1evv.ent', distance=2))
elapsedTime = time.time() - startTime

print(elapsedTime)

print(len(list(itertools.product([1,2,3,4], ['A', 'B', 'C', 'D']))))