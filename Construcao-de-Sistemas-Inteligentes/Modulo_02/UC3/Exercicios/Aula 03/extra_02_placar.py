# O código abaixo registra os pontos de um jogador.

class Placar:
    def __init__(self, jogador):
        self.jogador = jogador
        self.pontos = 0

    def marcar(self, quantidade):
        if quantidade > 0:
            self.pontos = self.pontos + quantidade
            return True
        return False

    def consultar_pontos(self):
        return self.pontos


placar = Placar("Lia")

print(placar.marcar(3))
print(placar.marcar(2))
print(placar.marcar(0))
print(placar.marcar(-1))

pontuacao = placar.consultar_pontos()
print(pontuacao)
print(pontuacao * 2)

# Em __init__, escrever apenas pontos = 0 cria uma variável local chamada pontos,
# não um atributo do objeto. Usar self.pontos cria o atributo acessível pelo objeto.


