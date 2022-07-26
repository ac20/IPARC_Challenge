"""
"""

import numpy as np
from scipy.ndimage import binary_erosion, binary_hit_or_miss


def HMT_R1(img, band):
    """
    """
    img = HMT_ReflectRight(img, 0, band)
    return img


def HMT_R2(img, band):
    """
    """
    img = HMT_ReflectRight(img, 1, band)
    return img


def HMT_R3(img, band):
    """
    """
    img = HMT_ReflectRight(img, 2, band)
    return img


def HMT_R4(img, band):
    """
    """
    img = HMT_ReflectRight(img, 3, band)
    return img


def HMT_ReflectRight(img, col, band):
    """
    """
    m, n, k = img.shape

    img1 = np.pad(img[:, :, band], ((0, 0), (0, n)), constant_values=1)
    struct = np.zeros((1, n))
    struct[0, col] = 1
    struct = np.pad(struct, ((0, 0), (0, n)), constant_values=1)
    img[:, :, band] = binary_erosion(img1, struct, origin=(0, -1*(col+1)))[:, :n]
    return img


def HMT_SE1(img, band):
    m, n, k = img.shape

    struct_fg = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    struct_bg = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # img1 = np.pad(img[:, :, band], 3, constant_values=1)
    if band == 999:
        for band in range(k):
            img[:, :, band] = binary_hit_or_miss(img[:, :, band], struct_fg, struct_bg)
    else:
        img[:, :, band] = binary_hit_or_miss(img[:, :, band], struct_fg, struct_bg)
    return img


def HMT_SE2(img, band):
    m, n, k = img.shape

    struct_bg = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    struct_fg = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    # img1 = np.pad(img[:, :, band], 3, constant_values=0)
    if band == 999:
        for band in range(k):
            img[:, :, band] = binary_hit_or_miss(img[:, :, band], struct_fg, struct_bg)
    else:
        img[:, :, band] = binary_hit_or_miss(img[:, :, band], struct_fg, struct_bg)
    return img


if __name__ == "__main__":
    img = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0]]).reshape((4, -1, 1))
    print(img.reshape((4, -1)))
    img = HMT_R1(img, 0)
    print(img.reshape((4, -1)))

    img = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0]]).reshape((4, -1, 1))
    img = HMT_R2(img, 0)
    print(img.reshape((4, -1)))

    img = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0]]).reshape((4, -1, 1))
    img = HMT_R3(img, 0)
    print(img.reshape((4, -1)))

    img = np.array([[1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0]]).reshape((4, -1, 1))
    img = HMT_R4(img, 0)
    print(img.reshape((4, -1)))

    img = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]).reshape((3, 3, 1))
    print(img.reshape((3, 3)))
    img = HMT_SE1(img, 0)
    print(img.reshape((3, 3)))

    img = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]]).reshape((3, 3, 1))
    print(img.reshape((3, 3)))
    img = HMT_SE1(img, 0)
    print(img.reshape((3, 3)))

    img = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]).reshape((3, 3, 1))
    print(img.reshape((3, 3)))
    img = HMT_SE2(img, 0)
    print(img.reshape((3, 3)))
