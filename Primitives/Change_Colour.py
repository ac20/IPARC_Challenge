"""
"""

import pdb
import numpy as np


def Change_Colour_default(img, *args):
    """
    """
    rule = np.array([[0, 0, 0],
                     [0, 1, 1],
                     [1, 1, 1],
                     [1, 0, 1]])

    return Change_Colour(img, rule, keepdims=False)


def Change_Colour1(img, *args):
    """
    The image is assumed to have 3 bands (colors) - 0,1,2

    The final colouring is as follows:
    1) The original set of pixels is colored 1
    2) The proposed extension is colored 2
    3) The rest is colored 0

    Note: It is expected that band 2 has all the proposed pixels, which
    initially is entire background and is refined after each primitive.

    So, the rules are
    [0, 1, 0] -> 1
    [*, 1, 1] -> 2
    rest is mapped to be 0.
    """
    rule = np.array([[0, 0, 0, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 0],
                     [0, 1, 1, 2],
                     [1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [1, 0, 1, 0],
                     [1, 1, 1, 2]])

    return Change_Colour(img, rule)


def Change_Colour2(img, *args):
    """
    The image is assumed to have 3 bands (colors) - 0,1,2

     The final colouring is as follows:
    1) The final answer is colored 1.
    2) The rest is colored 0

    Note: The input to this is expected to have the original pixels in
    band-1, proposed extended pixels in band-2. Union of these two bands
    is to be colored 1 and the rest 0.

    So, the rules are
    [*, 1, 1] -> 1
    [*, 0, 1] -> 1 # This probably will not happen.
    [*, 1, 0] -> 1
    Rest would be 0.


    """
    rule = np.array([[0, 0, 0, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 1],
                     [0, 1, 1, 1],
                     [1, 0, 0, 0],
                     [1, 1, 0, 1],
                     [1, 0, 1, 1],
                     [1, 1, 1, 1]])

    return Change_Colour(img, rule, keepdims=False)


def Change_Colour3(img, *args):
    """
    The image is assumed to have 3 bands (colors) - 0,1,2

    The final colouring is as follows:
    1) The final answer is colored 1.
    2) The rest is colored 0

    Note: The output is the intersection of bands 1 and 3.

    So, the rule is
    [*, 1, *, 1] -> 1
    Rest would be 0.


    """
    rule = np.array([[0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0],
                     [0, 1, 0, 1, 1],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 0, 0, 1, 0],
                     [1, 1, 0, 1, 1],
                     [0, 0, 1, 0, 0],
                     [0, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0],
                     [0, 1, 1, 1, 1],
                     [1, 0, 1, 0, 0],
                     [1, 1, 1, 0, 0],
                     [1, 0, 1, 1, 0],
                     [1, 1, 1, 1, 1]])

    return Change_Colour(img, rule, keepdims=False)


def Change_Colour4(img, *args):
    """
    The image is assumed to have 3 bands (colors) - 0,1,2

     The final colouring is as follows:
    1) The final answer is colored 1.
    2) The rest is colored 0

    Note:

    So, the rules are
    [*, 1, 0] -> 1
    [*, 0, 1] -> 2
    Rest would be 0.


    """
    rule = np.array([[0, 0, 0, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 2],
                     [0, 1, 1, 0],
                     [1, 0, 0, 0],
                     [1, 1, 0, 1],
                     [1, 0, 1, 2],
                     [1, 1, 1, 0]])

    return Change_Colour(img, rule, keepdims=False)


def Change_Colour5(img, *args):
    """
    Return arg max.

    ** Works across different kinds of bands.
    """
    m, n, k = img.shape
    img = k - 1 - np.argmax(img[:, :, ::-1], axis=-1)
    return img


def Change_Colour(img, rule, keepdims=True, *args):
    """
    The rule is a mapping {0,1}^k -> {0,1,2,...k}

    Implemented as n x (k+1) array where $k$ is the number of colors.

    -> row 'i' corresponds to rule 'i'.
    -> Each rule will be of the form  <0,1,0,1...,j>
    -> The last entry denotes the color to assign based on first 'k'
    entries.

    """
    def func(a, rule):
        ind = np.where(np.all(rule[:, :-1] == a.reshape((1, -1)), axis=-1))[0]
        if len(ind) == 0:
            return 0
        elif len(ind) > 1:
            raise Exception("More than two Color_Change rules match the input")
        else:
            return rule[ind[0], -1]

    img = np.apply_along_axis(func, 2, img, rule)
    if keepdims:
        n, m = img.shape
        num_colors = np.max(img)+1
        img_cpy = np.zeros((n, m, num_colors))
        for color in range(num_colors):
            img_cpy[:, :, color] = (img == color)*1
        return img_cpy
    else:
        return img


if __name__ == "__main__":
    img1 = np.array([[0, 1, 0, 1]])
    img2 = np.array([[0, 0, 1, 1]])
    img = np.stack((img1, img2), axis=-1)
    rule = np.array([[0, 0, 0],
                     [0, 1, 1],
                     [1, 1, 2]])

    img = Change_Colour(img, rule)
    print(img)
