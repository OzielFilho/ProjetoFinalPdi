from abc import ABC, abstractmethod

from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_write_image_failure import InvalidWriteImageFailure
from domain.parameters.write_image_parameters import WriteImageParameters
from domain.entities.image import Image


class WriteImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    @abstractmethod
    def __call__(self, parameters: WriteImageParameters) -> Failure | None:
        pass


class WriteImage(WriteImageAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: WriteImageParameters) -> Failure | None:
        try:
            if parameters is None or not isinstance(parameters.image_path, str) or not isinstance(parameters.image, Image):
                return InvalidWriteImageFailure()

            return self.repository.write_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
