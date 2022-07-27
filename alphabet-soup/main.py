from typing import List
from src.app.Data.Models import AlphabetSoup
from src.app.Data.Models import Word
from src.app.Data.Enum import Position

# Funcion principal de program.
def main():
    # Creamos la lista de palabras
    words: List[Word] = [
    Word(word='Buho', position= Position.VERTICAL), 
    Word(word='Canguro', position= Position.HORIZONTAL), 
    Word(word='Jirafa', position= Position.DIAGONAL)
    ]
    totalWord: int = sum(c.lenght for c in words)
    # Creamos nuestro objecto con las palabras y el tamaño deseado.
    alphabetSoup = AlphabetSoup(words=words, size=15)
    print('Busque las siguientes parabaras en la sopa de letras siguiente:')
    print(','.join(w.word_raw for w in words))
    # Dibujamos nuestra sopa de letras.
    alphabetSoup.draw_soup()

# Se llama a executar la función
main()
