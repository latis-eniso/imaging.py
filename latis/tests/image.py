import os
from unittest import TestCase
from ..ImageProcessing.ImageIO import ImageIO
from ..ImageProcessing.Image import Image

file_dir = os.path.dirname(os.path.realpath('__file__'))
test_image = file_dir + '/test_images/image-000002.dcm'


class ImageTests(TestCase):
    def test_image_loading(self):
        image = ImageIO.loadImage(test_image)
        self.assertTrue(isinstance(image, Image))

    def test_image_has_pixel_data(self):
        image = ImageIO.loadImage(test_image)
        self.assertTrue(isinstance(image.pixelData, Image))
