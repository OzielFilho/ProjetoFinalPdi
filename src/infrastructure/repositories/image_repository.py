from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from src.domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.domain.repositories.image_repository_abstraction import ImageRepositoryAbstraction
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from src.infrastructure.errors.unable_to_load_image_exception import UnableToLoadImageException


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
