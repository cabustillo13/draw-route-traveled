from xml.dom import minidom
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

#Asignar elemento del archivo a su respectiva coordenada espacial
x = list()
y = list()
z = list()

#Leer archivo con coordenadas GPS
xmldoc = minidom.parse('./Recursos/prueba.gpx')
#Listar los archivos
itemlist = xmldoc.getElementsByTagName('trkpt')
#Contar la cantidad total de archivos
cantidad1=len(itemlist)

#Leer .txt con los valores de las coordenadas
f = open("./Recursos/elevacionLista.txt", "r")
for linea in f:
    z.append(float(linea))
f.close()
cantidad2=len(z)

#Para este caso cantidad1 = cantidad2
for s in itemlist:
    x.append(float(s.attributes['lat'].value))
    y.append(float(s.attributes['lon'].value))
    
#Graficar ruta recorrida en 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, color="red")
plt.show()

#Graficar ruta recorrida en 2D
plt.plot(x,y,color="red")
plt.axis('off')
plt.savefig("Ejemplo.png", bbox_inches='tight',transparent=True)
plt.show()

#Graficar ruta recorrida en 3D con su respectiva elevacion
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, color="red")
plt.show()

#NOTA:
"""Proceso de curado de la elevacion y el tiempo -> No fue un formato admisible en data.gpx ni elevacion.gpx"""
"""Por eso propuse elevacionLista.txt"""
