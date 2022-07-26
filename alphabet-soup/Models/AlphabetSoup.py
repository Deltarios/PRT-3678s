from typing import List
from .Word import Word
from random import shuffle, choice
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
        for i in soup:
            print(' '.join([chr(a) for a in i]))

    def insert_words(self, soup: List, word: List[Word]) -> List:
        coordinates: List = []
        
        pass 