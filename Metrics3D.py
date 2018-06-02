from loader.PDBLoader import *
from metric.MetricsRMSD import *
from filter.SphereFilter import *


class Metrics3D(object):

    def __init__(self):
        self.loader = PDBLoader()
        self.metric_rmsd = MetricsRMSD()

    def rmsd(self, first_pdb_id, second_pdb_id, sphere=None):

        reference_residues = self.loader.get_residue(first_pdb_id)
        model_residues = self.loader.get_residue(second_pdb_id)

        filtered_reference, filtered_model = filter_intersection_atoms(reference_residues, model_residues, sphere)

        self.metric_rmsd.set(filtered_reference, filtered_model)
        self.metric_rmsd.run_svd()

        return self.metric_rmsd.get_rms()
