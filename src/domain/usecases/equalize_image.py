from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_to_equalize_failure import InvalidImageToEqualizeFailure
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class EqualizeImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: EqualizeImageParameters) -> Failure | Image:
        pass


class EqualizeImage(EqualizeImageAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: EqualizeImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToEqualizeFailure()

            return self.repository.equalize_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
