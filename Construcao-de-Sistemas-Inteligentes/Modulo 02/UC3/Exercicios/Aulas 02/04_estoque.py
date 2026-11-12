# Implemente a classe Produto com os métodos repor, vender e valor_em_estoque apresentados na aula.

# Crie um produto de preço 5.0 e estoque 4. Execute, nesta ordem:

# Venda de 2 unidades.
# Tentativa de venda de 3 unidades.
# Reposição de 5 unidades.
# Tentativa de reposição de 0 unidades.


# Registre o retorno e o estoque após cada chamada. Ao final, mostre o valor em estoque.

# Conferência: os estoques devem ser 2, 2, 7 e 7. O valor final deve ser 35.0.


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


produto = Produto("Produto", 5.0, 4)

resultado = produto.vender(2)
print(f"Venda de 2: retorno={resultado}, estoque={produto.estoque}")

resultado = produto.vender(3)
print(f"Tentativa de venda de 3: retorno={resultado}, estoque={produto.estoque}")

resultado = produto.repor(5)
print(f"Reposição de 5: retorno={resultado}, estoque={produto.estoque}")

resultado = produto.repor(0)
print(f"Tentativa de reposição de 0: retorno={resultado}, estoque={produto.estoque}")

print(f"Valor em estoque: {produto.valor_em_estoque():.1f}")

