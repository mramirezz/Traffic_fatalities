# Desafio Inicial

Se espera que muestren conocimiento en las siguientes areas:

- Realizar consultas a una base de datos publica alojada en Google Could Plataform
- Trabajar con bases de datos relacionales
- Procesamiento de datos
- Visualización de datos
- Versionado de software

Usando el dataset `nhtsa_traffic_fatalities` desde el proyecto `bigquery-public-data`, y usando la tabla de datos del año 2015. Se pide realizar lo siguiente:

1. Crear y completar un diccionario de datos de la tabla, guardarlo en un archivo de texto separado por comas `.csv` 
Lo siguiente se debe realizar en un jupyter notebook
2. Identificar, usando consultas y con gráficas las siguientes características del dataset: 
   1. Mayor numero de accidentes por estado (`state_name`).
   2. Mayor numero de accidentes por uso de tierra (`land_use`).
   3. Mayor numero de accidentes por empresa de carreteras (`ownership_name`).
   4. Mayor numero de accidentes por carretera (`trafficway_identifier`).
3. Realizar un análisis mensual de accidentes por estado. 
4. Realizar un análisis según la hora del dia. 
   - Ahondar para los estados con mayor cantidad de muertes
5. Finalmente realizar un análisis resaltando la razón entre números de accidentes y conductores ebrios. 

Los resultados deben ser entregados como un repositorio en [github](https://github.com), con una rama de desarrollo  y una de producción, además el repositorio deberá contar con un archivo de requerimientos (requirements.txt) donde se listen las librerías de python relevantes para el desarrollo del análisis y un readme donde se presenten los resultados obtenidos indicando y argumentando todos los descubrimientos que realicen del dataset. 

Para realizar el trabajo en github, les recomiendo la siguiente [guía](https://david-estevez.gitbooks.io/the-git-the-bad-and-the-ugly/content/es/buenas-practicas-al-trabajar-con-git.html), si van a trabajar en grupos, ademas de especificarlo en el readme, cada integrante debe tener su rama de desarrollo y hacer los correspondiente fork y pull request.

