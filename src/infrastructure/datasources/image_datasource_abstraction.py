from abc import ABC, abstractmethod
import numpy

from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters


class ImageDataSourceAbstraction(ABC):
    @abstractmethod
    def load_image(self, parameters: LoadImageParameters) -> Image:
        pass

    @abstractmethod
    def show_image(self,matrix:numpy.ndarray) -> None:
        pass
