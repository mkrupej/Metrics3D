class Sphere(object):

    def __init__(self, center, radius):
        self.c = center
        self.r = radius

    def __contains__(self, atom):
        p = atom.get_coord()
        if (p[0]-self.c[0]) ** 2 + (p[1]-self.c[1]) ** 2 + (p[2]-self.c[2]) ** 2 < self.r ** 2:
            return True
        else:
            return False


def filter_intersection_atoms(reference_residues, model_residues, sphere=None):

    model_id_list = map(lambda x: x.get_id()[1], model_residues)

    intersection_seq_id_list = [s.get_id()[1] for s in reference_residues if s.get_id()[1] in model_id_list]

    filtered_reference = {r.get_id()[1]: r for r in reference_residues if r.get_id()[1] in intersection_seq_id_list}

    filtered_model = {r.get_id()[1]: r for r in model_residues if r.get_id()[1] in intersection_seq_id_list}

    reference_atoms, model_atoms = [], []

    for i in intersection_seq_id_list:
        reference_atoms_temp = list(filter_atoms_in_residue(filtered_reference[i], sphere))
        model_atoms_temp = list(filter_atoms_in_residue(filtered_model[i], sphere))

        reference_atoms += [a for a in reference_atoms_temp if a.get_name() in [x.get_name() for x in model_atoms_temp]]
        model_atoms += [a for a in model_atoms_temp if a.get_name() in [x.get_name() for x in reference_atoms_temp]]

    return reference_atoms, model_atoms


def filter_atoms_in_residue(residue, sphere):

    if sphere is not None and isinstance(sphere, Sphere):
        return filter(lambda x: sphere.__contains__(x), [a for a in residue.get_atoms()])
    else:
        return residue.get_atoms()


def filter_atoms(atoms, sphere):
    if sphere is not None and isinstance(sphere, Sphere):
        return filter(lambda x: sphere.__contains__(x), [a for a in atoms])
    else:
        return atoms


def filter_base_pairs(base_pairs, sphere, residues):

    result = []

    for b in base_pairs:
        res_1 = filter_atoms_in_residue(residues[int(b['a_number'])], sphere)
        res_2 = filter_atoms_in_residue(residues[int(b['b_number'])], sphere)
        if len(list(res_1)) > 0 and len(list(res_2)) > 0:
            result.append(b)

    return result
