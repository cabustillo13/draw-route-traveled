from xml.dom import minidom
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

#Leer archivo con coordenadas GPS
xmldoc = minidom.parse('prueba.gpx')

#Listar los archivos
itemlist = xmldoc.getElementsByTagName('trkpt')
#Contar la cantidad total de archivos
cantidad=len(itemlist)

#Asignar elemento del archivo a su respectiva coordenada espacial
x = list()
y = list()

for s in itemlist:

    x.append(float(s.attributes['lat'].value))
    y.append(float(s.attributes['lon'].value))
   
#Graficar ruta recorrida en 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y,color="red")
plt.show()

#Graficar ruta recorrida en 2D
plt.plot(x,y,color="red")
plt.axis('off')
plt.savefig("Ejemplo.png", bbox_inches='tight',transparent=True)
plt.show()
