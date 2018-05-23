from Bio.SVDSuperimposer import SVDSuperimposer
import numpy


class MetricsRMSD(object):

    def __init__(self):
        self.reference_coordinate = None
        self.model_coordinate = None
        self.sup = SVDSuperimposer()

    def clear(self):
        self.reference_coordinate = None
        self.model_coordinate = None

    def set(self, reference_coordinate, model_coordinate):

        if not len(reference_coordinate) == len(model_coordinate):
            raise ValueError("Reference coordinate and coordinate moving atom lists differ in size")

        self.clear()
        self.reference_coordinate = reference_coordinate
        self.model_coordinate = model_coordinate

    def run_svd(self):
        self.sup.set(self.reference_coordinate, self.model_coordinate)
        self.sup.run()

    def get_rms(self):
        rotation, translation = self.sup.get_rotran()

        transformed_coordinate = numpy.dot(self.model_coordinate, rotation) + translation

        diff = transformed_coordinate - self.reference_coordinate
        return numpy.sqrt(sum(sum(diff * diff)) / len(self.model_coordinate))
