"""
Calculates p-value metric
"""
from numpy import sqrt
import scipy.special as scipy


class MetricsPValue(object):

    def __init__(self):
        pass

    def set_parameters(self, length, RMSD, mean, std):
        """

        :param length: RNA length
        :param RMSD: RMSD result
        :param mean: mean from set of pairs in RMSD
        :param std: std from set of pairs in RMSD
        :return:
        """
        self.length = length
        self.RMSD = RMSD
        self.mean = mean
        self.std = std

    def calculate_z_value(self):
        """
        Calculates z_value
        :return: z_value
        """
        return (self.RMSD - self.mean) / self.std

    def calculate_p_value(self):
        """
        Calculates p_value
        :return: p_value
        """
        return (1 + scipy.erf(self.calculate_z_value() / sqrt(2))) / 2
