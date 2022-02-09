from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_to_equalization_failure import InvalidImageToEqualizationFailure
from domain.parameters.equalization_image_parameters import EqualizationImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class EqualizationAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: EqualizationImageParameters) -> Failure | Image:
        pass


class EqualizationImage(EqualizationAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: EqualizationImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToEqualizationFailure()

            return self.repository.equalization_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
