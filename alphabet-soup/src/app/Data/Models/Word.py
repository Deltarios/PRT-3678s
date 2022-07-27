from random import randint

from ..Enum import Position

class Word:
    """ Clase para la creación de instancia de tipo Palabras.
    """    
    def __init__(self, word: str, position: Position) -> None:
        """ Contructor para crear instancia de palabras.

        Args:
            word (str): Palabra que se desea crear.
            position (Position): Posición a la que estará la palabra.
        """        
        self._word_raw = word if len(word) > 0 else 'Palabra'
        self._word = self.transform_word(word)
        self._position = position
        self._lenght = 0

    @property
    def word_raw(self):
        """Getter para obtener la palabra sin modificacion.

        Returns:
            _type_: El atributo palabra.
        """
        return self._word_raw

    @property
    def word(self):
        """ Getter para obtener la palabra.

        Returns:
            _type_: La palabra con modificación de orientación.
        """        
        return self._word

    @word.setter
    def word(self, v):
        """Setter para modificar el valor de las palabras.

        Args:
            v (_type_): Valor de la nueva palabra.
        """        
        self._word = v

    @property
    def position(self):
        """Getter para la posición de la palabra.

        Returns:
            _type_: La posición de la palabra.
        """        
        return self._position

    @position.setter
    def position(self, v):
        """Setter para la posición.

        Args:
            v (_type_): Posición nueva que se le desea asignar a la palabra.
        """        
        self._position = v

    @property
    def lenght(self):
        """ Tamaño de la palabra.

        Returns:
            _type_: Devuelve el tamaño de la palabra.
        """
        self._lenght = len(self._word)
        return self._lenght

    def transform_word(self, word: str) -> str:
        """Método para transformar la orientación de la palabra. Se realiza al azar.

        Args:
            word (str): Palabra para cambio de orientación.

        Returns:
            str: Palabra con la orientación modificada al azar.
        """        
        rotate: int = randint(0, 1)
        if (rotate == 1):
            return ''.join(reversed(word))
        else:
            return word