from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_to_convert_to_grayscale_failure import InvalidImageToConvertToGrayScaleFailure
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class ConvertImageToGrayScaleAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: ConvertImageToGrayscaleParameters) -> Failure | Image:
        pass


class ConvertImageToGrayScale(ConvertImageToGrayScaleAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: ConvertImageToGrayscaleParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToConvertToGrayScaleFailure()

            return self.repository.convert_image_to_grayscale(parameters)

        except BaseException as exception:
            return ImageFailure(str(exception))
