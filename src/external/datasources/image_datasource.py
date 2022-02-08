import cv2
import numpy 

from src.domain.entities.image import Image
from src.domain.parameters.load_image_parameters import LoadImageParameters
from src.infrastructure.datasources.image_datasource_abstraction import ImageDataSourceAbstraction
from src.infrastructure.errors.invalid_image_exception import InvalidImageException
from src.infrastructure.models.image_model import ImageMapper


class ImageDataSource(ImageDataSourceAbstraction):
    def load_image(self, parameters: LoadImageParameters) -> Image:
        data = cv2.imread(parameters.image_path)

        if data is not None:
            return ImageMapper.from_array(data=data)
        else:
            raise InvalidImageException()
    
    def show_image(self, matrix: numpy.ndarray) -> None:
        cv2.imshow('image',matrix)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

