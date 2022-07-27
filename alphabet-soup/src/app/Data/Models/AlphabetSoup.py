from typing import List
from .Word import Word
from ..Enum import Position
from random import shuffle, choice, randint
import string
import numpy as np

class AlphabetSoup:
    size: int
    words: List[Word]

    def __init__(self, words: List[Word], size: int = 10) -> None:
        self.words = words
        self.size = 10 if size <= 0  else size

    def remplace_letter(self, letter: int) -> int:
        if letter == 79:
            return 48
        elif letter == 108:
            return 49
        else:
            return letter
        
    def generate_soup(self) -> List[str]:
        letters: List = []
        for _ in range(self.size * self.size):
            letter = ord(choice(string.ascii_letters))
            letters.append(self.remplace_letter(letter))
        shuffle(letters)
        return np.reshape(letters,(self.size, self.size))

    def draw_soup(self):
        soup = self.generate_soup()
        soup_with_words = self.insert_words(soup=soup, words=self.words)
        for s in soup_with_words:
            print(' '.join([chr(a) for a in s]))

    def insert_words(self, soup: List, words: List[Word]) -> List:
        for w in words:
            if w.position == Position.HORIZONTAL:
               x, y, soup = self.set_position(w.word, soup, 1, 0)
            elif w.position == Position.VERTICAL:
                x, y, soup = self.set_position(w.word, soup, 0, 1)
            else:
                x, y, soup = self.set_position(w.word, soup, 1, 1)
        return soup

    def set_position(self, word: str, soup: List, h: int, v: int) -> tuple:
        x: int = randint(0, self.size - len(word) * (1 * h) - 1)
        y: int = randint(0, self.size - len(word) * (1 * v) - 1)
        for i, c in enumerate(word):
            soup[y + (i * v)][x + (i * h)] = ord(c)
        return (x, y, soup)