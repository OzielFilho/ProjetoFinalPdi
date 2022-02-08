import cv2
import numpy as np

from src.infrastructure.datasources.normalization_datasource_abstraction import NormalizationDataSourceAbstraction
from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.infrastructure.models.image_model import ImageMapper
from src.infrastructure.errors.invalid_image_exception import InvalidImageException

class NormalizationDataSource(NormalizationDataSourceAbstraction):
    def normalization_image(self, parameters: LoadImageParameters) -> Image:
        img = cv2.imread(parameters.image_path)
        matrix = np.zeros((800, 800))
        data = cv2.normalize(img,  matrix, 0, 255, cv2.NORM_MINMAX)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise InvalidImageException()