# Regresión basada en el indice de Libertad Económica

## ¿Existe una relación entre el nivel de libertad económica en un país y su PBI per capita?

Para responder esta pregunta, utilizaremos diferentes regresiones que tomarán como variable dependiente (es decir, la que queremos explicar) al PBI per capita con paridad del poder adquisitivo y como variable independiente o explicativa al punteje de libertad económica de la fundación Heritage.

Todos los datos fueron extraídos de: https://www.heritage.org/index/excel/2021/index2021_data.xls

Para este analisis utilizaremos Python y los modulos numpy, Pandas, statsmodel y matplotlib.

En primer lugar, utilizamos pandas para importar los datos y convertirlos en un dataframe de pandas. Luego la limpiamos de aquellos países de los que no contamos con la información suficiente. Si abrimos la variable en la que guardamos estos países, vemos que los eliminados son 6: Irak, Libya, Liechtenstein, Somalia, Syria y Yemen.

Después de esto, vamos a crear un scatterplot para ver si podemos ver a simple vista una relación en los datos.

![](images/scatterplot.png)

Podemos ver claramente que a medida que aumenta el puntaje de libertad económica, aumenta el PBI per capita. Ademas, tenemos varios outliers que pueden tener una influencia desmesurada en el resultado de nuestra regresión, marcados como puntos azules. Estos puntos serán eliminados para que no incidan en nuestros resultados



Los limites fueron elegidos con el siguiente criterio:

Limite Superior = Q3 + 1,5*IQR

Limite Inferior = Q1 – 1,5*IQR

Con:

Q1 = Cuartil 1, punto que contiene el 25% de los valores
Q3 = Cuartil 3, punto que contiene el 75% de los valores
IQR = Rango intercuartil, resultado de restar Q3 a Q1

Luego de todo esto, comencemos con una regresión lineal simple.

Asignamos los valores de PBI per capita a la variable ‘y’ a explicar y el puntaje de  libertad económica a la variable ‘x’ explicativa. Utilizamos el modulo statsmodels para realizar la regresión y ploteamos los resultados asi como también los residuos:

![]("images/linear regression.png")

Resultados de la Regresión:

|    Conceptos         |      Detalle       | 
| -------------------- |:------------------:|
|  Variable Dependiente  |PBI per Cápita (PPP)|
|  Nº de Observaciones   |         171        |
|  R²                    |        0.638       |
|  Prob (F-statistic)   |    2.31e-39        |


![]("images/linear regression 1.png")

Podemos ver que nuestro R² es razonable y la correlación es estadisticamente significativa. Sin embargo, analizando mas detalladamente los residuos, se aprecia que estos tienen una relación no lineal. Esto quiere decir, que una regresión con otra forma podría ajustarse mejor a nuestros datos.

Probamos entonces con una regresión cuadratica, añadiendo un termino mas a la ecuación, que serán los puntajes de libertad económica elevados al cuadrado.

Corremos la regresión y tenemos:

![]("images/quad regression.png")

Resultados de la Regresión:

|   Conceptos   |    Detalle
|--------------|------------
|   R²   |    0,817   
|   R² ajustado   | 0,815
|   Durbin-Watson   |   2,131
|   Prob (F-statistic)   | 4.08e-63





