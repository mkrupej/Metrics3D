import numpy
from numpy import sqrt
import scipy.special as scipy

import filter.SphereFilter
from metric import MetricsRMSD


class MetricsPValue(object):

    def __init__(self):
        self.length_rna = None
        self.RMSD = None

    def set_parameters(self, length, RMSD):
        self.length = length
        self.RMSD = RMSD

    def mean(self):
        return -.41

    def std(self):
        return 1.8 #Standard deviations are ∼1.8 ± 0.3 Å in all cases

    def calculate_z_value(self):
        return (self.RMSD - self.mean()) / self.std()

    def calculate_p_value(self):
        return ((1 + scipy.erf(self.calculate_z_value() / sqrt(2))) / 2)