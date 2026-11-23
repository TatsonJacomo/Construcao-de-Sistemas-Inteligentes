# Crie a classe Oficina, com nome, capacidade e inscritos. 
# Receba nome e capacidade na criação; inicie inscritos com zero. 
# Considere a capacidade um inteiro positivo.


# Implemente:

# inscrever(): adiciona uma pessoa se houver vaga;
# cancelar(): remove uma pessoa se existir pelo menos uma inscrição;
# vagas_disponiveis(): retorna a quantidade de vagas restantes.


# Os métodos que alteram o estado retornam True quando realizam a operação e False quando a recusam.

# Crie uma lista com estas oficinas:

#| Nome	      |  Capacidade	| Tentativas de inscrição  |
#| Robótica   |    	2	    |        3                 |
#| Desenho    |  	3	    |        1                 |
#| Música	  |     1	    |        0                 | 


# Use os métodos para realizar as tentativas. Depois, percorra a lista e mostre:

# nome, inscritos e vagas disponíveis de cada oficina;
# total de pessoas inscritas;
# total de vagas disponíveis;
# quantidade de oficinas lotadas.


# Conferência: Robótica tem 2 inscritos, Desenho tem 1 e Música tem 0. 
# O relatório apresenta 3 inscritos, 3 vagas disponíveis e 1 oficina lotada.


# Repita o relatório com uma lista vazia: os três totais devem ser zero. 
# Em um teste separado, cancele duas vezes uma oficina com apenas uma inscrição e confira que a segunda tentativa preserva zero inscritos.


class Oficina:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.inscritos = 0

    def inscrever(self):
        if self.inscritos >= self.capacidade:
            return False
        self.inscritos += 1
        return True

    def cancelar(self):
        if self.inscritos <= 0:
            return False
        self.inscritos -= 1
        return True

    def vagas_disponiveis(self):
        return self.capacidade - self.inscritos


def mostrar_relatorio(oficinas):
    total_inscritos = 0
    total_vagas = 0
    oficinas_lotadas = 0

    for oficina in oficinas:
        print(oficina.nome, "- inscritos:", oficina.inscritos,
              "- vagas disponíveis:", oficina.vagas_disponiveis())
        total_inscritos += oficina.inscritos
        total_vagas += oficina.vagas_disponiveis()
        if oficina.vagas_disponiveis() == 0:
            oficinas_lotadas += 1

    print("Total de inscritos:", total_inscritos)
    print("Total de vagas disponíveis:", total_vagas)
    print("Oficinas lotadas:", oficinas_lotadas)


robotica = Oficina("Robótica", 2)
for _ in range(3):
    robotica.inscrever()

desenho = Oficina("Desenho", 3)
desenho.inscrever()

musica = Oficina("Música", 1)

oficinas = [robotica, desenho, musica]
mostrar_relatorio(oficinas)

print("--- Lista vazia ---")
mostrar_relatorio([])

print("--- Cancelamento com uma inscrição ---")
teste = Oficina("Teste", 2)
print(teste.inscrever())
print(teste.cancelar())
print(teste.cancelar())
print("Inscritos finais:", teste.inscritos)

