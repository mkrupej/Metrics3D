from loader.PDBLoader import *
from metric.MetricsRMSD import *
from metric.MetricClashScore import *
from filter.SphereFilter import *


class Metrics3D(object):

    def __init__(self):
        self.loader = PDBLoader()
        self.metric_rmsd = MetricsRMSD()
        self.metric_clash_score = MetricClashScore()

    def rmsd(self, first_pdb_id, second_pdb_id, sphere=None):

        reference_residues = self.loader.get_residue(first_pdb_id)
        model_residues = self.loader.get_residue(second_pdb_id)

        filtered_reference, filtered_model = filter_intersection_atoms(reference_residues, model_residues, sphere)

        self.metric_rmsd.set(filtered_reference, filtered_model)
        self.metric_rmsd.run_svd()

        return self.metric_rmsd.calculate_rms()

    def clash_score(self, pdb_id, distance, sphere=None):

        atoms = self.loader.get_atoms(pdb_id)

        filtered_atoms = filter_atoms(atoms, sphere)

        self.metric_clash_score.set_distance(distance)

        return self.metric_clash_score.calculate_clash_score(filtered_atoms)
