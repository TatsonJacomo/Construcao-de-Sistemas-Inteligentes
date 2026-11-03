# Leia a quantidade de alunos. 
# Se ela for menor ou igual a zero, informe que a quantidade é inválida e não calcule a média.

# Para uma quantidade válida, utilize for para ler a nota de cada aluno. 
# Use while para solicitar novamente qualquer nota fora da faixa de 0 a 10, sem avançar para o próximo aluno.

# Mostre a média da turma e quantos alunos obtiveram nota a partir de 7. 
# Teste com apenas um aluno e com uma nota inválida seguida de uma válida

quantidade = int(input("Digite a quantidade de alunos: "))

if quantidade <= 0:
    print("A quantidade de alunos é inválida!")
else:
    soma = 0
    aprovados = 0

    for aluno in range(1, quantidade + 1):
        nota = float(input(f"Digite a nota do aluno {aluno}: "))

        while nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
            nota = float(input(f"Digite a nota do aluno {aluno}: "))

        soma += nota

        if nota >= 7:
            aprovados += 1

    media = soma / quantidade
    print(f"Média da turma: {media:.2f}")
    print(f"Alunos com nota a partir de 7: {aprovados}")
