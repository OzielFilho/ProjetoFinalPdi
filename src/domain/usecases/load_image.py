from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_path_failure import InvalidImagePathFailure
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class LoadImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: LoadImageParameters) -> Failure | Image:
        pass


class LoadImage(LoadImageAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: LoadImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image_path, str) or len(parameters.image_path) <= 0:
                return InvalidImagePathFailure()

            return self.repository.load_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
