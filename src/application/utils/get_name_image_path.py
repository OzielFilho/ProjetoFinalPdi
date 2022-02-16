from operator import contains
from os import sep


def get_name_image_path(image_path:str) -> str:
    general_path = './assets/rim_one_db/'

    if general_path in image_path:
        list_path = image_path.split(sep=general_path)
        return list_path[1].split(sep='.jpg')[0]
    