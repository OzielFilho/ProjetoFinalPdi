from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_to_denoise_failure import InvalidImageToDenoiseFailure
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class DenoiseImageUsingNonLocalMeansAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    @abstractmethod
    def __call__(self, parameters: DenoiseImageUsingNonLocalMeansParameters) -> Failure | Image:
        pass


class DenoiseImageUsingNonLocalMeans(DenoiseImageUsingNonLocalMeansAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: DenoiseImageUsingNonLocalMeansParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageToDenoiseFailure()

            return self.repository.denoise_image_using_non_local_means(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))
