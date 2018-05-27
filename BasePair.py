from Bio.PDB import *
import numpy
import wget
import os
import csv
import re


BASE_PAIR_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/basepairs/csv"
BASE_STACKING_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/stacking/csv"


class BasePairLoader(object):

    def __init__(self, pdb_id_list):

        self.pdb_id_list = pdb_id_list
        self.retrieve_base_pair_and_stacking()

    def retrieve_base_pair_and_stacking(self):

        for pdb_id in self.pdb_id_list:
            save_path_base_pair = "base_pair/{}".format(pdb_id)
            download_path_base_pair = BASE_PAIR_CALCULATOR.format(pdb_id)

            save_path_base_stacking = "base_stacking/{}".format(pdb_id)
            download_path_base_stacking = BASE_STACKING_CALCULATOR.format(pdb_id)

            if not os.path.exists(save_path_base_pair): #jesli plik istnieje pomin pobieranie
                wget.download(download_path_base_pair, save_path_base_pair)

            if not os.path.exists(save_path_base_stacking):
                wget.download(download_path_base_stacking, save_path_base_stacking)


class BasePair(object):

    def __init__(self, pdb_id):
        self.pdb_id = pdb_id
        self.base_pairs = self.extract_pairs()
        self.base_stacking = self.extract_stacking()

    def extract_pairs(self):
        return self.extract_alignment("PAIR")

    def extract_stacking(self):
        return self.extract_alignment("STACKING")

    def extract_alignment(self, type):

        PAIR = "base_pair/{}"
        STACKING = "base_stacking/{}"

        alignment = []

        pair = {'a_model' : None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        if type is "PAIR":
            file = PAIR.format(self.pdb_id)

        elif type is "STACKING":
            file = STACKING.format(self.pdb_id)

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



pdblist = ["1EHZ", "1EVV"]
a = BasePairLoader(pdblist)

b = BasePair("1EVV")
#print(b.base_pairs)
print(b.base_stacking)