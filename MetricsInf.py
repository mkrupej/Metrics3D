import numpy


class MetricsInf(object):

    MCC = 0
    PPV = 0
    STY = 0
    TP = 0
    FP = 0
    FN = 0

    def __init__(self):
        self.pdb_id_a = None
        self.pdb_id_b = None

    def clear(self):
        self.pdb_id_a = None
        self.pdb_id_b = None

    def set(self, pdb_id_a, pdb_id_b):
        self.clear()
        self.pdb_id_a = pdb_id_a
        self.pdb_id_b = pdb_id_b

    def run_wc(self):
        self.run()
        pass

    def run_none_wc(self):
        self.run()
        pass

    def run_stacking(self):
        self.run()
        pass

    def run_all(self):
        self.run()
        pass

    def run(self):
        pass

    def get_from_wc(self):
        pass

    def get_from_non_wc(self):
        pass

    def get_from_stacking(self):
        pass

    def get_from_all(self):
        pass