import unittest
from Metrics3D import Metrics3D


class MetricRMSDTest(unittest.TestCase):

    metric = Metrics3D()

    def test_rmsd_without_sphere(self):

        rmsd_result = self.metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent')

        self.assertEqual(round(rmsd_result, 2), 1.69)

    def test_rmsd_with_sphere(self):

        rmsd_result = self.metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=100)

        self.assertEqual(round(rmsd_result, 2), 1.02)

    def test_rmsd_with_sphere_full(self):

        rmsd_result = self.metric.rmsd('pdb/pdb1ehz.ent', 'pdb/pdb1evv.ent', residue_seq_id=56, radius=1000)

        self.assertEqual(round(rmsd_result, 2), 1.69)