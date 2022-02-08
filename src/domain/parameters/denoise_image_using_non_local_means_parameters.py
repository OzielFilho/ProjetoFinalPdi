from domain.entities.image import Image


class DenoiseImageUsingNonLocalMeansParameters:
    def __init__(self, image: Image) -> None:
        self.image = image
