from functools import reduce
from typing import List
from Models import AlphabetSoup
from Models import Word
from Enum import Position


def main():
    words: List[Word] = [Word(word='Buho', position= Position.VERTICAL.value), Word(word='Canguro', position= Position.HORIZONTAL), Word(word='Jirafa', position= Position.DIAGONAL.value)]
    totalWord: int = sum(c.lenght for c in words)
    alphabetSoup = AlphabetSoup(words=words, size=10)
    print('Busque las siguientes parabaras en la sopa de letras siguiente:')
    print(','.join(w.word for w in words))
    alphabetSoup.draw_soup()

main()
