# Regresión basada en el indice de Libertad Económica

## ¿Existe una relación entre el nivel de libertad económica en un país y su PBI per capita?

Para responder esta pregunta, utilizaremos diferentes regresiones que tomarán como variable dependiente (es decir, la que queremos explicar) al PBI per capita con paridad del poder adquisitivo y como variable independiente o explicativa al punteje de libertad económica de la fundación Heritage.

Todos los datos fueron extraídos de: https://www.heritage.org/index/excel/2021/index2021_data.xls

Para este analisis utilizaremos Python y los modulos numpy, Pandas, statsmodel y matplotlib.

En primer lugar, utilizamos pandas para importar los datos y convertirlos en un dataframe de pandas. Luego la limpiamos de aquellos países de los que no contamos con la información suficiente. Si abrimos la variable en la que guardamos estos países, vemos que los eliminados son 6: Irak, Libya, Liechtenstein, Somalia, Syria y Yemen.

Después de esto, vamos a crear un scatterplot para ver si podemos ver a simple vista una relación en los datos.

[](https://github.com/Gabeeh94/Economic-Freedom-Regression/blob/ff025d6a2656057c920f04567a7c4525c4c04acf/images/scatterplot.png)
