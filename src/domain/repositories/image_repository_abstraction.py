from abc import ABC, abstractmethod

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction


class ImageRepositoryAbstraction(ABC):
    @abstractmethod
    def __init__(self, datasource: ImageDataSourceAbstraction) -> None:
        pass

    @abstractmethod
    def load_image(self, parameters: LoadImageParameters) -> Failure | Image:
        pass

    @abstractmethod
    def normalize_image(self, parameters: NormalizeImageParameters) -> Failure | Image:
        pass

    @abstractmethod
    def denoise_image_using_non_local_means(
            self,
            parameters: DenoiseImageUsingNonLocalMeansParameters
    ) -> Failure | Image:
        pass
