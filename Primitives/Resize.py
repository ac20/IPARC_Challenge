"""
"""

import numpy as np
import pdb


def Crop(img, x1, y1, x2, y2):
    """
    Crops the image with corners (x1,y1), (x2,y2)

    Note: This happens across all bands!
    """
    img = img[x1:x2, y1:y2, :]
    return img


def Pad(img, x1, x2, y1, y2):
    """
    Increases the size of the image by padding with 0's

    Note: This happens across all bands!
    """
    img = np.pad(img, ((x1, x2), (y1, y2), (0, 0)), constant_values=0)
    return img
