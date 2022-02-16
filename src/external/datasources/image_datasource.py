import os

import cv2
import numpy as np
from domain.entities.image import Image
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from infrastructure.errors.unable_to_convert_image_to_bgr_color_space_exception import \
    UnableToConvertImageToBgrColorSpaceException
from infrastructure.errors.unable_to_convert_image_to_grayscale_exception import \
    UnableToConvertImageToGrayscaleException
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import \
    UnableToDenoiseImageUsingNonLocalMeansException
from infrastructure.errors.unable_to_equalize_exception import UnableToEqualizeImageException
from infrastructure.errors.unable_to_get_all_glaucomatous_images_paths_exception import \
    UnableToGetAllGlaucomatousImagesPathsException
from infrastructure.errors.unable_to_get_all_normal_images_paths_exception import \
    UnableToGetAllNormalImagesPathsException
from infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException
from infrastructure.errors.unable_to_normalize_image_exception import UnableToNormalizeImageException
from infrastructure.mappers.image_mapper import ImageMapper
from domain.parameters.write_image_parameters import WriteImageParameters
from infrastructure.errors.unable_to_write_image_exception import UnableToWriteImageException


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

    def get_paths_from(self, path: str):
        paths: list[str] = []

        for file in os.listdir(path):
            paths.append(os.path.join(path, file))

        return paths

    def get_all_normal_images_paths(self) -> list[str]:
        try:
            current_path = os.getcwd()
            os.chdir('..')
            root_path = os.getcwd()

            normal_images_folder_path = os.path.join(
                root_path,
                'assets',
                'rim_one_db',
                'normal'
            )

            paths = self.get_paths_from(normal_images_folder_path)

            os.chdir(current_path)

            return paths
        except:
            raise UnableToGetAllNormalImagesPathsException()

    def get_all_glaucomatous_images_paths(self) -> list[str]:
        try:
            current_path = os.getcwd()
            os.chdir('..')
            root_path = os.getcwd()

            glaucomatous_images_folder_path = os.path.join(
                root_path,
                'assets',
                'rim_one_db',
                'glaucoma'
            )

            paths = self.get_paths_from(glaucomatous_images_folder_path)

            os.chdir(current_path)

            return paths
        except:
            raise UnableToGetAllGlaucomatousImagesPathsException()
    
    def write_image(self, parameters: WriteImageParameters) -> None:
        data = cv2.imwrite(parameters.image_path,parameters.image.matrix)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise UnableToWriteImageException()

