#Para Type annotation
from typing import List

#Pilha de livros com type annotation
stack_of_books: List[str] = []  # {1}
#Adicionando livros no topo da pilha
stack_of_books.append('Livro 1')  # {2}
stack_of_books.append('Livro 2')  # {2}
stack_of_books.append('Livro 3')  # {2}

try:
    #Obtendo o elemento mais novo
    book_1 = stack_of_books.pop()  # Livro 3 {3}
    print(book_1)  # Livro 3

    book_2 = stack_of_books.pop()  # Livro 2 {3}
    print(book_2)  # Livro 2

    book_3 = stack_of_books.pop()  # Livro 1 {3}
    print(book_3)  # Livro 1

    # IndexError: pop from empty list
    book = stack_of_books.pop()  # Não há mais livros {4}
    print(book)  # Seu código não chegará aqui
except IndexError:
        print('chegou ao fim.')