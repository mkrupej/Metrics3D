from Bio.PDB import *
import shutil


class PDBLoader(object):

    def __init__(self):
        self.pdb_list = PDBList()
        self.parser = PDBParser()

    def retrieve_pdb_file(self, pdb_id):
        self.pdb_list.retrieve_pdb_file(pdb_id, file_format='pdb', pdir='pdb')
        shutil.rmtree('obsolete', ignore_errors=True)

    def parse_structure(self, pdb_id):
        self.retrieve_pdb_file(pdb_id)
        return self.parser.get_structure(pdb_id, 'pdb/pdb{}.ent'.format(pdb_id.lower()))

    def get_residue(self, pdb_id):
        return list(self.parse_structure(pdb_id).get_residues())
