"""
Calculates INF metric
"""
from math import sqrt


class MetricsInf(object):

    def __init__(self):
        """
        Initialize, set model and reference pairs to None
        """
        self.model_pairs = None
        self.reference_pairs = None

    def clear(self):
        """
        Clear current model and reference pairs
        :return:
        """
        self.model_pairs = None
        self.reference_pairs = None

    def set(self, model_pairs, reference_pairs):
        """
        Set base pairs for model and reference
        :param model_pairs: base pairs from RNA A
        :param reference_pairs: base pairs from RNA B
        :return:
        """
        self.clear()
        self.model_pairs = model_pairs
        self.reference_pairs = reference_pairs

    @staticmethod
    def extract_significant_values_from_pair(pair):
        """
        Based on given pair dictionary returns significant data
        :param pair: base pair as a dictionary
        :return: significant values to further comparison
        """
        return pair["a_compound"], pair["a_number"], pair["b_compound"], pair["b_number"]

    def get_extracted_pair_set(self, pair_set):
        return [self.extract_significant_values_from_pair(e) for e in pair_set]

    def calculate_inf(self):

        model = self.get_extracted_pair_set(self.model_pairs)
        reference = self.get_extracted_pair_set(self.reference_pairs)

        intersection = [pair for pair in reference if pair in model]

        tp = len(intersection)
        fp = len(list(pair for pair in model if pair not in intersection))
        fn = len(list(pair for pair in reference if pair not in intersection))

        ppv = tp / (tp + fp)

        sty = tp / (tp + fn)

        return sqrt(ppv * sty)