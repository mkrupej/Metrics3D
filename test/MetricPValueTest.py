import unittest
from Metrics3D import Metrics3D


class MetricPValueTest(unittest.TestCase):

    metric = Metrics3D()

    def test_p_value_case_1(self):

        p_value_result = self.metric.p_value('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent')

        self.assertEqual(round(p_value_result, 3), 0.074)

    def test_p_value_case_1_with_sphere(self, residue_seq_id=56, radius=50):

        p_value_result = self.metric.p_value('pdb/pdb4tna.ent', 'pdb/pdb4tra.ent', residue_seq_id, radius)

        self.assertEqual(round(p_value_result, 3), 0.326)

    def test_p_value_case_2(self):

        p_value_result = self.metric.p_value('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')

        self.assertEqual(round(p_value_result, 2), 0.11)