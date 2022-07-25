# RESPUESTAS RELACIONADAS A ANGULAR

## 16.	¿Qué es un servicio en Angular?
Los componentes de angular no deberían obtener o guardar datos de forma directa, y no deben presentar datos falsos. Deben de sentrarse en presentar la información y delegar el acceso a los datos mediante un servicio.
Los servicios son una manera de compartir información entre clases que no se conocen entre sí.

## 17.	¿Qué es un Pipe?
Usamos los pipe para transformar string, cantidades y fechas y otros datos que se presentán.

Son simples funciones que usan data biding para aceptar un valor de entrada y devolver un valor transformado. Son muy útiles por que se pueden utilizar en toda la aplicación, y solo se requieré declarar un vez.

## 18.	¿Qué es un Componente y qué elementos lo definen?

Los componentes en Angular son el principal bloque de construcción. Cada componente consiste en:

- Un template HTML que declará que se rederizará en la vista.
- Una clase de TypeScript que define el comportamiento.
- Un selector de estilos CSS aplicados en la plantilla.

## 19.	¿Qué es un módulo?
Las aplicaciones de angular son modulares por lo que un modulo es un bloque de código dedicado a una sección de nuestra aplicación, puede contener componentes, servicios y otros archivos. Se pueden importar y exportar funcionalidades para que se utilicen en otros modulos de Angular.

## 20.	Describe qué es lo que haces para incluir en tu proyecto un módulo nuevo o utilería, como por ejemplo ngx-datatable.

Dependiendo del modulo o utilería se procedería a analizar o investigar al respecto, por que si este incluye compatiblidad con Angular nos podría facilitar su utilización en la aplicación.

1. Investigación de la utilería.
2. Intalación mediante NPM u cualquier gestionador de paquetes.
3. Integrar el modulo o utilería a nuestro modulo donde será utilizado. Si se desea que sea utilizado de forma global, se podría integrar al modulo prinicipal. Si se requiere un modulo en especifico, se integra a ese modulo.

