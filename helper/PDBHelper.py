import numpy


def to_vector_list(atom_list):
    """

    :param atom_list: list of atoms object from Bio.PDB
    :return: numpy vector of atoms
    """
    coordinate = numpy.zeros((len(atom_list), 3))

    for index, atom in enumerate(atom_list):
        coordinate[index] = atom.get_coord()

    return coordinate

