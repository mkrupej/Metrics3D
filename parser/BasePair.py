import copy
import wget
import os
import csv
import logging
from loader.PDBLoader import *


class BasePair(object):

    watson_crick = ["cWW", "tWW", "cWH", "tWH", "cWS", "tWS"]

    PAIR_TYPE = "PAIR"
    STACKING_TYPE = "STACKING"

    def __init__(self, pdb_id):

        self.loader = PDBLoader()
        self.pdb_id = pdb_id
        self.PAIR = "../base_pair/{}"
        self.STACKING = "../base_stacking/{}"

        self.pair_alignment = None
        self.stacking_alignment = None

    def clear(self):
        self.pair_alignment = None
        self.stacking_alignment = None

    def extract_stacking(self):
        file = self.STACKING.format(self.pdb_id)
        self.stacking_alignment = self.extract_alignment(file= file)

    def extract_pair(self):
        file = self.PAIR.format(self.pdb_id)
        self.pair_alignment = self.extract_alignment(file= file)

    def extract_alignment(self, file):

        residues = self.loader.parse_structure(self.pdb_id)

        def get_residues_by_seq(seq):
            return [r for r in residues if r.get_id()[1] == seq]

        alignment = []

        pair = {'a_model': None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        with open(file) as csv_file:
                line_reader = csv.reader(csv_file, delimiter='|', quotechar= " ")

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

    def get_all_pairs(self, sphere=None):
        return self.pair_alignment

    def get_wc_pairs(self):
        return [pair for pair in self.pair_alignment if pair['interaction'] in self.watson_crick]

    def get_nwc_pairs(self):
        return [pair for pair in self.pair_alignment if pair not in self.get_wc_pairs()]

    def get_stacking(self):
        return self.stacking_alignment


a = BasePair("1EHZ")

a.extract_pair()
print(a.get_all_pairs())
print(len(a.get_all_pairs()))

print(a.get_wc_pairs())
print(len(a.get_wc_pairs()))
print((a.get_nwc_pairs()))

a.extract_stacking()
print(a.get_stacking())
print(len(a.get_stacking()))