from domain.entities.image import Image


class ConvertImageToBgrColorSpaceParameters:
    def __init__(self, image: Image) -> None:
        self.image = image
