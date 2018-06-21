"""
Calculates Clash Score metric
"""
import itertools


class MetricClashScore(object):

    def __init__(self):
        self.distance = None

    def set_distance(self, distance):
        """

        :param distance: distance between atoms in clash score
        """
        self.distance = distance

    def calculate_clash_score(self, model_atoms):
        """

        :param model_atoms: list of atoms
        :return: the number of atoms that meet the clash score condition
        """
        all_permutation = list(itertools.combinations(model_atoms, 2))

        calculate_distance = map(lambda x: self.check_distance(x[0], x[1]), all_permutation)

        filter_clash_score = list(filter(lambda x: x is True, calculate_distance))

        return len(filter_clash_score)

    def check_distance(self, atom1, atom2):
        """

        :param atom1:
        :param atom2:
        :return: true if distance between atoms is small than clash score distance
        """
        if atom1 - atom2 < self.distance:
            return True
        else:
            return False
