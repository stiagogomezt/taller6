#matplotlib es una biblioteca de python para realizar graficos cientificos
import numpy as np 
import matplotlib.pyplot as plt
#biblioteca esta organizada por modulos 
#crear un arreglo de 1 diemnsion 100 elemntos quiespaciados desde 0 a 2pi

X= np.linspace(0,2*np.pi,100)
Y= np.sin(X)

#usar matplotlib para definir el tamaño de la figura 
plt.figure(figsize=(8,4))
plt.title("grafico cientifico")
plt.plot(X,Y)
plt.show()