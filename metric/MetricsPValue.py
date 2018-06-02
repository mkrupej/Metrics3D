import numpy


class MetricsPValue(object):

    def __init__(self):
        self.pdb_id_a = None

    def clear(self):
        self.pdb_id_a = None

    def set(self, pdb_id_a, pdb_id_b):
        self.clear()
        self.pdb_id_a = pdb_id_a

    def run_pvalue(self):
        self.run()
        pass

    def get_pvalue(self):
        pass