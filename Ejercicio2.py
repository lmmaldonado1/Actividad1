'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


import numpy as np # uso de la libreira numpy
print("Programa para calcular la inversa de matrices de dimensión 2x2")
print("Ingrese los valores de la matriz: ") # Ingreso los valores para individuales 
a=float(input("Ingrese un valor para a"))
b=float(input("Ingrese un valor para b"))
c=float(input("Ingrese un valor para c"))
d=float(input("Ingrese un valor para d"))
mtz =np.array([[a,b],[c,d]])#
print("Los datos de la matriz son  ")# muesto en pantalla los datos en forma de matriz
print(mtz)
mtzI=np.linalg.inv(mtz) # formula para caclular la inverza
print("La matriz invertida es: ")# muesto en pantalla la matriz inverza
print(mtzI)
