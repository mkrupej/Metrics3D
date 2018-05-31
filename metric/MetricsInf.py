import numpy


class MetricsInf(object):

    variables = {"MCC" : None, "PPV": None, "STY": None, "TP": None, "FP": None, "FN": None}

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