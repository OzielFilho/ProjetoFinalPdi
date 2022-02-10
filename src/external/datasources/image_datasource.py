import cv2
import numpy as np

from domain.entities.image import Image
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalization_image_parameters import \
    EqualizationImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.parameters.bgr_image_parameters import BgrImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from infrastructure.errors.unable_to_bgr_image_exception import UnableToBgrImageException
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import \
    UnableToDenoiseImageUsingNonLocalMeansException
from infrastructure.errors.unable_to_equalization_exception import \
    UnableToEqualizationImageException
from infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException
from infrastructure.errors.unable_to_normalize_image_exception import UnableToNormalizeImageException
from infrastructure.models.image_mapper import ImageMapper


class ImageDataSource(ImageDataSourceAbstraction):
    def load_image(self, parameters: LoadImageParameters) -> Image:
        # Zero makes the image grayscale
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
        red, green, blue = cv2.split(parameters.image.matrix)

        equalized_red = cv2.equalizeHist(red)
        equalized_green = cv2.equalizeHist(green)
        equalized_blue = cv2.equalizeHist(blue)

        data = cv2.merge((equalized_red, equalized_green, equalized_blue))

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToEqualizationImageException()
    
    def image_to_bgr(self,parameters:BgrImageParameters) -> Image:
        data = cv2.cvtColor(parameters.image.matrix,cv2.COLOR_RGB2BGR)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToBgrImageException() 
