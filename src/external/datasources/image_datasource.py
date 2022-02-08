import cv2
import numpy as np

from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from src.infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException
from src.infrastructure.errors.unable_to_normalize_image_exception import UnableToNormalizeImageException
from src.infrastructure.models.image_mapper import ImageMapper


class ImageDataSource(ImageDataSourceAbstraction):
    def load_image(self, parameters: LoadImageParameters) -> Image:
        data = cv2.imread(parameters.image_path)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToLoadImageException()

    def normalize_image(self, parameters: NormalizeImageParameters) -> Image:
        matrix = np.zeros((800, 800))
        data = cv2.normalize(parameters.image.matrix, matrix, 0, 255, cv2.NORM_MINMAX)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToNormalizeImageException()
