from math import sqrt


class MetricsInf(object):

    def __init__(self):
        self.model_pairs = None
        self.reference_pairs = None
        self.variables = {"PPV": 0, "STY": 0, "TP": 0, "FP": 0, "FN": 0}
        self.mcc = 0

    def clear(self):
        self.model_pairs = None
        self.reference_pairs = None
        self.variables = {"PPV": 0, "STY": 0, "TP": 0, "FP": 0, "FN": 0}
        self.mcc = 0

    def set(self, trna_1_pairs, trna_2_pairs):
        self.clear()
        self.model_pairs = trna_1_pairs
        self.reference_pairs = trna_2_pairs

    def run(self):
        self.variables["TP"], self.variables["FP"], self.variables["FN"] = self.compare_pairs()
        self.variables["PPV"] = self.variables["TP"] / (self.variables["TP"] + self.variables["FP"])
        self.variables["STY"] = self.variables["TP"] / (self.variables["TP"] + self.variables["FN"])
        self.mcc = sqrt(self.variables["PPV"] * self.variables["STY"])

    @staticmethod
    def get_pair(base_pair):
        return base_pair["a_compound"], base_pair["a_number"], base_pair["b_compound"], base_pair["b_number"]

    def compare_pairs(self):
        true_positive = 0
        false_positive = 0
        false_negative = 0

        for pair_a in self.model_pairs:
            match_a = self.get_pair(pair_a)
            for pair_b in self.reference_pairs:
                match_b = self.get_pair(pair_b)
                if match_a == match_b:
                    true_positive += 1
                    break
            else:
                false_positive += 1

        for pair_b in self.reference_pairs:
            match_b = self.get_pair(pair_b)
            for pair_a in self.model_pairs:
                match_a = self.get_pair(pair_a)
                if match_b == match_a:
                    break
            else:
                false_negative += 1

        return true_positive, false_positive, false_negative

    def get_inf_value(self):
        return self.mcc

    def get_inf_metric(self):
        return self.variables, self.mcc


# metric = MetricsInf()
# metric.set([
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'A', 'a_number': '2', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'C', 'b_number': '2', 'interaction': 'cWW'},
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'B', 'a_number': '71', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'C', 'b_number': '2', 'interaction': 'cWW'},
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'C', 'a_number': '71', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'C', 'b_number': '2', 'interaction': 'cWW'},
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'D', 'a_number': '11', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'A', 'b_number': '1', 'interaction': 'cWW'},
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'G', 'a_number': '71', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'C', 'b_number': '2', 'interaction': 'cWW'},
# ]
# ,[
#  {'a_model': '1', 'a_chain': 'A', 'a_compound': 'G', 'a_number': '71', 'b_model': '1', 'b_chain': 'A', 'b_compound': 'C', 'b_number': '2', 'interaction': 'cWW'},
# ]
# )
#
# print(metric.compare_pairs())
# metric.run()
# print(metric.mcc)