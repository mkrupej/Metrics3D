from Bio.PDB import *
import numpy


class PDBLoader(object):

    def __init__(self):
        self.pdb_list = PDBList()
        self.parser = PDBParser()

    def retrieve_pdb_file(self, pdb_id):
        self.pdb_list.retrieve_pdb_file(pdb_id, file_format='pdb', pdir='pdb')

    def parse_structure(self, pdb_id):
        self.retrieve_pdb_file(pdb_id)
        return self.parser.get_structure(pdb_id, 'pdb/pdb{}.ent'.format(pdb_id.lower()))

    def get_atom_array(self, pdb_id):
        atoms = list(self.parse_structure(pdb_id).get_atoms())

        coordinate = numpy.zeros((len(atoms), 3))

        for index, atom in enumerate(atoms):
            coordinate[index] = atom.get_coord()

        return coordinate
