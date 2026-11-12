# Crie a classe Contador. 
# Cada instância deve começar com valor = 0 e oferecer os métodos incrementar() e zerar().

# Crie dois contadores. 
# Incremente o primeiro três vezes e o segundo uma vez. 
# Mostre os valores, zere somente o primeiro e mostre novamente.

# Resultado esperado: primeiro 3 e 1; depois 0 e 1.


class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0


contador1 = Contador()
contador2 = Contador()

for _ in range(3):
    contador1.incrementar()
contador2.incrementar()


print(f"\nAntes de zerar: primeiro = {contador1.valor}, segundo = {contador2.valor}")
contador1.zerar()
print(f"Depois de zerar: primeiro = {contador1.valor}, segundo = {contador2.valor}\n")