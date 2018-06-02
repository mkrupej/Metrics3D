from loader.PDBLoader import *
from metric.MetricsRMSD import *


class Metrics3D(object):

    def __init__(self):
        self.loader = PDBLoader()
        self.metric_rmsd = MetricsRMSD()

    def rmsd(self, first_pdb_id, second_pdb_id, sphere=None):

        first_structure = self.loader.get_atoms(first_pdb_id, sphere)
        second_structure = self.loader.get_atoms(second_pdb_id, sphere)

        intersection_residue = get_intersection(first_structure, second_structure)

        self.metric_rmsd.set(first_structure, second_structure)
        self.metric_rmsd.run_svd()

        return self.metric_rmsd.get_rms()
