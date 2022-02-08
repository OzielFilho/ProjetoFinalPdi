from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.unable_to_denoise_image_using_non_local_means_failure import \
    UnableToDenoiseImageUsingNonLocalMeansFailure
from domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from infrastructure.errors.unable_to_denoise_image_using_non_local_means_exception import \
    UnableToDenoiseImageUsingNonLocalMeansException
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
