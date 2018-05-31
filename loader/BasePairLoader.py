import wget
import os
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