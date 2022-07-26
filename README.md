# IPARC_Challenge

Solution for Cat A Task-1

    python Main.py --input ./Dataset/CatA/Task1.json --prog Process Create_Copy[0] Bottom_HalfPlane_Closing[1] Change_Colour1 Top_HalfPlane_Closing[1] Change_Colour1 Left_HalfPlane_Closing[1] Change_Colour1 Right_HalfPlane_Closing[1] Change_Colour1 Change_Colour2

Solution for Cat A Task-2

    python Main.py --input ./Dataset/CatA/Task2.json --prog Process Create_Copy[1] Pad[0,3,0,0] Shift_Down[1] Shift_Down[1] Shift_Down[1] Change_Colour2

    

Notes:
------

1. `Process` makes the input into multi-banded image where each band belongs to one colour and is a binary image.
2. `<Primitive_Name>[i]` applies the primitive to band `i`.
3. `Create_Copy[i]` copies band `i` into a new colour.
4. `Change_Colouri` are the most in-elegant of these operators at present. No simple way yet to phrase these.
5. Each primitive itself can be a combination of other primitives. This is acheived using a `-` symbol inbetween primitives. For example, the solution for Task-1 can also be written as 

        python Main.py --input ./Dataset/CatA/Task1.json --prog Process Create_Copy[0] Bottom_HalfPlane_Closing[1]-Change_Colour1 Top_HalfPlane_Closing[1]-Change_Colour1 Left_HalfPlane_Closing[1]-Change_Colour1 Right_HalfPlane_Closing[1]-Change_Colour1 Change_Colour2

    Where, `<?>HalfPlane_Closing[1]-ChangeColor1` is a higher-order primitive.

6. Although not used yet `IntEndo-<Primitives>` and `UnionEndo-<Primitives>` construct endomorphisms. 

