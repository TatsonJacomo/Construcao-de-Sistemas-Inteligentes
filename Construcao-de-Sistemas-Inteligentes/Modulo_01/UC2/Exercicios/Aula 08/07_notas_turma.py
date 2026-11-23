# Leia a quantidade de alunos.
# Se for menor ou igual a zero, informe que a quantidade é inválida.
# Para uma quantidade válida, leia e armazene as notas, solicitando novamente qualquer nota fora da faixa de 0 a 10.

# Mostre todas as notas, a média, a maior nota, a menor nota e quantas atingiram pelo menos 7.

# Teste com apenas um aluno, com notas repetidas e com uma nota inválida seguida de uma válida.

quantidade = int(input("Digite a quantidade de alunos: "))

if quantidade <= 0:
    print("Quantidade inválida.")
else:
    notas = []

    for i in range(quantidade):
        while True:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("Nota fora da faixa permitida. Digite uma nota de 0 a 10.")

    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    atingiram_sete = sum(1 for nota in notas if nota >= 7)

    print(f"Notas: {notas}")
    print(f"Média: {media:.1f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Quantidade de alunos com pelo menos 7: {atingiram_sete}")