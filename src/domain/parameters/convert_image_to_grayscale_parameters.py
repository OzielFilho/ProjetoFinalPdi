from domain.entities.image import Image


class ConvertImageToGrayscaleParameters:
    def __init__(self, image: Image) -> None:
        self.image = image