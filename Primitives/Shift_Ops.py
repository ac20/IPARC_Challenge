"""
"""

import numpy as np
from skimage.morphology import binary_dilation


def Shift_Down(img, band):
    """
    """
    footprint = np.array([[0], [0], [1]])
    img[:, :, band] = binary_dilation(img[:, :, band], footprint)
    return img


def Shift_Up(img, band):
    """
    """
    footprint = np.array([[1], [0], [0]])
    img[:, :, band] = binary_dilation(img[:, :, band], footprint)
    return img


def Shift_Right(img, band):
    """
    """
    footprint = np.array([[0, 0, 1]])
    img[:, :, band] = binary_dilation(img[:, :, band], footprint)
    return img


def Shift_Left(img, band):
    """
    """
    footprint = footprint = np.array([[1, 0, 0]])
    img[:, :, band] = binary_dilation(img[:, :, band], footprint)
    return img


if __name__ == "__main__":

    print("Checking the functions on simple example.")

    img = np.array([[1, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0]]).reshape((3, 5, 1))
    print("Original\n", img.reshape((3, 5)))
    img = Shift_Down(img, 0)
    print("Shift Down\n", img.reshape((3, 5)))
    img = Shift_Up(img, 0)
    print("Shift Up\n", img.reshape((3, 5)))
    img = Shift_Right(img, 0)
    print("Shift Right\n", img.reshape((3, 5)))
    img = Shift_Left(img, 0)
    print("Shift Left\n", img.reshape((3, 5)))
