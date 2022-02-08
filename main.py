from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.usecases.normalization_image import NormalizationImage
from src.external.datasources.normalization_datasource import NormalizationDataSource
from src.infrastructure.repositories.normalization_repository import NormalizationRepository

parameters = LoadImageParameters("..\\ProjetoFinalPdi\\assets\\image.jpg")
datasource = NormalizationDataSource()
repository = NormalizationRepository(datasource)
usecase = NormalizationImage(repository=repository)
image = usecase(parameters=parameters)
print(image.matrix)
