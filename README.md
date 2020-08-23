# draw-route-traveled
A partir de la información recolectada en un GPS, marcar la ruta recorrida en un mapa.

# CONTEXTO

De acuerdo con el informe Data never Sleeps, elaborado por el sistema operativo basado en la nube Domo, cada día se crean en Internet más de 2,5 billones de bytes de datos, que van en aumento. Generamos información cuando salimos a caminar y activamos una app que cuente nuestros pasos, distancia, etc. También en el auto cuando hacemos un recorrido.

En este caso propuse darle uso a datos obtenidos de un GPS (se obtuvieron archivos .gpx) de un camino recorrido, interpretar esos datos y graficarlos en el espacio para darnos una idea de lo que se recorrió. Fue todo un desafío por el tipo de dato elegido(especialmente con los atributos "ele" y "time"), pero se logró al final implementarlo de la forma buscada.

# RESULTADOS

* **Imagen real de campo superpuesta a la gráfica obtenida**

![imageninsitu](https://github.com/cabustillo13/draw-route-traveled/blob/master/Ejemplos/EjemploinSitu.png)

* **Imagen 3D de la ruta obtenida a partir de las coordenadas**

![imagen3D](https://github.com/cabustillo13/draw-route-traveled/blob/master/Ejemplos/Ejemplo3D.png)

* **Imagen 3D de la ruta en el espacio con su respectiva elevación para cada punto**

![elevacion](https://github.com/cabustillo13/draw-route-traveled/blob/master/Ejemplos/Elevacion.png)
