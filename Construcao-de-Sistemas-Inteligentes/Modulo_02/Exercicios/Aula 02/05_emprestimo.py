# Crie uma classe Livro com titulo e emprestado. O título é recebido na criação; emprestado começa como False.

# emprestar() deve mudar o estado para True e retornar True, desde que o livro ainda não esteja emprestado. Caso contrário, deve retornar False.
# devolver() deve mudar o estado para False e retornar True, desde que exista um empréstimo. Caso contrário, deve retornar False.

# Teste duas tentativas de empréstimo seguidas de duas tentativas de devolução. Mostre os retornos e o estado após cada operação.

# Conferência: os retornos são True, False, True, False.




class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True

        return False

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True

        return False


livro = Livro("Dom Casmurro")


resultado = livro.emprestar()
print("Primeiro empréstimo:", resultado)
print("Está emprestado:", livro.emprestado)


resultado = livro.emprestar()
print("\nSegundo empréstimo:", resultado)
print("Está emprestado:", livro.emprestado)

resultado = livro.devolver()
print("\nPrimeira devolução:", resultado)
print("Está emprestado:", livro.emprestado)


resultado = livro.devolver()
print("\nSegunda devolução:", resultado)
print("Está emprestado:", livro.emprestado)