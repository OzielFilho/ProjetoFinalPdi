from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from domain.parameters.bgr_image_parameters import BgrImageParameters
from domain.errors.invalid_image_to_bgr_failure import InvalidImageBgrFailure


class ImageToBgrAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self, parameters: BgrImageParameters) -> Failure | Image:
        pass


class ImageToBgr(ImageToBgrAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self, parameters: BgrImageParameters) -> Failure | Image:
        try:
            if parameters is None or not isinstance(parameters.image, Image):
                return InvalidImageBgrFailure()

            return self.repository.bgr_image(parameters)

        except BaseException as exception:
            return ImageFailure(str(exception))
