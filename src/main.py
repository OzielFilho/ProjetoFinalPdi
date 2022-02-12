import sys

import cv2

from domain.entities.image import Image
from domain.errors.failure import Failure
from domain.errors.image_failure import ImageFailure
from domain.errors.invalid_image_path_failure import InvalidImagePathFailure
from domain.errors.invalid_image_to_convert_to_bgr_color_space_failure import \
    InvalidImageToConvertToBgrColorSpaceFailure
from domain.errors.invalid_image_to_convert_to_grayscale_failure import InvalidImageToConvertToGrayScaleFailure
from domain.errors.invalid_image_to_denoise_failure import InvalidImageToDenoiseFailure
from domain.errors.invalid_image_to_equalize_failure import InvalidImageToEqualizeFailure
from domain.errors.invalid_image_to_normalize_failure import InvalidImageToNormalizeFailure
from domain.errors.unable_to_convert_image_to_bgr_color_space_failure import UnableToConvertImageToBgrColorSpaceFailure
from domain.errors.unable_to_denoise_image_using_non_local_means_failure import \
    UnableToDenoiseImageUsingNonLocalMeansFailure
from domain.errors.unable_to_equalize_image_failure import UnableToEqualizeImageFailure
from domain.errors.unable_to_load_image_failure import UnableToLoadImageFailure
from domain.errors.unable_to_normalize_image_failure import UnableToNormalizeImageFailure
from domain.parameters.convert_image_to_bgr_color_space_parameters import ConvertImageToBgrColorSpaceParameters
from domain.parameters.convert_image_to_grayscale_parameters import ConvertImageToGrayscaleParameters
from domain.parameters.denoise_image_using_non_local_means_parameters import \
    DenoiseImageUsingNonLocalMeansParameters
from domain.parameters.equalize_image_parameters import EqualizeImageParameters
from domain.parameters.load_image_parameters import LoadImageParameters
from domain.parameters.normalize_image_parameters import NormalizeImageParameters
from domain.usecases.convert_image_to_bgr_color_space import ConvertImageToBgrColorSpace
from domain.usecases.convert_image_to_grayscale import ConvertImageToGrayScale
from domain.usecases.denoise_image_using_non_local_means import DenoiseImageUsingNonLocalMeans
from domain.usecases.equalize_image import EqualizeImage
from domain.usecases.load_image import LoadImage
from domain.usecases.normalize_image import NormalizeImage
from external.datasources.image_datasource import ImageDataSource
from infrastructure.errors.unable_to_convert_image_to_grayscale_exception import \
    UnableToConvertImageToGrayscaleException
from infrastructure.repositories.image_repository import ImageRepository

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
        if isinstance(result, InvalidImageToEqualizeFailure):
            print("The specified image to equalize is invalid")
        if isinstance(result, UnableToEqualizeImageFailure):
            print("Can't equalize image")
        if isinstance(result, InvalidImageToConvertToBgrColorSpaceFailure):
            print("The specified image to convert is invalid")
        if isinstance(result, UnableToConvertImageToBgrColorSpaceFailure):
            print("Can't convert image to BGR color space")
        if isinstance(result, InvalidImageToConvertToGrayScaleFailure):
            print("The specified image to convert is invalid")
        if isinstance(result, UnableToConvertImageToGrayscaleException):
            print("Can't convert image to grayscale")
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


def image_equalization(image: Image) -> Image:
    equalize_image = EqualizeImage(image_repository)
    parameters = EqualizeImageParameters(image)
    result = equalize_image(parameters)

    return error_checker(result)


def image_color_space_conversion(image: Image) -> Image:
    convert_image_to_bgr_color_space = ConvertImageToBgrColorSpace(
        image_repository)
    parameters = ConvertImageToBgrColorSpaceParameters(image)
    result = convert_image_to_bgr_color_space(parameters)

    return error_checker(result)


def image_convert_to_grayscale(image: Image) -> Image:
    convert_image_to_grayscale = ConvertImageToGrayScale(image_repository)
    parameters = ConvertImageToGrayscaleParameters(image)
    result = convert_image_to_grayscale(parameters)

    return error_checker(result)


def pre_processing(image_path: str) -> Image:
    image = load_image_from_path(image_path)
    display_image("Original image", image)

    normalized_image = image_normalization(image)
    display_image("Normalized image", normalized_image)

    denoised_image = image_denoising(normalized_image)
    display_image("Denoised image", denoised_image)

    equalized_image = image_equalization(denoised_image)
    display_image("Equalized image", equalized_image)

    return equalized_image


def color_space_conversion(image: Image) -> Image:
    image_in_bgr_color_space = image_color_space_conversion(image)
    display_image("Image in BGR color space", image_in_bgr_color_space)

    image_in_grayscale = image_convert_to_grayscale(image_in_bgr_color_space)
    display_image("Image in Grayscale", image_in_grayscale)


def image_processing(image_path: str) -> None:
    processed_image = pre_processing(image_path)
    color_space_conversion(processed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image_processing('../assets/rim_one_db/glaucoma/Im256.jpg')


if __name__ == "__main__":
    main()
