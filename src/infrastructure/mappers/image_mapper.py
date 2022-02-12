import numpy

from domain.entities.image import Image


class ImageMapper(Image):
    @staticmethod
    def from_array(data: numpy.ndarray) -> Image:
        return Image(matrix=data)
