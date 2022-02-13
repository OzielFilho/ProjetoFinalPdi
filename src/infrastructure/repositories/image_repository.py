from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.unable_to_convert_image_to_bgr_color_space_failure import UnableToConvertImageToBgrColorSpaceFailure
from domain.errors.unable_to_convert_image_to_grayscale_failure import UnableToConvertImageToGrayscaleFailure
from domain.errors.unable_to_denoise_image_using_non_local_means_failure import \
    UnableToDenoiseImageUsingNonLocalMeansFailure
from domain.errors.unable_to_equalize_image_failure import UnableToEqualizeImageFailure
from domain.errors.unable_to_get_all_glaucomatous_images_paths_failure import \
    UnableToGetAllGlaucomatousImagesPathsFailure
from domain.errors.unable_to_get_all_normal_images_paths_failure import UnableToGetAllNormalImagesPathsFailure
from domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
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


class ImageRepository(ImageRepositoryAbstraction):
    def __init__(self, datasource: ImageDataSourceAbstraction) -> None:
        self.datasource = datasource

    def load_image(self, parameters: LoadImageParameters) -> Failure | Image:
        try:
            return self.datasource.load_image(parameters)
        except UnableToLoadImageException:
            return UnableToLoadImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def normalize_image(self, parameters: NormalizeImageParameters) -> Failure | Image:
        try:
            return self.datasource.normalize_image(parameters)
        except UnableToLoadImageException:
            return UnableToNormalizeImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def denoise_image_using_non_local_means(
            self,
            parameters: DenoiseImageUsingNonLocalMeansParameters
    ) -> Failure | Image:
        try:
            return self.datasource.denoise_image_using_non_local_means(parameters)
        except UnableToDenoiseImageUsingNonLocalMeansException:
            return UnableToDenoiseImageUsingNonLocalMeansFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def equalize_image(self, parameters: EqualizeImageParameters) -> Failure | Image:
        try:
            return self.datasource.equalize_image(parameters)
        except UnableToEqualizeImageException:
            return UnableToEqualizeImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def convert_image_to_bgr_color_space(self, parameters: ConvertImageToBgrColorSpaceParameters) -> Failure | Image:
        try:
            return self.datasource.convert_image_to_bgr_color_space(parameters)
        except UnableToConvertImageToBgrColorSpaceException:
            return UnableToConvertImageToBgrColorSpaceFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def convert_image_to_grayscale(self, parameters: ConvertImageToGrayscaleParameters) -> Failure | Image:
        try:
            return self.datasource.convert_image_to_grayscale(parameters)
        except UnableToConvertImageToGrayscaleException:
            return UnableToConvertImageToGrayscaleFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def get_all_normal_images_paths(self) -> Failure | list[str]:
        try:
            return self.datasource.get_all_normal_images_paths()
        except UnableToGetAllNormalImagesPathsException:
            return UnableToGetAllNormalImagesPathsFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))

    def get_all_glaucomatous_images_paths(self) -> Failure | list[str]:
        try:
            return self.datasource.get_all_glaucomatous_images_paths()
        except UnableToGetAllGlaucomatousImagesPathsException:
            return UnableToGetAllGlaucomatousImagesPathsFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))
