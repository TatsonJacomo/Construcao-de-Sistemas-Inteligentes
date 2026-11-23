# Crie a classe Turma, com nome e uma lista própria alunos, inicialmente vazia. Implemente matricular(nome_aluno) e quantidade_alunos(), que retorna o tamanho da lista.

# Crie duas turmas. Matricule duas pessoas na primeira e uma na segunda. Mostre o nome de cada turma, seus alunos e sua quantidade.

# Nomes repetidos são permitidos neste exercício. Explique onde a lista deve ser criada para que uma turma não receba os alunos da outra.


class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)


alunos_turma1 = ["Ana", "Bruno"]
alunos_turma2 = ["Carla"]

turma1 = Turma("Turma A")
for aluno in alunos_turma1:
    turma1.matricular(aluno)

turma2 = Turma("Turma B")
for aluno in alunos_turma2:
    turma2.matricular(aluno)

print(f"\n{turma1.nome}: alunos = {turma1.alunos}, quantidade = {turma1.quantidade_alunos()}")
print(f"{turma2.nome}: alunos = {turma2.alunos}, quantidade = {turma2.quantidade_alunos()}\n")

print("A lista 'alunos' deve ser criada dentro de __init__ da classe, para que cada instância tenha sua própria lista e não compartilhe dados entre turmas.\n")






