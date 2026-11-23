# Crie a classe Retangulo, inicializada com largura e altura, ambas positivas.
#  Implemente calcular_area(), que devolve a multiplicação dessas medidas.

# Crie dois objetos e mostre suas áreas fora do método. Teste com medidas 4 e 3: área 12.

# Para explicar: qual é a diferença entre retornar a área e mostrá-la dentro do método?

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


retangulo1 = Retangulo(4, 3)
retangulo2 = Retangulo(5, 2)

area1 = retangulo1.calcular_area()
area2 = retangulo2.calcular_area()

print("Área do primeiro retângulo:", area1)
print("Área do segundo retângulo:", area2)