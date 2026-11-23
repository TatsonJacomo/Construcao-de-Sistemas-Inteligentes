# Crie a classe Livro, com os atributos titulo, autor e paginas, recebidos em __init__.

# Crie dois livros diferentes e apresente seus dados. 
# Altere o número de páginas de apenas um deles e mostre os dois novamente.

# Para explicar: quais são a classe, as instâncias e os atributos? 
# A alteração afetou os dois livros?



class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro1 = Livro("Crazy Frog", "Daniel De Almeida", 1390)
livro2 = Livro("O Senhor Valdir", "Valdibras de hahaha", 1200)

print(f"\nAntes da alteração: ")
print(f"Livro 1: {livro1.titulo}, Autor: {livro1.autor}, Páginas: {livro1.paginas}")
print(f"Livro 2: {livro2.titulo}, Autor: {livro2.autor}, Páginas: {livro2.paginas}")

livro1.paginas = 350

print(f"\nApós alteração:")
print(f"Livro 1: {livro1.titulo}, Autor: {livro1.autor}, Páginas: {livro1.paginas}")
print(f"Livro 2: {livro2.titulo}, Autor: {livro2.autor}, Páginas: {livro2.paginas}")
print("\n")