import unittest
from Metrics3D import Metrics3D


class MetricDITest(unittest.TestCase):

    metric = Metrics3D()

    def test_di_without_sphere(self):

        di_result = self.metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')

        self.assertEqual(round(di_result, 2), 1.70)

    def test_di_with_sphere(self):

        di_result = self.metric.di('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=100)

        self.assertEqual(round(di_result, 2), 1.04)
