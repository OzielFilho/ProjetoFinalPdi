import numpy

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_failure import InvalidImageFailure
from src.domain.errors.invalid_matrix_image_failure import InvalidMatrixImageFailure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from src.infrastructure.errors.invalid_image_exception import InvalidImageException
from src.infrastructure.errors.invalid_image_exception import InvalidMatrixImageException

class ImageRepository(ImageRepositoryAbstraction):
    def __init__(self, datasource: ImageDataSourceAbstraction) -> None:
        self.datasource = datasource

    def load_image(self, parameters: LoadImageParameters) -> Failure | Image:
        try:
            return self.datasource.load_image(parameters)
        except InvalidImageException:
            return InvalidImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def show_image(self, matrix: numpy.ndarray) -> Failure | None:
        try:
            return self.datasource.show_image(matrix)
        except InvalidMatrixImageException:
            return InvalidMatrixImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))
