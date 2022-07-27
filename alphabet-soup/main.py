from operator import attrgetter
from typing import List
from src.app.Data.Models import AlphabetSoup
from src.app.Data.Models import Word
from src.app.Data.Enum import Position


def check_size_matrix(words: List[Word]) -> int:
    """ Función para check el tamaño minimo de la matrix en función del tamaño de la palabra más grande, por defecto si el tamaño es igual o menor a 15 este valor se mantendra.

    Args:
        words (List[Word]): Lista de palabras.

    Returns:
        int: Devuelve el tamaño minimo para la matrix.
    """    
    size: int = max(words, key=attrgetter('lenght')).lenght
    if (size > 15):
        return size + 4
    else:
        return 15


def main():
    """Función principal del programa.
    """    
    # Creamos la lista de palabras
    words: List[Word] = [
    Word(word='Buho', position= Position.VERTICAL), 
    Word(word='Canguro', position= Position.HORIZONTAL), 
    Word(word='Jirafa', position= Position.DIAGONAL)
    ]
    # Creamos nuestro objecto con las palabras y el tamaño deseado.
    sizeMinimum: int = check_size_matrix(words)
    alphabetSoup = AlphabetSoup(words=words, size=sizeMinimum)
    print('Busque las siguientes palabras en la sopa de letras siguiente:')
    print(','.join(w.word_raw for w in words))
    # Dibujamos nuestra sopa de letras.
    alphabetSoup.draw_soup()

# Se llama a executar la función
main()
