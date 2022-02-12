from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction


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
    def equalize_image(self, parameters: EqualizeImageParameters) -> Failure | Image:
        pass

    @abstractmethod
    def convert_image_to_bgr_color_space(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Failure | Image:
        pass

    @abstractmethod
    def convert_image_to_grayscale(self, parameters: ConvertImageToGrayscaleParameters) -> Failure | Image:
        pass
