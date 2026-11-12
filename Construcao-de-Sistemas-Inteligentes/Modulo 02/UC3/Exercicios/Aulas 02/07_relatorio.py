# Utilize a classe Produto e uma lista com três instâncias. 
# Percorra a lista para mostrar nome, estoque e valor em estoque de cada uma.

# Mostre também:

# o valor total em estoque;
# a quantidade de produtos cujo estoque é zero.

# Teste com Produto("Caderno", 10.0, 2), Produto("Caneta", 3.0, 0) e Produto("Borracha", 2.0, 5).

# Resultado esperado: total 30.0 e um produto sem estoque. 
# Repita com uma lista vazia: o total e a contagem devem ser zero.



class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= 0:
            return False
        if quantidade > self.estoque:
            return False
        self.estoque -= quantidade
        return True

    def repor(self, quantidade):
        if quantidade <= 0:
            return False
        self.estoque += quantidade
        return True

    def valor_em_estoque(self):
        return self.preco * self.estoque


def relatorio(produtos):
    total = 0.0
    sem_estoque = 0

    for produto in produtos:
        total += produto.valor_em_estoque()
        if produto.estoque == 0:
            sem_estoque += 1

        print(f"{produto.nome}: estoque={produto.estoque}, valor em estoque={produto.valor_em_estoque():.1f}")

    print(f"Total em estoque: {total:.1f}")
    print(f"Produtos sem estoque: {sem_estoque}")


produtos = [
    Produto("Caderno", 10.0, 2),
    Produto("Caneta", 3.0, 0),
    Produto("Borracha", 2.0, 5),
]

print("Lista com produtos:\n")
relatorio(produtos)

print("\nLista vazia:\n")
relatorio([])
