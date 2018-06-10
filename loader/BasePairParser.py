"""
Module responsible for parsing file containing base pair / base stacking alignment
"""
import copy
import csv


class BasePairParser(object):

    def __init__(self, base_pair_path, base_stacking_path):
        """
        Initialize - path to downloaded base_pair / base_stacking files
        :param self:
        :return:
        """
        self.PAIR = base_pair_path
        self.STACKING = base_stacking_path

    def extract_stacking(self, pdb_id):
        """
        Returns extracted stacking alignment as list for given pdb_id
        :param pdb_id:
        :return: stacking alignment as BasePair objcets
        """
        file = self.STACKING.format(pdb_id)
        return BaseStacking(self.extract_alignment(file=file))

    def extract_pair(self, pdb_id):
        """
        Returns extracted base pair alignment as list for given pdb_id
        :param pdb_id:
        :return: base pair alignment BasePair object
        """
        file = self.PAIR.format(pdb_id)
        return BasePair(self.extract_alignment(file=file))

    @staticmethod
    def extract_alignment(file):
        """
        Extracts alignment from given file. Saves each pair in dictionary called pair
        :param file: path to file which is processed
        :return: List of pair dictionaries
        """
        alignment = []

        pair = {'a_model': None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        with open(file) as csv_file:
                line_reader = csv.reader(csv_file, delimiter='|', quotechar=" ")

                for line in line_reader:
                    pair['a_model'] = line[1]
                    pair['a_chain'] = line[2]
                    pair['a_compound'] = line[3]
                    pair['a_number'] = line[4].split('"')[0]
                    pair['b_model'] = line[5]
                    pair['b_chain'] = line[6]
                    pair['b_compound'] = line[7]
                    pair['b_number'] = line[8][:-1]
                    pair['interaction'] = line[4].split('"')[2]
                    alignment.append(copy.deepcopy(pair))
                    pair.clear()

        return alignment


class BasePair(object):

    watson_crick = ["cWW", "tWW", "cWH", "tWH", "cWS", "tWS"]

    def __init__(self, alignment):
        """
        Initialized with given BasePairParser alignment
        :param alignment:
        """
        self.alignment = alignment

    def get_all_pairs(self):
        """
        Get all base pairs
        :return: returns all base pairs as list of dictionaries
        """
        return self.alignment

    def get_wc_pairs(self):
        """
        Get Watson Crick pairs
        :return: returns all watson crick pairs filtered from the whole alignment as a list of dictionaries
        """
        return [pair for pair in self.alignment if pair['interaction'] in self.watson_crick]

    def get_nwc_pairs(self):
        """
        Get non Watson Crick pairs
        :return: returns all non watson crick pairs filtered from the whole alignment as a list of dictionaries
        """
        return [pair for pair in self.alignment if pair not in self.get_wc_pairs()]


class BaseStacking(object):

    def __init__(self, alignment):
        """
        Initialized with given BasePairParser alignment
        :param alignment:
        """
        self.alignment = alignment

    def get_stacking(self):
        """
        Get non base stacking alignment
        :return: returns all stacking alignment as a list of dictionaries
        """
        return self.alignment
