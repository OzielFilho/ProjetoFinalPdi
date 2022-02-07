import cv2
from utils.input_image import InputImage

print('-'*55)
print('\t\tProject Final PDI')
print('-'*55)

inputImage = InputImage('./assets/image.jpg')
image = inputImage.imageGet()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inputImage.writeImage('./results/image_result.jpg', gray)

inputImage.showImage(gray)




