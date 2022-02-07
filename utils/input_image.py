import cv2

class InputImage:
    def __init__(self,location:str):
        self.location = location
        print('INPUT IMAGE - INITIALIZATION')

    def imageGet(self):
        image = cv2.imread(self.location)
        return image

    def showImage(self,image):
         cv2.imshow('HSV Image',image)
