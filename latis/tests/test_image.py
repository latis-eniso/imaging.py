import os
from unittest import TestCase
from latis.ImageProcessing.ImageIO import ImageIO
from latis.ImageProcessing.Image import Image

file_dir = os.path.dirname(os.path.realpath('__file__'))
test_image = file_dir + '\\test_images\\image-000002.dcm'


class ImageTests(TestCase):
    def test_image_loading(self):
        image = ImageIO.loadImage(test_image)
        self.assertTrue(isinstance(image, Image))

    def test_image_has_pixel_data(self):
        image = ImageIO.loadImage(test_image)
        self.assertTrue(image.pixelData.size > 0)

    def test_image_has_height_width(self):
      image = ImageIO.loadImage(test_image)
      self.assertTrue(image.height != None)
      self.assertTrue(image.width != None)

    def test_image_has_dtype(self):
      image = ImageIO.loadImage(test_image)
      self.assertTrue(image.dtype == 'uint16')

