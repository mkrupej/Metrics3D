"""
Parser responsible for parsing file containing base pair / base stacking alignment
"""
import copy
import csv
import re


class BasePairParser(object):

    def __init__(self, base_pair_path, base_stacking_path):
        """
        Initialize - path to downloaded base_pair / base_stacking files
        :param self:
        :return:
        """
        self.PAIR = base_pair_path
        self.STACKING = base_stacking_path

    def extract_stacking(self, server_pair_file=None, mc_annotate_file = None):
        """
        Returns extracted stacking alignment as list for given pdb_id
        :param pdb_file:
        :return: stacking alignment as BasePair objcets
        """
        if mc_annotate_file is None:
            file = self.STACKING.format(server_pair_file)
            return BaseStacking(self.extract_alignment_from_server_file(server_pair_file))

        else:
            return BaseStacking(self.extract_stacking_alignment_from_mc_annotate(mc_annotate_file))

    def extract_pair(self, server_pair_file=None, mc_annotate_file = None):
        """
        Returns extracted base pair alignment as list for given pdb_id
        :param pdb_id:
        :return: base pair alignment BasePair object
        """
        if mc_annotate_file is None:
            file = self.PAIR.format(server_pair_file)
            return BasePair(self.extract_alignment_from_server_file(server_pair_file))
        else:
            return BasePair(self.extract_pair_alignment_from_mc_annotate(mc_annotate_file))

    @staticmethod
    def extract_alignment_from_server_file(pair_file):
        """
        Extracts alignment from given file. Saves each pair in dictionary called pair
        :param pair_file: path to file which is processed
        :return: List of pair dictionaries
        """
        alignment = []

        pair = {'a_compound': None, 'a_number': None,
                'b_compound': None, 'b_number': None,
                'interaction': None}

        with open(pair_file) as csv_file:
                line_reader = csv.reader(csv_file, delimiter='|', quotechar=" ")

                for line in line_reader:
                    pair['a_compound'] = line[3]
                    pair['a_number'] = line[4].split('"')[0]
                    pair['b_compound'] = line[7]
                    pair['b_number'] = line[8][:-1]
                    pair['interaction'] = line[4].split('"')[2]
                    alignment.append(copy.deepcopy(pair))
                    pair.clear()

        return alignment

    @staticmethod
    def extract_pair_alignment_from_mc_annotate(file):
        """
        Extracts alignment from given file. Saves each pair in dictionary called pair
        :param file: path to file which is processed
        :return: List of pair dictionaries
        """
        alignment = []

        pair = {'a_compound': None, 'a_number': None,
                'b_compound': None, 'b_number': None,
                'interaction': None}

        ref_save = 0

        with open(file) as file_ref:
            for line_ref in file_ref:
                if "Base-pairs" in line_ref:
                    ref_save = 1
                elif ref_save:
                    pair['a_compound'] = re.findall('[A-Z]', line_ref )[2]
                    pair['a_number'] = re.findall('\d+', line_ref )[0]
                    pair['b_compound'] = re.findall('[A-Z]', line_ref )[3]
                    pair['b_number'] = re.findall('\d+', line_ref )[1]
                    pair['interaction'] = re.search(r'(\s(\w|\D){2,3}/(\w|\D){2,3}\s)', line_ref).group(0).strip()
                    alignment.append(copy.deepcopy(pair))
                    pair.clear()

        return alignment

    @staticmethod
    def extract_stacking_alignment_from_mc_annotate(file):
        """
        Extracts alignment from given file. Saves each pair in dictionary called pair
        :param file: path to file which is processed
        :return: List of pair dictionaries
        """
        alignment = []

        pair = {'a_compound': None, 'a_number': None,
                'b_compound': None, 'b_number': None,
                'interaction': None}

        ref_save = 0
        with open(file) as file_ref:
            for line_ref in file_ref:
                if not line_ref:
                    continue
                elif "Adjacent stackings" in line_ref:
                    ref_save = 1
                elif "Non-Adjacent stackings" in line_ref:
                    continue
                elif "Number of stackings" in line_ref:
                    break
                elif ref_save:
                    pair['a_compound'] = "S"
                    pair['a_number'] = re.findall('\d+', line_ref)[0]
                    pair['b_compound'] = "S"
                    #print(line_ref, pair["a_number"])
                    pair['b_number'] = re.findall('\d+', line_ref)[1]
                    pair['interaction'] = "s"
                    alignment.append(copy.deepcopy(pair))
                    pair.clear()
        return alignment


class BasePair(object):

    watson_crick = ["cWW", "tWW", "cWH", "tWH", "cWS", "tWS", "Ww/Ww", "Ww/Hh", "Ww/Ws"]

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
