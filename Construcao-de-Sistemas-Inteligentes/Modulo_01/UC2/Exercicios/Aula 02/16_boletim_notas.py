# Um aluno recebeu as notas 7.5, 8.0 e 9.5 em três atividades de mesmo peso.

# Guarde o nome do aluno e cada nota em variáveis separadas.
# Calcule a soma das notas em uma variável soma_notas.
# Calcule a média dividindo a soma pela quantidade de atividades.
# Mostre o nome, as três notas e a média.
# Troque apenas a segunda nota por 6.5 no código e execute novamente.
# O programa deve recalcular a média a partir das variáveis. Não escreva a média pronta no código. Não é necessário informar aprovação ou reprovação.

nome_aluno = "Maria"
nota1 = 7.5
nota2 = 8.0
nota3 = 9.5

soma_notas = nota1 + nota2 + nota3
quantidade_atividades = 3
media = soma_notas / quantidade_atividades

print(f"Aluno: {nome_aluno}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media:.2f}")

# Alterando apenas a segunda nota:
nota2 = 6.5
soma_notas = nota1 + nota2 + nota3
media = soma_notas / quantidade_atividades

print(f"Aluno: {nome_aluno}")
print(f"Notas atualizadas: {nota1}, {nota2}, {nota3}")
print(f"Nova média: {media:.2f}")
