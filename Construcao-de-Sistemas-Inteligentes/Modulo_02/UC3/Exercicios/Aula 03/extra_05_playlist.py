# Crie a classe Playlist, recebendo nome e criando uma lista própria musicas, inicialmente vazia.

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self, titulo):
        if titulo == "" or titulo in self.musicas:
            return False
        self.musicas.append(titulo)
        return True

    def quantidade_musicas(self):
        return len(self.musicas)


estudo = Playlist("Estudo")
viagem = Playlist("Viagem")

print(estudo.adicionar("Chuva"))
print(estudo.adicionar("Piano"))
print(estudo.adicionar("Chuva"))
print(estudo.adicionar(""))

print(viagem.adicionar("Estrada"))

print(estudo.nome, estudo.musicas, estudo.quantidade_musicas())
print(viagem.nome, viagem.musicas, viagem.quantidade_musicas())

print("Músicas de Estudo:")
for titulo in estudo.musicas:
    print(titulo)

# Se musicas = [] fosse declarada diretamente no corpo da classe, ela seria
# uma lista compartilhada por todas as instâncias da classe, em vez de existir
# separadamente em cada objeto. Adicionar música em uma playlist afetaria as outras.

