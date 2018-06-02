import numpy


def to_vector_list(atom_list):
    coordinate = numpy.zeros((len(atom_list), 3))

    for index, atom in enumerate(atom_list):
        coordinate[index] = atom.get_coord()

    return coordinate


def get_intersection(first_atoms, second_atoms):
    first_residue = [a.get_parent() for a in first_atoms]
    second_residue = [a.get_parent() for a in second_atoms]

    intersection_residue = {r.get_id()[1] for r in first_residue if second_residue.__contains__(r)}

    return intersection_residue


