import wget
import os
import csv
import logging


class BasePairLoader(object):

    def __init__(self):
        self.BASE_PAIR_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/basepairs/csv"
        self.BASE_STACKING_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/stacking/csv"

    def retrieve_base_pair(self, pdb_id_list):
        for pdb_id in pdb_id_list:
            save_path = "base_pair/{}".format(pdb_id)
            download_path = self.BASE_PAIR_CALCULATOR.format(pdb_id)

            self.download_file(save_path, download_path)

    def retrieve_stacking(self, pdb_id_list):
        for pdb_id in pdb_id_list:
            save_path = "base_stacking/{}".format(pdb_id)
            download_path = self.BASE_STACKING_CALCULATOR.format(pdb_id)

            self.download_file(save_path, download_path)

    @staticmethod
    def download_file(save_path, download_path):
        if not os.path.exists(save_path):
            wget.download(save_path, download_path)
        else:
            logging.info('File exists: {}'.format(save_path))

class BasePair(object):

    def __init__(self, pdb_id):
        self.pdb_id = pdb_id
        PAIR = "base_pair/{}"
        STACKING = "base_stacking/{}"

        self.base_pairs = None
        self.base_stacking = None

    def clear(self):
        self.base_stacking = None
        self.base_pairs = None

    def extract_pairs(self):
        self.clear()
        self.base_pairs = self.extract_alignment("PAIR")

    def extract_stacking(self):
        self.clear()
        self.base_stacking = self.extract_alignment("STACKING")

    def extract_alignment(self, type):

        alignment = []

        pair = {'a_model' : None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        if type is "PAIR":
            file = self.PAIR.format(self.pdb_id)

        elif type is "STACKING":
            file = self.STACKING.format(self.pdb_id)

        with open(file) as csv_file:
                line_reader = csv.reader(csv_file, delimiter='|', quotechar = " ")
                for line in line_reader:
                    pair['a_model'] = line[1]
                    pair['a_chain'] = line[2]
                    pair['a_compound'] = line[3]
                    pair['a_number'] = line[4].split('"')[0]
                    pair['b_model'] = line[5]
                    pair['b_chain'] = line[6]
                    pair['b_compound'] =line[7]
                    pair['b_number'] = line[8][:-1]
                    pair['interaction'] = line[4].split('"')[2]
                    alignment.append(pair)

        return alignment