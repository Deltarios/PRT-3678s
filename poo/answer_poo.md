# RESPUESTAS RELACIONADAS A PROGRAMACION ORIENTADA A OBJECTOS EN C#

## 11.	¿Qué es una clase?
Las clases son plantillas para la creación de objectos (Atributos y Métodos). Cada vez que creamos un objecto usaremos la clase (plantilla) para crearlo, pues define sus atributos y métodos.

## 12.	¿Qué es una instancia?
Es el proceso de crear un objecto a partir de una clase, por lo que a cada objecto creado se le puede llamar instancia. Con una sola clase podemos crear cientas instancias sin tener que reescribir el código para cada uno de ellas.

## 13.	Describa qué es la herencia y de un ejemplo básico.

Es el proceso en el cual las clases hijas heredan los atributos y métodos de las clases padre.

Ejemplo:

Creamos un clase Mascota que tiene diferentes atributos como, nombre, dueño_id, tamaño, color, edad y pueda tener diferentes métodos como Moverse, Comer, Dormir etc...

Pero creamos diferentes clases para diferentes tipos de macotas, como Perro, Gato, Pez, etc... al estas clases heredar de la mismo padre, heredan sus atributos y funciones.

~~~
class Mascota {
    private String nombre;
    private int dueno_id;
    private double tamano;
    private int edad;
    private String color;

    Mascota();

    public moverse() {
        print('Se movio')
    }

    public comer() {
        print('Comiendo...')
    }

    public dormir() {
        print('Estoy durmiendo')
    }
}


class Perro extends Mascota {}

class Gato extends Mascota {}

class Pez extends Mascosta {}

Perro perro = new Perro();
Gato gato = new Gato();
Pez pez = new Pez();

perro.comer();
gato.dormir();
pez.moverse();
~~~