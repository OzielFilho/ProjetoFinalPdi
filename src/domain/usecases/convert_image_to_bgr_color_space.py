from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from domain.errors.invalid_image_to_convert_to_bgr_color_space_failure import InvalidImageToConvertToBgrColorSpaceFailure
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters


class ConvertImageToBgrColorSpaceAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Failure | Image:
        pass


class ConvertImageToBgrColorSpace(ConvertImageToBgrColorSpaceAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToConvertToBgrColorSpaceFailure()

            return self.repository.convert_image_to_bgr_color_space(parameters)

        except BaseException as exception:
            return ImageFailure(str(exception))
