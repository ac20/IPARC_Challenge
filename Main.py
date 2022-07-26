#!/usr/bin/env python
"""

run ./Main.py --input <input_name>.json -- output <output_name>.json --program f1 f2 f3 ... fn

** Here each fi denotes a primitive. 

Notes:
------
** We consider the input image as k-binary images where each binary image
denotes a different color. So, we use a 3 dim binary array of size (n x m x k)
to denote the binary image. Hence the first primitive is ALWAYS preprocess
Accordingly the last primitive is a Change_Colour which resolves conflicts
if any.



"""

import numpy as np
import pdb
from matplotlib import pyplot as plt
import json
import re

import argparse

from Primitives import HalfPlane_Closings, Shift_Ops, HitorMissTransforms, Dilation, Resize, Change_Colour


def Process(img, *args):
    n, m = img.shape
    num_colors = np.max(img)+1
    img_cpy = np.zeros((n, m, num_colors))
    for color in range(num_colors):
        img_cpy[:, :, color] = (img == color)*1
    return img_cpy


def CreateCopy(img, band, *args):
    n, m, k = img.shape
    img1 = np.array(img, copy=True)
    img2 = np.array(img[:, :, band], copy=True).reshape((n, m, 1))
    img = np.concatenate((img1, img2), axis=-1)
    return img


def Intersection(img1, img2, *args):
    """
    """
    return np.logical_and(img1, img2)*1


def Union(img1, img2, *args):
    """
    """
    return np.logical_or(img1, img2)*1


dict_primitives = {
    'Bottom_HalfPlane_Closing': HalfPlane_Closings.Bottom_HalfPlane_Closing,
    'Top_HalfPlane_Closing': HalfPlane_Closings.Top_HalfPlane_Closing,
    'Left_HalfPlane_Closing': HalfPlane_Closings.Left_HalfPlane_Closing,
    'Right_HalfPlane_Closing': HalfPlane_Closings.Right_HalfPlane_Closing,
    'Shift_Up': Shift_Ops.Shift_Up,
    'Shift_Down': Shift_Ops.Shift_Down,
    'Shift_Right': Shift_Ops.Shift_Right,
    'Shift_Left': Shift_Ops.Shift_Left,
    'HMT_R1': HitorMissTransforms.HMT_R1,
    'HMT_R2': HitorMissTransforms.HMT_R2,
    'HMT_R3': HitorMissTransforms.HMT_R3,
    'HMT_R4': HitorMissTransforms.HMT_R4,
    'HMT_SE1': HitorMissTransforms.HMT_SE1,
    'HMT_SE2': HitorMissTransforms.HMT_SE2,
    'Dilation_SE1': Dilation.Dilation_SE1,
    'Dilation_SE2': Dilation.Dilation_SE2,
    'Crop': Resize.Crop,
    'Pad': Resize.Pad,
    'Change_Colour': Change_Colour.Change_Colour_default,
    'Process': Process,
    'Change_Colour1': Change_Colour.Change_Colour1,
    'Change_Colour2': Change_Colour.Change_Colour2,
    'Change_Colour3': Change_Colour.Change_Colour3,
    'Create_Copy': CreateCopy
}

"""
Parse the input arguments.
"""

parser = argparse.ArgumentParser(description="Run the program on <input_name>.json and get <output_name>.json")
parser.add_argument('--input', dest='f_input', action='store', help='Input file name. Should be *.json file.')
parser.add_argument('--output', dest='f_output', action='store', help='Output file name. Should be *.json file.')
parser.add_argument('--prog', dest='program', action='store', nargs="*", help='A sequence of primitives separated by <space>')

args = parser.parse_args()


def apply(prog, img, *args):

    if prog.startswith("IntEndo"):
        list_ops = prog.split("-")
        img_cpy = np.array(img, copy=True)
        for z in list_ops[1:]:
            out = re.split('[\W]', z)
            fn_name = out[0]
            if len(out) > 1:
                a = int(out[1])
            else:
                a = None
            img = dict_primitives[fn_name](img, a)
        img = Intersection(img, img_cpy)

    elif prog.startswith("UnionEndo"):
        list_ops = prog.split("-")
        img_cpy = np.array(img, copy=True)
        for z in list_ops[1:]:
            out = re.split('[\W]', z)
            fn_name = out[0]
            if len(out) > 1:
                a = int(out[1])
            else:
                a = None
            img = dict_primitives[fn_name](img, a)
        img = Union(img, img_cpy)

    else:
        list_ops = prog.split("-")
        img_cpy = np.array(img, copy=True)
        for z in list_ops:
            out = re.split('[\W]', z)
            fn_name = out[0]
            if len(out) > 2:
                args = tuple([int(x) for x in out[1:-1]])
                img = dict_primitives[fn_name](img, *args)
            elif len(out) == 2:
                args = int(out[1])
                img = dict_primitives[fn_name](img, args)
            else:
                args = None
                img = dict_primitives[fn_name](img, args)
    return img


with open(args.f_input) as f:
    data = json.load(f)
print("Saw {} examples...".format(len(data)))
print("There are {} sequence of primitives...".format(len(args.program)))

out_pred = []
for ind_image in range(len(data)):
    inp = data[ind_image]['input']
    out_gt = data[ind_image]['output']

    inp_process = np.array(inp, dtype=np.int32, copy=True)
    for prog in args.program:
        inp_process = apply(prog, inp_process)
    inp_process = [[int(y) for y in x] for x in inp_process]
    data[ind_image]['out_pred'] = inp_process


if args.f_output is None:
    fname = args.f_input
    fname = fname.replace("/", "_")
    fname = fname.replace("Dataset", "")
    fname = fname.replace("._", "./temp/")
    with open(fname, "w") as f:
        f.write(json.dumps(data))
