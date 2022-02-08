from abc import ABC, abstractmethod

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_to_normalize_failure import InvalidImageToNormalizeFailure
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


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
