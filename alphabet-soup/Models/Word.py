from Enum import Position

class Word:
    def __init__(self, word: str, position: Position) -> None:
        self._word = word if len(word) > 0 else 'Palabra'
        self._position = position
        self._lenght = 0


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