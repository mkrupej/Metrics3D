import csv


class BasePair(object):

    def __init__(self, pdb_id):
        self.pdb_id = pdb_id
        self.PAIR = "base_pair/{}"
        self.STACKING = "base_stacking/{}"

        self.base_pairs = None
        self.base_stacking = None

    def clear(self):
        self.base_stacking = None
        self.base_pairs = None

    def extract_pairs(self):
        self.clear()
        self.base_pairs = self.extract_alignment("pair")

    def extract_stacking(self):
        self.clear()
        self.base_stacking = self.extract_alignment("stacking")

    def extract_alignment(self, file_type):

        alignment = []

        pair = {'a_model' : None, 'a_chain': None, 'a_compound': None, 'a_number': None,
                'b_model': None, 'b_chain': None, 'b_compound': None, 'b_number': None,
                'interaction': None}

        if file_type.lower() is "pair":
            file = self.PAIR.format(self.pdb_id)

        elif file_type.lower() is "stacking":
            file = self.STACKING.format(self.pdb_id)

        else:
            raise ValueError("Wrong file type. Should be stacking or pair")

        with open(file) as csv_file:
                line_reader = csv.reader(csv_file, delimiter='|', quotechar = " ")
                for line in line_reader:
                    pair['a_model'] = line[1]
                    pair['a_chain'] = line[2]
                    pair['a_compound'] = line[3]
                    pair['a_number'] = line[4].split('"')[0]
                    pair['b_model'] = line[5]
                    pair['b_chain'] = line[6]
                    pair['b_compound'] = line[7]
                    pair['b_number'] = line[8][:-1]
                    pair['interaction'] = line[4].split('"')[2]
                    alignment.append(pair)

        return alignment
