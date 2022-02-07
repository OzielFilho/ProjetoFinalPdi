from utils.input_image import InputImage


print('-'*55)
print('\t\tProject Final PDI')
print('-'*55)

inputImage = InputImage('./assets/image.jpg')
image = inputImage.imageGet()

inputImage.showImage(image)




