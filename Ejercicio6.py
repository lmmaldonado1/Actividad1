'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import numpy as np
from numpy.lib import math
x=np.pi/3# fucnion para calcular la serie
n=50 #valor en donde se trucala serie
pln=0

for k in range(n):
    pln=pln + (-1)**k*x**(2*k+1) /np.math.factorial(2*k+1)#formula de taylor
    print(k,pln) #impime serie de taylor truncada en 50
    
