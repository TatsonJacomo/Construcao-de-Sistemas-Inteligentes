# Solicite quantos alunos existem em uma turma.

# Em seguida, leia a nota de cada aluno e calcule a média geral.

# A quantidade de alunos deve ser maior que zero.


alunos = int(input("Digite quantos alunos tem na turma: "))

soma = 0
contador = 1

if alunos <1:
    print()

while contador <= alunos:
    nota = float(input(f"Digite a nota do {contador}° aluno: "))
    soma = soma + nota
    contador = contador + 1

    nota = float(input("Digite a nota do aluno: "))
    contador += alunos 

print(f"A média da turma e: {alunos + soma / 2} ")


while contador <= alunos:
    nota = float(input(f"Digite a nota do {contador}º aluno (0 a 10): "))
    
    if 0 <= nota <= 10:
        soma += nota
        contador += 1 
    else:
        print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.")

if alunos > 0:
    media = soma / alunos
    print(f"\nA média geral da turma é: {media:.2f}")
else:
    print("Não foi possível calcular a média.")