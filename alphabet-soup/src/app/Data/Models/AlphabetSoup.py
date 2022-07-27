from typing import List
from .Word import Word
from ..Enum import Position
from random import shuffle, choice, randint
import string
import numpy as np

class AlphabetSoup:
    """ Clase AlphabetSoup. Creación de Sopa de letras.
    """    
    size: int
    words: List[Word]

    def __init__(self, words: List[Word], size: int = 10) -> None:
        """Contructor para la clase AlphabetSoup.

        Args:
            words (List[Word]): Lista de palabras
            size (int, optional): Tamaño de la matriz de letras. Defaults to 10.
        """        
        self.words = words
        self.size = 10 if size <= 0  else size

    def remplace_letter(self, letter: int) -> int:
        """Método para remplazar una letra por otra, cuando se encuentra O -> 0, I -> 1.

        Args:
            letter (int): Letra por remplazar.

        Returns:
            int: La nueva letra encuentrada.
        """        
        if letter == 79:
            return 48
        elif letter == 108:
            return 49
        else:
            return letter
        
    def generate_soup(self) -> List[str]:
        """ Método para generar una matriz de letras aletorias simple.

        Returns:
            List[str]: Devuelve una matriz de letras aletorias.
        """        
        letters: List = []
        for _ in range(self.size * self.size):
            letter = ord(choice(string.ascii_letters))
            letters.append(self.remplace_letter(letter))
        shuffle(letters)
        return np.reshape(letters,(self.size, self.size))

    def draw_soup(self):
        """ Método para dibujar en consola la matriz de letras.
        """        
        soup = self.generate_soup()
        soup_with_words = self.insert_words(soup=soup, words=self.words)
        for s in soup_with_words:
            print(' '.join([chr(a) for a in s]))

    def insert_words(self, soup: List, words: List[Word]) -> List:
        """ Método para insertar una lista de palabras a la matriz de letras.

        Args:
            soup (List): Matriz de letras
            words (List[Word]): Lista de palabras que se van insertar.

        Returns:
            List: Matriz de letras con las palabras insertadas.
        """        
        for w in words:
            if w.position == Position.HORIZONTAL:
               x, y, soup = self.set_position(w.word, soup, 1, 0)
            elif w.position == Position.VERTICAL:
                x, y, soup = self.set_position(w.word, soup, 0, 1)
            else:
                x, y, soup = self.set_position(w.word, soup, 1, 1)
        return soup

    def set_position(self, word: str, soup: List, h: int, v: int) -> tuple:
        """ Funcion para establecer la posición de las palabras.

        Args:
            word (str): Palabra que se insertará
            soup (List): Matriz de letras
            h (int): Poderación horinzontal entre 0 - 1 (Desactivado - Activado)
            v (int): Poderación vertical entre 0 - 1 (Desactivado - Activado)

        Returns:
            tuple: Devuelve la nueva matriz con la palabra insertada.
        """        
        x: int = randint(0, self.size - len(word) * (1 * h) - 1)
        y: int = randint(0, self.size - len(word) * (1 * v) - 1)
        for i, c in enumerate(word):
            soup[y + (i * v)][x + (i * h)] = ord(c)
        return (x, y, soup)