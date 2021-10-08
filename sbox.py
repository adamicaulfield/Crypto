# Adam Caulfield (ac7717@rit.edu)
# CSCI662 - HW4
# sbox.py
# Completes the affine mmapping step of the sbox


import numpy as np

#b_ini = [0,0,1,0,1,0,0,1] #0A
#b_ini = [0,0,1,1,1,1,0,0] #34
b_ini = [0,0,0,0,0,0,0,1] #01

affMap = [[1,0,0,0,1,1,1,1],
	  [1,1,0,0,0,1,1,1],
	  [1,1,1,0,0,0,1,1],
	  [1,1,1,1,0,0,0,1],
	  [1,1,1,1,1,0,0,0],
	  [0,1,1,1,1,1,0,0],
	  [0,0,1,1,1,1,1,0],
	  [0,0,0,1,1,1,1,1]]

vIncr = [1,1,0,0,0,1,1,0]

tmp = np.matmul(affMap, b_ini)

b = np.add(vIncr, tmp)

b = np.mod(b,2)

#Print as hex
h1 = 8*b[0]+4*b[1]+2*b[2]+b[3]
h2 = 8*b[4]+4*b[5]+2*b[6]+b[7]

hexLetters = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
print(str(hexLetters[h1])+str(hexLetters[h2]))