from domain.entities.image import Image


class BgrImageParameters:
    def __init__(self, image: Image) -> None:
        self.image = image