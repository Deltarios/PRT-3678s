from random import randint

from ..Enum import Position

class Word:
    def __init__(self, word: str, position: Position) -> None:
        self._word_raw = word if len(word) > 0 else 'Palabra'
        self._word = self.transform_word(word)
        self._position = position
        self._lenght = 0

    @property
    def word_raw(self):
        return self._word_raw

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, v):
        self._word = v

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, v):
        self._position = v

    @property
    def lenght(self):
        self._lenght = len(self._word)
        return self._lenght

    def transform_word(self, word: str) -> str:
        rotate: int = randint(0, 1)
        if (rotate == 1):
            return ''.join(reversed(word))
        else:
            return word