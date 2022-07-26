"""
"""

import numpy as np
from skimage.morphology import binary_closing
import pdb


def Bottom_HalfPlane_Closing(img, band):
    """
    """
    m, n, k = img.shape
    footprint = np.zeros((2*m+1, 2*n+1))
    footprint[m+1:, :] = 1
    img[:, :, band] = binary_closing(img[:, :, band], footprint)
    return img


def Top_HalfPlane_Closing(img, band):
    """
    """
    m, n, k = img.shape
    footprint = np.zeros((2*m+1, 2*n+1))
    footprint[:(m+1), :] = 1
    img[:, :, band] = binary_closing(img[:, :, band], footprint)
    return img


def Right_HalfPlane_Closing(img, band):
    """
    """
    m, n, k = img.shape
    footprint = np.zeros((2*m+1, 2*n+1))
    footprint[:, (n+1):] = 1
    img[:, :, band] = binary_closing(img[:, :, band], footprint)
    return img


def Left_HalfPlane_Closing(img, band):
    """
    """
    m, n, k = img.shape
    footprint = np.zeros((2*m+1, 2*n+1))
    footprint[:, :(n+1)] = 1
    img[:, :, band] = binary_closing(img[:, :, band], footprint)
    return img


if __name__ == "__main__":

    img = np.zeros((9, 9))
    img[7, 1] = 1
    img[3, 2] = 1
    img[5, 4] = 1
    img = img.reshape((9, 9, 1))
    print(img.reshape((9, 9)))
    img = Bottom_HalfPlane_Closing(img, 0)
    print(img.reshape((9, 9)))

    img = np.zeros((9, 9))
    img[7, 1] = 1
    img[3, 2] = 1
    img[5, 4] = 1
    img = img.reshape((9, 9, 1))
    img = Top_HalfPlane_Closing(img, 0)
    print(img.reshape((9, 9)))

    img = np.zeros((9, 9))
    img[7, 1] = 1
    img[3, 2] = 1
    img[5, 4] = 1
    img = img.reshape((9, 9, 1))
    img = Right_HalfPlane_Closing(img, 0)
    print(img.reshape((9, 9)))

    img = np.zeros((9, 9))
    img[7, 1] = 1
    img[3, 2] = 1
    img[5, 4] = 1
    img = img.reshape((9, 9, 1))
    img = Left_HalfPlane_Closing(img, 0)
    print(img.reshape((9, 9)))
