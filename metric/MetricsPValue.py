import numpy
from numpy import sqrt
import scipy.special as scipy


class MetricsPValue(object):

    def __init__(self):
        self.length_rna = None
        self.RMSD = None

    def set_parameters(self, length, RMSD):
        self.length = length
        self.RMSD = RMSD

    def mean(self):
        #tbd
        return 2

    def std(self):
        #tbd
        return 2

    def calculate_z_value(self):
        return (self.RMSD - self.mean()) / self.std()

    def calculate_p_value(self):
        return ((1 + scipy.erf(self.calculate_z_value() / sqrt(2))) / 2)


# a = MetricsPValue()
# a.set_parameters(50, 20)
#
# print(a.calculate_p_value())