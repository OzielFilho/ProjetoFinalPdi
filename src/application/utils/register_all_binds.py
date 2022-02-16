from application.utils.service_locator import register_bind
from domain.usecases.convert_image_to_bgr_color_space import ConvertImageToBgrColorSpace
from domain.usecases.convert_image_to_grayscale import ConvertImageToGrayScale
from domain.usecases.denoise_image_using_non_local_means import DenoiseImageUsingNonLocalMeans
from domain.usecases.equalize_image import EqualizeImage
from domain.usecases.get_all_glaucomatous_images_paths import GetAllGlaucomatousImagesPaths
from domain.usecases.get_all_normal_images_paths import GetAllNormalImagesPaths
from domain.usecases.load_image import LoadImage
from domain.usecases.normalize_image import NormalizeImage
from external.datasources.image_datasource import ImageDataSource
from infrastructure.repositories.image_repository import ImageRepository
from domain.usecases.write_image import WriteImage


def register_all_binds():
    register_bind(ImageDataSource)
    register_bind(ImageRepository)
    register_bind(GetAllNormalImagesPaths)
    register_bind(LoadImage)
    register_bind(NormalizeImage)
    register_bind(DenoiseImageUsingNonLocalMeans)
    register_bind(EqualizeImage)
    register_bind(ConvertImageToBgrColorSpace)
    register_bind(ConvertImageToGrayScale)
    register_bind(GetAllGlaucomatousImagesPaths)
    register_bind(WriteImage)
