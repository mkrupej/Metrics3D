from numpy import sqrt
import scipy.special as scipy


class MetricsPValue(object):

    def __init__(self):
        self.length_rna = None
        self.RMSD = None

    def set_parameters(self, length, RMSD, mean, std):
        self.length = length
        self.RMSD = RMSD
        self.mean = mean
        self.std = std

    def calculate_z_value(self):
        return (self.RMSD - self.mean) / self.std

    def calculate_p_value(self):
        return ((1 + scipy.erf(self.calculate_z_value() / sqrt(2))) / 2)
