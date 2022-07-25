# Introducción
Este repositorio contine una seríe de respuestas, para la revisón técnica. Se utiliza este sistema de repositorio para almacenar la doucmentación y el código utilizado.

En esta sección vamos almacenar las respuestas a las preguntas de la 1 a la 6.


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

