import sys

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_path_failure import InvalidImagePathFailure
from src.domain.errors.invalid_image_to_normalize_failure import InvalidImageToNormalizeFailure
from src.domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from src.domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.domain.usecases.load_image import LoadImage
from src.domain.usecases.normalize_image import NormalizeImage
from src.external.datasources.image_datasource import ImageDataSource
from src.infrastructure.repositories.image_repository import ImageRepository

# Core dependencies
image_datasource = ImageDataSource()
image_repository = ImageRepository(image_datasource)


def error_checker(result):
    if isinstance(result, Failure):
        if isinstance(result, InvalidImagePathFailure):
            print("The specified image path is invalid")
        if isinstance(result, UnableToLoadImageFailure):
            print("Can't load image")
        if isinstance(result, InvalidImageToNormalizeFailure):
            print("The specified image to normalize is invalid")
        if isinstance(result, UnableToNormalizeImageFailure):
            print("Can't normalize image")
        if isinstance(result, ImageFailure) and result.message is not None:
            print(result.message)

        sys.exit()
    else:
        return result


def load_image_from_path(image_path: str) -> Image:
    load_image = LoadImage(image_repository)
    parameters = LoadImageParameters(image_path)
    result = load_image(parameters)

    return error_checker(result)


def image_normalization(image: Image) -> Image:
    normalize_image = NormalizeImage(image_repository)
    parameters = NormalizeImageParameters(image)
    result = normalize_image(parameters)

    return error_checker(result)


def pre_processing():
    image = load_image_from_path("../assets/image.jpg")
    normalized_image = image_normalization(image)


def main():
    pre_processing()


if __name__ == "__main__":
    main()
