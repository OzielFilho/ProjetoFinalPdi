from abc import ABC, abstractmethod

from domain.entities.image import Image
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.parameters.denoise_image_using_non_local_means_parameters import DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters


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

    @abstractmethod
    def convert_image_to_grayscale(self, parameters: ConvertImageToGrayscaleParameters) -> Image:
        pass

    @abstractmethod
    def get_all_normal_images_paths(self) -> list[str]:
        pass

    @abstractmethod
    def get_all_glaucomatous_images_paths(self) -> list[str]:
        pass
