import cv2

class InputImage:
    def __init__(self,location:str):
        self.location = location
        print('INPUT IMAGE - INITIALIZATION')

    def imageGet(self):
        image = cv2.imread(self.location)
        return image
        
    def showImage(self,imageShow):
        return cv2.imshow('Image',imageShow)

    def writeImage(self,destiny:str,imageWrite):
         cv2.imwrite(destiny,imageWrite)
     
