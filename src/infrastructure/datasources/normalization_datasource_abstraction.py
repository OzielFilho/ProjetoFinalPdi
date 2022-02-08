from abc import ABC, abstractmethod
from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters

class NormalizationDataSourceAbstraction(ABC):
    @abstractmethod
    def normalization_image(self, parameters: LoadImageParameters) -> Image:
        pass