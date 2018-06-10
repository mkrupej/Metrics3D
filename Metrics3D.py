from loader.PDBLoader import *
from loader.BasePairLoader import *
from metric.MetricsRMSD import *
from metric.MetricClashScore import *
from filter.SphereFilter import *
from metric.MetricInf import *
from metric.MetricsPValue import *

class Metrics3D(object):

    def __init__(self):
        self.pdb_loader = PDBLoader()
        self.base_pair_loader = BasePairLoader()
        self.metric_rmsd = MetricsRMSD.MetricsRMSD()
        self.metric_inf = MetricsInf()
        self.metric_clash_score = MetricClashScore()
        self.metric_p_value = MetricsPValue()

    def clash_score(self, pdb_id, distance, sphere=None):

        atoms = self.pdb_loader.get_atoms(pdb_id)

        filtered_atoms = filter_atoms(atoms, sphere)

        self.metric_clash_score.set_distance(distance)
        return self.metric_clash_score.calculate_clash_score(filtered_atoms)

    def di(self, first_pdb_id, second_pdb_id, sphere=None):
        rmsd_result = self.rmsd(first_pdb_id, second_pdb_id, sphere=sphere)
        inf_result = self.inf(first_pdb_id, second_pdb_id, sphere=sphere)

        return rmsd_result / inf_result

    def rmsd(self, first_pdb_id, second_pdb_id, sphere=None):

        reference_residues = self.pdb_loader.get_residue(first_pdb_id)
        model_residues = self.pdb_loader.get_residue(second_pdb_id)

        filtered_reference, filtered_model = filter_intersection_atoms(reference_residues, model_residues, sphere)

        self.metric_rmsd.set(filtered_reference, filtered_model)
        self.metric_rmsd.run_svd()

        return self.metric_rmsd.calculate_rms()

    def inf(self, first_pdb_id, second_pdb_id, bp_type='all', sphere=None):

        if bp_type == 'all':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_all(first_pdb_id, second_pdb_id)
        elif bp_type == 'wc':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_wc(first_pdb_id, second_pdb_id)
        elif bp_type == 'nWc':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_nwc(first_pdb_id, second_pdb_id)
        elif bp_type == 'stacking':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_stacking(first_pdb_id, second_pdb_id)
        else:
            raise ValueError("Unsupported bp_type. Use all, wc, nWc, or stacking")

        first_residue = self.pdb_loader.get_residue_as_map(first_pdb_id)
        second_residue = self.pdb_loader.get_residue_as_map(second_pdb_id)

        filtered_first_base_pairs = filter_base_pairs(first_base_pairs, sphere, first_residue)
        filtered_second_base_pairs = filter_base_pairs(second_base_pairs, sphere, second_residue)

        self.metric_inf.set(filtered_first_base_pairs, filtered_second_base_pairs)
        return self.metric_inf.calculate_inf()

    def p_value(self, first_pdb_id, second_pdb_id, sphere=None):

        rmsd = self.rmsd(first_pdb_id, second_pdb_id, sphere)
        len = self.pdb_loader.get_length(first_pdb_id)

        self.metric_p_value.set_parameters(len, rmsd)
        return self.metric_p_value.calculate_p_value()
