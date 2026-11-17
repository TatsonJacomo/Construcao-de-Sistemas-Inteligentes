# Crie a classe Reservatorio, recebendo capacidade e iniciando nivel com zero.
# Considere a capacidade positiva e todas as medidas em litros inteiros.

class Reservatorio:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.nivel = 0

    def adicionar(self, litros):
        if litros <= 0:
            return False
        if litros > self.espaco_disponivel():
            return False
        self.nivel += litros
        return True

    def retirar(self, litros):
        if litros <= 0:
            return False
        if litros > self.nivel:
            return False
        self.nivel -= litros
        return True

    def espaco_disponivel(self):
        return self.capacidade - self.nivel


reservatorio = Reservatorio(100)

print("adicionar(60):", reservatorio.adicionar(60), "- nível:", reservatorio.nivel)
print("adicionar(50):", reservatorio.adicionar(50), "- nível:", reservatorio.nivel)
print("retirar(20):", reservatorio.retirar(20), "- nível:", reservatorio.nivel)
print("adicionar(60):", reservatorio.adicionar(60), "- nível:", reservatorio.nivel)
print("retirar(100):", reservatorio.retirar(100), "- nível:", reservatorio.nivel)
print("retirar(1):", reservatorio.retirar(1), "- nível:", reservatorio.nivel)
print("adicionar(0):", reservatorio.adicionar(0), "- nível:", reservatorio.nivel)

print("Nível final:", reservatorio.nivel)
print("Espaço disponível:", reservatorio.espaco_disponivel())

print("retirada negativa:", reservatorio.retirar(-5), "- nível:", reservatorio.nivel)

vazio = Reservatorio(100)
print("adição exata da capacidade:", vazio.adicionar(100), "- nível:", vazio.nivel)

