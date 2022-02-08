from abc import ABC, abstractmethod
import numpy

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_path_failure import InvalidMatrixImageFailure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class ShowImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass    

    @abstractmethod
    def __call__(self, matrix: numpy.ndarray) -> Failure | None:
        pass

class ShowImage(ShowImageAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, matrix: numpy.ndarray) -> Failure | Image:
        try:
            if matrix is None or not isinstance(matrix, numpy.ndarray) :
                return InvalidMatrixImageFailure()

            return self.repository.show_image(matrix)
        except BaseException as exception:
            return ImageFailure(str(exception))