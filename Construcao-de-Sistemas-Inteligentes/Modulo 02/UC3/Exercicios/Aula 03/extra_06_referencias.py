# Sem executar, preveja as quatro linhas da saída:

class Marcador:
    def __init__(self, valor):
        self.valor = valor

    def somar(self, quantidade):
        self.valor = self.valor + quantidade


primeiro = Marcador(10)
atalho = primeiro
segundo = Marcador(10)

atalho.somar(5)
segundo.somar(2)
print(primeiro.valor)
print(atalho.valor)
print(segundo.valor)

atalho = segundo
atalho.somar(3)
print(segundo.valor)


# 1. Execute o código e compare com sua previsão.
# 2. Desenhe setas ligando cada variável ao objeto correspondente antes e depois de atalho = segundo.
# 3. Explique quantos objetos foram criados e por que a atribuição não cria um terceiro.
# 4. Altere a criação inicial de atalho para que ele seja um objeto independente de valor 10. Execute novamente e explique a mudança nas saídas.


