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
#        self.metric_rmsd = MetricsRMSD()
        self.metric_inf = MetricsInf()
        self.metric_clash_score = MetricClashScore()
        self.metric_p_value = MetricsPValue()

    def clash_score(self, pdb_path, distance, sphere=None):

        atoms = self.pdb_loader.get_atoms(pdb_path)

        filtered_atoms = filter_atoms(atoms, sphere)

        self.metric_clash_score.set_distance(distance)
        return self.metric_clash_score.calculate_clash_score(filtered_atoms)

    def di(self, first_pdb_path, second_pdb_path, sphere=None):
        rmsd_result = self.rmsd(first_pdb_path, second_pdb_path, sphere=sphere)
        inf_result = self.inf(first_pdb_path, second_pdb_path, sphere=sphere)

        return rmsd_result / inf_result

    def rmsd(self, first_pdb_path, second_pdb_path, sphere=None):

        reference_residues = self.pdb_loader.get_residue(first_pdb_path)
        model_residues = self.pdb_loader.get_residue(second_pdb_path)

        filtered_reference, filtered_model = filter_intersection_atoms(reference_residues, model_residues, sphere)

        self.metric_rmsd.set(filtered_reference, filtered_model)
        self.metric_rmsd.run_svd()

        return self.metric_rmsd.calculate_rms()

    def inf(self, first_pdb_path, second_pdb_path, first_mcannotate_path = None, second_mcannotate_path=None
            , bp_type='all', sphere=None):

        if bp_type == 'all pairs':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_all_pairs(first_pdb_path, second_pdb_path, first_mcannotate_path, second_mcannotate_path, second_mcannotate_path)
        elif bp_type == 'wc':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_wc(first_pdb_path, second_pdb_path, first_mcannotate_path, second_mcannotate_path)
        elif bp_type == 'nWc':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_nwc(first_pdb_path, second_pdb_path, first_mcannotate_path, second_mcannotate_path)
        elif bp_type == 'stacking':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_stacking(first_pdb_path, second_pdb_path, first_mcannotate_path, second_mcannotate_path)
        elif bp_type == 'all':
            first_base_pairs, second_base_pairs = self.base_pair_loader.get_all(first_pdb_path, second_pdb_path, first_mcannotate_path, second_mcannotate_path)
        else:
            raise ValueError("Unsupported bp_type. Use all pairs, wc, nWc, stacking or all")

        first_residue = self.pdb_loader.get_residue_as_map(first_pdb_path)
        second_residue = self.pdb_loader.get_residue_as_map(second_pdb_path)

        filtered_first_base_pairs = filter_base_pairs(first_base_pairs, sphere, first_residue)
        filtered_second_base_pairs = filter_base_pairs(second_base_pairs, sphere, second_residue)

        self.metric_inf.set(filtered_first_base_pairs, filtered_second_base_pairs)
        return self.metric_inf.calculate_inf()

    def p_value(self, first_pdb_path, second_pdb_path, sphere=None):

        reference_residues = self.pdb_loader.get_residue(first_pdb_path)
        model_residues = self.pdb_loader.get_residue(second_pdb_path)
        filtered_reference, filtered_model = filter_intersection_atoms(reference_residues, model_residues, sphere)

        self.metric_rmsd.set(filtered_reference, filtered_model)
        self.metric_rmsd.run_svd()

        rmsd = self.metric_rmsd.calculate_rms()
        len = self.pdb_loader.get_length(first_pdb_path)
        mean = self.metric_rmsd.calculate_mean()
        std = self.metric_rmsd.calculate_std()
        #print("rmsd: {}, len: {}, mean: {}, std: {}".format(rmsd, len, mean, std))
        self.metric_p_value.set_parameters(len, rmsd, mean, std)
        return self.metric_p_value.calculate_p_value()


class Metric3DPdbId(object):

    def __init__(self):
        self.metric = Metrics3D()
        self.pdb_loader = PDBLoader()

    def clash_score(self, pdb_id, distance, sphere=None):

        self.pdb_loader.retrieve_pdb_file(pdb_id)

        return self.metric.clash_score('pdb/pdb{}.ent'.format(pdb_id), distance, sphere)

    def rmsd(self, first_pdb_id, second_pdb_id, sphere=None):

        self.pdb_loader.retrieve_pdb_file(first_pdb_id)
        self.pdb_loader.retrieve_pdb_file(second_pdb_id)

        return self.metric.rmsd('pdb/pdb{}.ent'.format(first_pdb_id), 'pdb/pdb{}.ent'.format(second_pdb_id), sphere)


