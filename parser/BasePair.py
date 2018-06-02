import wget
import os
import csv
import logging
from loader.PDBLoader import *


class BasePair(object):

    watson_crick = ["cWW", "tWW", "cWH", "tWH", "cWS", "tWS"]

    def __init__(self, pdb_id):
        self.loader = PDBLoader()
        self.pdb_id = pdb_id
        self.PAIR = "base_pair/{}"
        self.STACKING = "base_stacking/{}"

        self.base_pairs_all = None
        self.base_pairs_wc = None
        self.base_pairs_nwc = None
        self.base_stacking = None

        self.types = {"stacking": self.base_stacking, "all": self.base_pairs_all, "wc": self.base_pairs_wc, "nwc": self.base_pairs_nwc}

    def clear(self, type):
        self.types[type] = None

    def extract_all_pairs(self):
        self.clear("all")
        self.base_pairs_all = self.extract_alignment("PAIR")

    def extract_wc_pairs(self):
        self.clear("wc")
        self.base_pairs_wc = self.extract_alignment("PAIR", "WC")

    def extract_nwc_pairs(self):
        self.clear("nwc")
        self.base_pairs_nwc = self.extract_alignment("PAIR", "nWC")

    def extract_stacking(self):
        self.clear("stacking")
        self.base_stacking = self.extract_alignment("STACKING")

    def extract_alignment(self, type, subtype=None):

        residues = self.loader.parse_structure(self.pdb_id)

        def get_residues_by_seq(seq):
            return [r for r in residues if r.get_id()[1]==seq]

        alignment = []

        pair = {'a_model' : None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        subtypes = {'WC': None, "nWC": None}

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
                    pair['a_number'] = get_residues_by_seq(line[4].split('"')[0])
                    pair['b_model'] = line[5]
                    pair['b_chain'] = line[6]
                    pair['b_compound'] = line[7]
                    pair['b_number'] = get_residues_by_seq(line[8][:-1])
                    pair['interaction'] = line[4].split('"')[2]

                    if subtype == None:
                        alignment.append(pair)

                    elif subtype == "WC":
                        if pair['interaction'] in self.watson_crick:
                            #print(pair)
                            alignment.append(pair)
                            print(alignment)

                    elif subtype == "nWC":
                        if pair['interaction'] not in self.watson_crick:
                            alignment.append(pair)

                    pair.clear()
        return alignment

    def get_all(self, sphere=None):
        return self.base_pairs_all

    def get_wc_pairs(self):
        return self.base_pairs_wc

    def get_nwc_pairs(self):
        return self.base_pairs_nwc

    def get_stacking(self):
        return self.base_stacking


