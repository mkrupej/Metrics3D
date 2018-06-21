import unittest
from Metrics3D import Metrics3D


class MetricInfTest(unittest.TestCase):

    metric = Metrics3D()

    def test_inf_all(self):

        p_value_result = self.metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv')

        self.assertEqual(round(p_value_result, 4), 0.9865)

    def test_inf_all_pairs(self):

        p_value_result = self.metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv', bp_type="all pairs")

        self.assertEqual(round(p_value_result, 2), 1)

    def test_inf_wc_pairs(self):

        p_value_result = self.metric.inf('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent', 'base_pair_mcannotate/4tna', 'base_pair_mcannotate/4tra', bp_type="wc")

        self.assertEqual(round(p_value_result, 2), 0.97)

    def test_inf_nWc_pairs(self):

        p_value_result = self.metric.inf('pdb/pdb4tna.ent', 'pdb/pdb6tna.ent', 'base_pair_mcannotate/4tna', 'base_pair_mcannotate/6tna', bp_type="nWc")

        self.assertEqual(round(p_value_result, 2), 0.71)

    def test_inf_stacking_pairs(self):

        p_value_result = self.metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', 'base_pair_mcannotate/1ehz', 'base_pair_mcannotate/1evv', bp_type="stacking")

        self.assertEqual(round(p_value_result, 2), 0.98)

    def test_inf_all_pairs_without_mc_annotate_files(self):

        p_value_result = self.metric.inf('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')

        self.assertEqual(round(p_value_result, 2), 0.99)

    def test_inf_stacking_without_mc_annotate_files(self):

        p_value_result = self.metric.inf('pdb/pdb4tra.ent', 'pdb/pdb4tna.ent', bp_type="stacking")

        self.assertEqual(round(p_value_result, 2), 0.97)