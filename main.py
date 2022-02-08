import cv2

from src.domain.parameters.load_image_parameters import LoadImageParameters
from domain.usecases.normalize_image import NormalizeImage
from src.external.datasources.normalization_datasource import NormalizationDataSource
from src.infrastructure.repositories.normalization_repository import (
    NormalizationRepository,
)

parameters = LoadImageParameters("..\\ProjetoFinalPdi\\assets\\image.jpg")
datasource = NormalizationDataSource()
repository = NormalizationRepository(datasource)
usecase = NormalizeImage(repository=repository)
image = usecase(parameters=parameters)


print(image.matrix)
