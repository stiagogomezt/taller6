#taller Numpy: numpy es una biblioteca para realizar calculos numericos en arreglos n dimesionales 
#Crear un ndarray, arreglo de dos dimensiones de unas lista
import numpy as np 
A= np.array([[1,5],[2,9]])
B =np.array([[2,3],[3,6]])
#producto punto
C=np.dot(A,B)
print(C)
#solucion de un sistema de ecuaciones lineales que se puedan expresar con numpy
m_solucion= np.array([5,17])
m=np.linalg.solve(A,m_solucion)
print(m)


#valores propios y vectores propios 
