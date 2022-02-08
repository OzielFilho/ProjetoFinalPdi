from abc import ABC, abstractmethod

from src.domain.repositories.normalization_repository_abstraction import NormalizationRepositoryAbstraction
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_path_failure import InvalidImagePathFailure

class NormalizationImageAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: NormalizationRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: LoadImageParameters) -> Failure | Image:
        pass

class NormalizationImage(NormalizationImageAbstraction):
    def __init__(self, repository: NormalizationRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: LoadImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image_path, str) or len(parameters.image_path) <= 0:
                return InvalidImagePathFailure()

            return self.repository.normalization_image(parameters)
        except BaseException as exception:
            return ImageFailure(str(exception))