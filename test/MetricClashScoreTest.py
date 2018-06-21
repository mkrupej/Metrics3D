import unittest
from Metrics3D import Metrics3D


class MetricClashScoreTest(unittest.TestCase):

    metric = Metrics3D()

    def test_clash_score_without_sphere(self):

        clash_score_result = self.metric.clash_score('pdb/pdb1ehz.ent', distance=5)

        self.assertEqual(clash_score_result, 23890)

    def test_clash_score_with_sphere(self):

        clash_score_result = self.metric.clash_score('pdb/pdb1ehz.ent', distance=5, residue_seq_id=56, radius=10)

        self.assertEqual(clash_score_result, 1053)