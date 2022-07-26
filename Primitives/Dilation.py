"""
"""

import numpy as np
from scipy.ndimage import binary_dilation


def Dilation_SE1(img, band):
    m, n, k = img.shape

    struct = np.array([[1, 0, 0, 0, 1],
                       [0, 1, 0, 1, 0],
                       [0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0],
                       [1, 0, 0, 0, 1]])
    if band == 999:
        for band in range(k):
            img[:, :, band] = binary_dilation(img[:, :, band], struct)
    else:
        img[:, :, band] = binary_dilation(img[:, :, band], struct)
    return img


def Dilation_SE2(img, band):
    m, n, k = img.shape

    struct = np.array([[0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0],
                       [1, 1, 0, 1, 1],
                       [0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0]])
    if band == 999:
        for band in range(k):
            img[:, :, band] = binary_dilation(img[:, :, band], struct)
    else:
        img[:, :, band] = binary_dilation(img[:, :, band], struct)
    return img


if __name__ == "__main__":
    img = np.zeros((5, 5, 1))
    img[2, 2] = 1
    print(img.reshape((5, 5)))
    img = Dilation_SE1(img, 0)
    print(img.reshape((5, 5)))

    img = np.zeros((5, 5, 1))
    img[2, 2] = 1
    img = Dilation_SE2(img, 0)
    print(img.reshape((5, 5)))
