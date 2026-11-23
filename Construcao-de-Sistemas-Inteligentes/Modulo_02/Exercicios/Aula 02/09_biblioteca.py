# Utilize a classe Livro do exercício 05 e uma lista com três livros de títulos diferentes. Construa um menu:

# 1 - Mostrar livros e disponibilidade
# 2 - Emprestar um livro
# 3 - Devolver um livro
# 0 - Sair

# Nas opções 2 e 3, leia o título e procure o objeto com um for. Considere a correspondência exata entre os textos.

# Se encontrar, chame o método adequado e apresente uma mensagem conforme seu retorno.
# Se não encontrar, informe Livro não encontrado.
# Trate opções desconhecidas com uma mensagem.
# Repita o menu até escolher 0.

# Teste: emprestar um livro disponível, tentar emprestá-lo novamente, devolvê-lo, tentar devolver um livro disponível e procurar um título inexistente.

# As regras de empréstimo devem permanecer nos métodos. O menu fica responsável por receber entradas, localizar o objeto e mostrar os resultados.


class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado:
            return False
        self.emprestado = True
        return True

    def devolver(self):
        if not self.emprestado:
            return False
        self.emprestado = False
        return True


livros = [
    Livro("Python para iniciantes"),
    Livro("Algoritmos em Python"),
    Livro("Estruturas de dados")
]

while True:
    print("\nMenu da biblioteca")
    print("1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Até logo!")
        break

    if opcao == "1":
        for livro in livros:
            status = "emprestado" if livro.emprestado else "disponível"
            print(f"{livro.titulo}: {status}")

    elif opcao == "2":
        titulo = input("Digite o título do livro para emprestar: ")
        encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.emprestar():
                    print(f"Livro '{titulo}' emprestado com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está emprestado.")
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "3":
        titulo = input("Digite o título do livro para devolver: ")
        encontrado = False
        for livro in livros:
            if livro.titulo == titulo:
                encontrado = True
                if livro.devolver():
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está disponível.")
                break
        if not encontrado:
            print("Livro não encontrado.")

    else:
        print("Opção inválida.")