from src.domain.entities.image import Image
from src.domain.errors.failure import Failure
from src.domain.errors.image_failure import ImageFailure
from src.domain.errors.invalid_image_failure import InvalidImageFailure
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.infrastructure.datasources.normalization_datasource_abstraction import NormalizationDataSourceAbstraction
from src.domain.usecases.normalization_image import NormalizationRepositoryAbstraction
from src.infrastructure.errors.invalid_image_exception import InvalidImageException

class NormalizationRepository(NormalizationRepositoryAbstraction):
    def __init__(self, datasource: NormalizationDataSourceAbstraction) -> None:
        self.datasource = datasource

    def normalization_image(self, parameters: LoadImageParameters) -> Failure | Image:
        try:
            return self.datasource.normalization_image(parameters)
        except InvalidImageException:
            return InvalidImageFailure()
        except BaseException as exception:
            return ImageFailure(message=str(exception))
