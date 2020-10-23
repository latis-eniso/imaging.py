import sys
sys.path.append("external")


from latis.ImageProccessing.ImageIO import ImageIO
image = ImageIO.loadImage("image-000002.dcm")
print(image)