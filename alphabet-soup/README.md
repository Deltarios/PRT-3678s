# Ejercicio Técnico "Sopa de Letras"
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)<br>
![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)<br>
![Mantenimiento: Yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)

## Para levantar este proyecto
Nos tenemos que posicionar en la carpeta [alphabet-soup](../alphabet-soup).

Creamos un ambiente virtual para mejor manejo del proyecto con los comandos:

```
python -m virutalenv .venv
```

En caso de no tener el paquete de virutalenv podemos instalarlo en el sistema con el siguiente comando:
```
pip install virtualenv
```

Finalmente ejecutamos el ambiente virutal.

En windows
```
venv\Scripts\activate
```

En mac o linux
```
source venv/bin/activate
```

Una vez en nuestro ambiente virtual instalamos nuestras dependencias mediante:

```
pip install -r requirements.txt
```


Y corremos el programa de main.py:
```
python main.py
```

### Debugger
Para vscode, se puede revisar la configuración de los debugger (python) por si se quiere implementar, esto se encuentran [aquí](.vscode/launch.json)

### Ejemplo de funcionamiento:

![Ejemplo de funcionamiento](../assets/example-code-alphabet-soup.png)

## Se deja a continuación el diagrama de flujo de este proyecto:

![Ejemplo de funcionamiento](../assets/diagrama_alphabet_soup.png)