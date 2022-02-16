from domain.entities.image import Image


class WriteImageParameters:
    def __init__(self, image_path: str,image: Image) -> None:
        self.image_path = image_path
        self.image = image