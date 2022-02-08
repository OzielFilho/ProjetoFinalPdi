import sys

import cv2

from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_path_failure import InvalidImagePathFailure
from src.domain.errors.invalid_image_to_denoise_failure import InvalidImageToDenoiseFailure
from src.domain.errors.invalid_image_to_normalize_failure import InvalidImageToNormalizeFailure
from src.domain.errors.unable_to_denoise_image_using_non_local_means_failure import \
    UnableToDenoiseImageUsingNonLocalMeansFailure
from src.domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from src.domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from src.domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.parameters.normalize_image_parameters import NormalizeImageParameters
from src.domain.usecases.denoise_image_using_non_local_means import DenoiseImageUsingNonLocalMeans
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
        if isinstance(result, InvalidImageToDenoiseFailure):
            print("The specified image to denoise is invalid")
        if isinstance(result, UnableToDenoiseImageUsingNonLocalMeansFailure):
            print("Can't denoise image using non local means method")
        if isinstance(result, ImageFailure) and result.message is not None:
            print(result.message)

        sys.exit()
    else:
        return result


def display_image(window_title: str, image: Image, auto_close: bool = False):
    cv2.imshow(window_title, image.matrix)

    if auto_close:
        cv2.waitKey(0)
        cv2.destroyWindow(str)


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


def image_denoising(image: Image) -> Image:
    denoise_image = DenoiseImageUsingNonLocalMeans(image_repository)
    parameters = DenoiseImageUsingNonLocalMeansParameters(image)
    result = denoise_image(parameters)

    return error_checker(result)


def pre_processing():
    image = load_image_from_path("../assets/wom1.png")
    display_image("Original image", image)
    normalized_image = image_normalization(image)
    display_image("Normalized image", normalized_image)
    denoised_image = image_denoising(normalized_image)
    display_image("Denoised image", denoised_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    pre_processing()


if __name__ == "__main__":
    main()
