from math import sqrt


class MetricsInf(object):

    def __init__(self):
        self.model_pairs = None
        self.reference_pairs = None
        self.mcc = 0

    def clear(self):
        self.model_pairs = None
        self.reference_pairs = None
        self.mcc = 0

    def set(self, model_pairs, reference_pairs):
        self.clear()
        self.model_pairs = model_pairs
        self.reference_pairs = reference_pairs

    def run(self):
        tp, fp, fn = self.compare_pairs()
        ppv = tp / (tp + fp)
        sty = tp / (tp + fn)
        self.mcc = round(sqrt(ppv * sty), 2)

    @staticmethod
    def extract_significant_values_from_pair(pair):
        return pair["a_compound"], pair["a_number"], pair["b_compound"], pair["b_number"]

    def get_extracted_pair_set(self, pair_set):
        pair_set_extracted = []
        for pair in pair_set:
            pair_set_extracted.append(self.extract_significant_values_from_pair(pair))
        return pair_set_extracted

    def compare_pairs(self):

        model = self.get_extracted_pair_set(self.model_pairs)
        reference = self.get_extracted_pair_set(self.reference_pairs)

        intersection = [pair for pair in reference if pair in model]

        tp = len(intersection)
        fp = len(list(pair for pair in model if pair not in intersection))
        fn = len(list(pair for pair in reference if pair not in intersection))

        return tp, fp, fn

    def get_inf_value(self):
        return self.mcc


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
#         {'a_model': '1', 'a_chain': 'A', 'a_compound': 'G', 'a_number': '71', 'b_model': '1', 'b_chain': 'A',
#          'b_compound': 'D', 'b_number': '2', 'interaction': 'cWW'},
#
#     ]
# )
#
# print(metric.compare_pairs())
# metric.run()
# print(metric.mcc)
#
# # metric.extract_values_from_pair_set(metric.model_pairs)
# #
# # print(metric.extract_values_from_pair_set(metric.model_pairs))