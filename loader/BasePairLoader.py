import wget
import os
from loader.BasePairParser import *


class BasePairLoader(object):

    BASE_PAIR_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/basepairs/csv"
    BASE_STACKING_CALCULATOR = "http://rna.bgsu.edu/rna3dhub/pdb/{}/interactions/fr3d/stacking/csv"

    SAVE_PATH_PAIR = "base_pair/{}"
    SAVE_PATH_STACKING = "base_stacking/{}"

    def __init__(self):
        self.parser = BasePairParser(self.SAVE_PATH_PAIR, self.SAVE_PATH_STACKING)

    def retrieve_base_pair(self, pdb_id_list):
        if not os.path.exists(self.SAVE_PATH_PAIR.format("")):
            os.makedirs("base_pair")

        for pdb_id in pdb_id_list:
            save_path = self.SAVE_PATH_PAIR.format(pdb_id)
            download_path = self.BASE_PAIR_CALCULATOR.format(pdb_id)

            self.download_file(download_path, save_path)

    def retrieve_stacking(self, pdb_id_list):
        if not os.path.exists(self.SAVE_PATH_STACKING.format("")):
            os.makedirs("base_stacking")

        for pdb_id in pdb_id_list:
            save_path = self.SAVE_PATH_STACKING.format(pdb_id)
            download_path = self.BASE_STACKING_CALCULATOR.format(pdb_id)

            self.download_file(download_path, save_path)

    @staticmethod
    def download_file(download_path, save_path):
        if not os.path.exists(save_path):
            wget.download(download_path, save_path)
        else:
            print('File exists: {}'.format(save_path))

    def get_all_pairs(self, first_pdb_id, second_pdb_id):
        self.retrieve_base_pair([first_pdb_id, second_pdb_id])
        first_result = self.parser.extract_pair(first_pdb_id).get_all_pairs()
        print(len(first_result))

        second_result = self.parser.extract_pair(second_pdb_id).get_all_pairs()
        print(len(second_result))

        return first_result, second_result

    def get_wc(self, first_pdb_id, second_pdb_id):
        self.retrieve_base_pair([first_pdb_id, second_pdb_id])
        first_result = self.parser.extract_pair(first_pdb_id).get_wc_pairs()
        second_result = self.parser.extract_pair(second_pdb_id).get_wc_pairs()
        return first_result, second_result

    def get_nwc(self, first_pdb_id, second_pdb_id):
        self.retrieve_base_pair([first_pdb_id, second_pdb_id])
        first_result = self.parser.extract_pair(first_pdb_id).get_nwc_pairs()
        second_result = self.parser.extract_pair(second_pdb_id).get_nwc_pairs()
        return first_result, second_result

    def get_stacking(self, first_pdb_id, second_pdb_id):
        self.retrieve_stacking([first_pdb_id, second_pdb_id])
        first_result = self.parser.extract_stacking(first_pdb_id).get_stacking()
        second_result = self.parser.extract_stacking(second_pdb_id).get_stacking()
        return first_result, second_result

    def get_all(self, first_pdb_id, second_pdb_id):
        self.retrieve_base_pair([first_pdb_id, second_pdb_id])
        self.retrieve_stacking([first_pdb_id, second_pdb_id])
        first_result_stacking = self.parser.extract_stacking(first_pdb_id).get_stacking()
        first_result_pair = self.parser.extract_pair(first_pdb_id).get_all_pairs()
        second_result_stacking = self.parser.extract_stacking(second_pdb_id).get_stacking()
        second_result_pair = self.parser.extract_pair(second_pdb_id).get_all_pairs()
        return first_result_pair+first_result_stacking, second_result_pair + second_result_stacking