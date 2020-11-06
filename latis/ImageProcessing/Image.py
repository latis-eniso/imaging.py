import pydicom


class Image(object):
    """
    image container representing an image

    """
    def __init__(self, pixelData, cols:int, rows:int, dataset:pydicom.Dataset):
        self.pixelData = pixelData
        self.height = cols
        self.width = rows
        self.dataset = dataset


    @property
    def dtype(self):
        return self.pixelData.dtype.name
