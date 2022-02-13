from abc import ABC, abstractmethod

from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction


class GetAllGlaucomatousImagesPathsAbstraction(ABC):
    @abstractmethod
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        pass

    @abstractmethod
    def __call__(self) -> Failure | list[str]:
        pass


class GetAllGlaucomatousImagesPaths(GetAllGlaucomatousImagesPathsAbstraction):
    def __init__(self, repository: ImageRepositoryAbstraction) -> None:
        self.repository = repository

    def __call__(self) -> Failure | list[str]:
        try:
            return self.repository.get_all_glaucomatous_images_paths()
        except BaseException as exception:
            return ImageFailure(str(exception))
