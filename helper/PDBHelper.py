import numpy


def to_vector_list(atom_list):
    coordinate = numpy.zeros((len(atom_list), 3))

    for index, atom in enumerate(atom_list):
        coordinate[index] = atom.get_coord()

    return coordinate
