#!/usr/bin/env python

import ctypes as C
math = C.CDLL('./libmymath.so')

#numeros

math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]
print math.add_int(3, 4)

math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
print math.add_float(3, 4)


tres = C.c_int(3)
cuatro = C.c_int(4)
res = C.c_int()
math.add_int_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
print res.value

tres = C.c_float(3)
cuatro = C.c_float(4)
res = C.c_float()
math.add_float_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
print res.value

#vectores

in1 = (C.c_int * 3) (1, 2, -5)
in2 = (C.c_int * 3) (-1, 3, 3)
out = (C.c_int * 3) (0,0,0)
math.add_int_array(C.byref(in1), C.byref(in2), C.byref(out),3)
print out[0],out[1],out[2]


math.dot_product.restype = C.c_float
in1 = (C.c_float * 3) (1, 2, -5)
in2 = (C.c_float * 3) (-1, 3, 3)

out = math.dot_product(C.byref(in1), C.byref(in2),3)
print math.dot_product(C.byref(in1), C.byref(in2),3)


