import cv2
import numpy as np

from domain.entities.image import Image
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import \
    UnableToDenoiseImageUsingNonLocalMeansException
from infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException
from infrastructure.errors.unable_to_normalize_image_exception import UnableToNormalizeImageException
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from infrastructure.errors.unable_to_convert_image_to_bgr_color_space_exception import \
    UnableToConvertImageToBgrColorSpaceException
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import UnableToDenoiseImageUsingNonLocalMeansException
from infrastructure.errors.unable_to_equalize_exception import UnableToEqualizeImageException
from infrastructure.mappers.image_mapper import ImageMapper
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from infrastructure.errors.unable_to_convert_image_to_grayscale_exception import UnableToConvertImageToGrayscaleException


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

    def equalize_image(self, parameters: EqualizeImageParameters) -> Image:
        red, green, blue = cv2.split(parameters.image.matrix)

        equalized_red = cv2.equalizeHist(red)
        equalized_green = cv2.equalizeHist(green)
        equalized_blue = cv2.equalizeHist(blue)

        data = cv2.merge((equalized_red, equalized_green, equalized_blue))

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToEqualizeImageException()

    def convert_image_to_bgr_color_space(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Image:
        data = cv2.cvtColor(parameters.image.matrix, cv2.COLOR_RGB2BGR)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToConvertImageToBgrColorSpaceException()

    def convert_image_to_grayscale(self, parameters: ConvertImageToGrayscaleParameters) -> Image:
        data = cv2.cvtColor(parameters.image.matrix, cv2.COLOR_BGR2GRAY)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToConvertImageToGrayscaleException()
