# RESPUESTAS RELACIONADAS A SQL

## 1.	Describa qué es una base de datos relacional.

Es un conjunto de datos organizados de la información sobre un temá especifico, se almacenan usando un sistema (Conjunto de tablas). Para las base de datos relaciones la información se organiza en tablas y evitan que los datos se repitan (consistencia), donde tenemos un identificador unico para cada registro, que nos permiten consultarlos cuando nosotros los necesitemos.

## 2.	Describa las 3 formas normales del diseño de bases de datos relacionales.

1. Diseño conceptual:
Se dibujan las entidades y sus relaciones. Consiste en definir las entidades y las relaciones entre ellos de forma abstracta, sin centrarnos en un modelo en especifico. Como resultado tenemos el esquema conceptual de la base de datos.

2. Diseño Lógico:
Se crean las tablas del diseño conceptual y se normalizan los datos, para se insentarán en la base de datos. Aquí pasamos de esquemas de entidad-relación  a un esquema de relaciones.

3. Diseño Físico:
Se definen los tipos de datos e indices, aquí se desarrollan los programas de SQL. Consiste en diseñar las instrucciones necesarias para un DBA (Administrador de Base de datos) pueda implementar una base de datos sin ambiguedad.

## 3.	Enuncie 4 los tipos de datos comunes en SQL y de ejemplos de cómo usar cada uno de ellos.

Conozco los siguientes tipos de datos en SQL:

- Numerico:
Utilizamos este tipo de dato, para almacenar valores númericos en nuestros registros de la base de datos, como ejemplo, definimos una tabla de usuarios donde una columna es la edad de un usuario.

- Caracter o Cadenas:
Utilizamos este tipo de dato, para almacenar un caracter o una cadena de caracteres con diferentes longitudes, como ejemplo, utilizando la misma tabla de usuario, podemos crear una columna del correo electrónico del usuario, donde dicho registro se almacena dicho valor en forma de cadena, pudiera ser el nombre del usuario.

- Fecha o tiempo:
Utilizamos este tipo de datos, para marcas temporales de los datos, donde queremos un registro de fecha, como ejemplo podemos tener una columna de creación del registro del usuario.

- Binario:
Podemos utilizar este tipo de dato para almacenar información de forma binaría, que pueden ser archivos, pasandolo en formato binario. Un ejemplo podría ser la imagen de perfil de un usuario.

Cabe resaltar que es un resumen, y cada tipo podría contener otros subtipos, pero no se toca o se explorá para mantener la respuesta simple.

## 4.	¿Qué diferencia tiene una llave primaria y una llave foránea?

Para poder relacionar tables, debemos poder identificar cada uno de los registros de manera única. No podemos realizar esto debido a que podríamos tener registros duplicados.

Las llaves primarias permiten identificar de manera única cada uno de los registros de una tabla. Se puede utilizar un registro que nunca se repita. Es usual que se le añada un campo adicional del identificador de tipo entero que se incrementa en uno cada nuevo registro.

Para las llaves foroneas, representan la relación que pudiera haber entre dos tablas.

La diferencia es que la llave primaria es el identificador único para cada registro de una tabla y la llave foránea es para establecer la relación entre una Tabla A y otra Table B.

## 5.	¿Cuál es la diferencia entre un inner join y un left join? Descríbalo con teoría de conjuntos.

Un inner join relaciona dos tablas, trayendo todos los campos de estas tablas, cuando una condición de relación se cumpla. Dado un conjunto universal, tenemos un cojunto A y B un inner join es el conjunto formado por todos los elementos formados por todos los elementos comunes, es decir los conjuntos que son comunes al conjunto A y B.

![Imagen de conjunto 1](/assets/sql-2.png)


Con respecto al left join es la relación de dos tablas siempre y cuando se cumpla la condición, pero este traerá todos los registros de la tabla de la izquierda y únicamente aquellos registros que cumplan con la condición de relación con la otra tabla.

![Imagen de conjunto](/assets/sql-1.png)

Diferencia consiste en que uno traera todos los campos de ambos conjuntos que cumplan la condición y en otro solo traera los campos de la tabla del conjunto de la izquierda.

## 6.	¿Para qué funcionan los índices y qué tipos de índices conoces?

Nos sirven para acelerar las busquedas dado que permite la busqueda rápida y eficiente de la fila o filas asociadas a los valores de cada clave. Cuando creamos indices el motor de base de datos, va primero al indice y luego recupera los correspondientes registros de la tabla directamente

Conozco dos tipos de indices:

- Agrupados

- No agrupados

## 7.	Realice una consulta que extraiga los distintos permisos activos de un usuario respecto a su id de usuario y los roles asignados a este, utilice como variable @userId.

Para esta respuesta se creo el script de SQL que se puede consultar en la siguiente liga:

[Ir al Script de respuesta #7](/sql/answer_sql.sql)

## 8.	Realice una consulta que determine si este mismo usuario tiene algún permiso que inicie con el nombre “/catalogs”. Se determinará que tiene el permiso, si el resultado de la consulta trae al menos un registro.

[Ir al Script de respuesta #8](/sql/answer_sql.sql)


### Haga click para Regresar al inicio
[Ir al inicio](../readme.md)
