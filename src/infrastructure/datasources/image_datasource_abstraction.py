from abc import ABC, abstractmethod
from domain.parameters.denoise_image_using_non_local_means_parameters import DenoiseImageUsingNonLocalMeansParameters

from domain.entities.image import Image
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.parameters.equalization_image_parameters import EqualizationImageParameters

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
    def equalization_image(self, parameters: EqualizationImageParameters) -> Image:
        pass
