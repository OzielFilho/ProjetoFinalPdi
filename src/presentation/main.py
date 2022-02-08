from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.domain.usecases.load_image import LoadImage
from src.external.datasources.image_datasource import ImageDataSource
from src.infrastructure.repositories.image_repository import ImageRepository

parameters = LoadImageParameters("C:\\Programming\\Code\\ProjetoFinalPdi\\assets\\image.jpg")
datasource = ImageDataSource()
repository = ImageRepository(datasource)
usecase = LoadImage(repository=repository)
image = usecase(parameters=parameters)
print(image.matrix)
