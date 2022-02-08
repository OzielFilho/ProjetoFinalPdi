import cv2
import numpy as np

from domain.entities.image import Image
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalization_image_parameters import \
    EqualizationImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import \
    UnableToDenoiseImageUsingNonLocalMeansException
from infrastructure.errors.unable_to_equalization_exception import \
    UnableToEqualizationImageException
from infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException
from infrastructure.errors.unable_to_normalize_image_exception import UnableToNormalizeImageException
from infrastructure.models.image_mapper import ImageMapper


class ImageDataSource(ImageDataSourceAbstraction):
    def load_image(self, parameters: LoadImageParameters) -> Image:
        data = cv2.imread(parameters.image_path)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToLoadImageException()

    def normalize_image(self, parameters: NormalizeImageParameters) -> Image:
        matrix = np.zeros((800, 800))
        data = cv2.normalize(parameters.image.matrix,
                             matrix, 0, 255, cv2.NORM_MINMAX)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToNormalizeImageException()

    def denoise_image_using_non_local_means(self, parameters: DenoiseImageUsingNonLocalMeansParameters) -> Image:
        data = cv2.fastNlMeansDenoising(parameters.image.matrix, None)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToDenoiseImageUsingNonLocalMeansException()

    def equalization_image(self, parameters: EqualizationImageParameters) -> Image:
        equalization = cv2.equalizeHist(parameters.image.matrix)
        data = np.hstack((parameters.image.matrix, equalization))
        
        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToEqualizationImageException()