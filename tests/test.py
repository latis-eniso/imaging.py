import sys
from latis.ImageProcessing.ImageIO import ImageIO



#  Simple Image Loading Test
image = ImageIO.loadImage("test_images/image-000002.dcm")
print(image)