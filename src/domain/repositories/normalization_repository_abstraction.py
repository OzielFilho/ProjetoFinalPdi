from abc import ABC, abstractmethod

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction


class NormalizationRepositoryAbstraction(ABC):
    @abstractmethod
    def __init__(self, datasource: ImageDataSourceAbstraction) -> None:
        pass

    @abstractmethod
    def normalization_image(self, parameters: LoadImageParameters) -> Failure | Image:
        pass
