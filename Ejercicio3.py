'''

'''

#importo las librerias necesarias para poder graficar 
import matplotlib.pyplot as plt#Uso de la libreria matplotlib
import numpy as np #Uso de la libreria numpy
a= lambda x: x**2-x+1 # primera fucnion a graficar
b= lambda x: 2/x-1# segunda fucnion a graficar

#escribo los valores tanto para x, y y los intervalos entre ellos
x=np.linspace(-10,10,100) #determino  rango de la grafica  en la 
                            #coordenada x y el numero de iteraciones
g1=a(x)
g2=b(x)
plt.plot(x,g1, color="green")# imprime grafica 1
plt.plot(x,g2, color="red")# imprime grafica 2
plt.show() #imprime las graficas en la misma pantalla
