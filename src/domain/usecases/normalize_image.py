from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_to_normalize_failure import InvalidImageToNormalizeFailure
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class NormalizeImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    @abstractmethod
    def __call__(self, parameters: NormalizeImageParameters) -> Failure | Image:
        pass


class NormalizeImage(NormalizeImageAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: NormalizeImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToNormalizeFailure()

            return self.repository.normalize_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
