"""
"""


import numpy as np
import json
import os


def _check(data):
    for i in range(len(data)):
        assert np.all(data[i]['output'] == data[i]['out_pred'])
    print("Passed...")


print("Checking Category A Task 1...")
os.system(
    "python Main.py --input ./Dataset/CatA/Task1.json --prog Process Create_Copy[0] Bottom_HalfPlane_Closing[1] Change_Colour1 Top_HalfPlane_Closing[1] Change_Colour1 Left_HalfPlane_Closing[1] Change_Colour1 Right_HalfPlane_Closing[1] Change_Colour1 Change_Colour2")

with open('./temp/_CatA_Task1.json', "r") as f:
    data = json.load(f)
    _check(data)

print("Checking Category A Task 2...")
os.system("python Main.py --input ./Dataset/CatA/Task2.json --prog Process Create_Copy[1] Pad[0,3,0,0] Shift_Down[1] Shift_Down[1] Shift_Down[1] Change_Colour2")

with open('./temp/_CatA_Task2.json', "r") as f:
    data = json.load(f)
    _check(data)

print("Checking Category A Task 3...")
os.system("python Main.py --input ./Dataset/CatA/Task3.json --prog Process Create_Copy[1] Pad[0,0,0,3] Shift_Right[1] Shift_Right[1] Shift_Right[1] Shift_Right[1] Crop[0,3,4,7] Change_Colour3")

with open('./temp/_CatA_Task3.json', "r") as f:
    data = json.load(f)
    _check(data)


print("Checking Category A Task 4...")
os.system("python Main.py --input ./Dataset/CatA/Task4.json --prog Process UnionEndo-HMT_SE1[999]-Dilation_SE1[999] UnionEndo-HMT_SE2[999]-Dilation_SE2[999] Change_Colour5")

with open('./temp/_CatA_Task4.json', "r") as f:
    data = json.load(f)
    _check(data)
