import cv2

from src.infrastructure.datasources.normalization_datasource_abstraction import NormalizationDataSourceAbstraction
from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.infrastructure.models.image_model import ImageMapper
from src.infrastructure.errors.invalid_image_exception import InvalidImageException

class NormalizationDataSource(NormalizationDataSourceAbstraction):
    def normalization_image(self, parameters: LoadImageParameters) -> Image:
        data = cv2.imread(parameters.image_path)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise InvalidImageException()