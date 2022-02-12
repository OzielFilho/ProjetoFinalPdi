from abc import ABC, abstractmethod
from domain.parameters.denoise_image_using_non_local_means_parameters import DenoiseImageUsingNonLocalMeansParameters

from domain.entities.image import Image
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters


class ImageDataSourceAbstraction(ABC):
    @abstractmethod
    def load_image(self, parameters: LoadImageParameters) -> Image:
        pass

    @abstractmethod
    def normalize_image(self, parameters: NormalizeImageParameters) -> Image:
        pass

    @abstractmethod
    def denoise_image_using_non_local_means(self, parameters: DenoiseImageUsingNonLocalMeansParameters) -> Image:
        pass

    @abstractmethod
    def equalize_image(self, parameters: EqualizeImageParameters) -> Image:
        pass

    @abstractmethod
    def convert_image_to_bgr_color_space(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Image:
        pass
