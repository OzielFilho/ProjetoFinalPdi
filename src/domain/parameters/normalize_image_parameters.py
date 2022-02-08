from src.domain.entities.image import Image


class NormalizeImageParameters:
    def __init__(self, image: Image) -> None:
        self.image = image
