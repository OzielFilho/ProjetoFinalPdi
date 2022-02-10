from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from domain.parameters.equalization_image_parameters import EqualizationImageParameters
from domain.parameters.bgr_image_parameters import BgrImageParameters


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

    @abstractmethod
    def equalization_image(self, parameters: EqualizationImageParameters) -> Failure | Image:
        pass

    @abstractmethod
    def bgr_image(self, parameters: BgrImageParameters) -> Failure | Image:
        pass
