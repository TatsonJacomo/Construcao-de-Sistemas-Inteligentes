# Crie a classe Leitura com titulo, total_paginas e paginas_lidas.
# Receba os dois primeiros na criação e inicie o terceiro com zero.
# Considere total_paginas um inteiro positivo.

class Leitura:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def avancar(self, quantidade):
        if quantidade <= 0:
            return False
        if quantidade + self.paginas_lidas > self.total_paginas:
            return False
        self.paginas_lidas += quantidade
        return True

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def concluida(self):
        return self.paginas_lidas == self.total_paginas


primeira = Leitura("Primeiro livro", 120)
segunda = Leitura("Segundo livro", 80)

print(primeira.avancar(30))
print(primeira.avancar(100))
print(primeira.avancar(90))

print("Páginas lidas:", primeira.paginas_lidas)
print("Páginas restantes:", primeira.paginas_restantes())
print("Concluída:", primeira.concluida())
print("Segunda leitura:", segunda.paginas_lidas)

print("Chamada concluida() 1:", primeira.concluida())
print("Chamada concluida() 2:", primeira.concluida())

# concluida() apenas compara paginas_lidas com total_paginas.
# Por isso chamá-la duas vezes não altera o progresso.

