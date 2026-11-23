# Uma turma com 20 alunos fará um passeio. O ônibus custa R$ 600.00 para toda a turma.
# Cada ingresso custa R$ 15.00 e cada lanche custa R$ 10.00 por aluno.

# Crie variáveis para os dados e calcule, em variáveis separadas:
# o custo de todos os ingressos;
# o custo de todos os lanches;
# o custo total do passeio, incluindo o ônibus uma única vez;
# o valor que cada aluno deverá pagar, dividindo o custo total igualmente.

# Mostre um relatório com a quantidade de alunos e todos os custos.
# Depois altere a quantidade de alunos para 25 e execute novamente sem modificar as fórmulas.
# Para pensar: por que o custo total aumenta, mas o valor por aluno diminui?

alunos = 20
onibus = 600.00
preco_ingresso = 15.00
preco_lanche = 10.00

custo_ingressos = alunos * preco_ingresso
custo_lanches = alunos * preco_lanche
custo_total = onibus + custo_ingressos + custo_lanches
valor_por_aluno = custo_total / alunos

print(f"Número de alunos: {alunos}")
print(f"Custo dos ingressos: R$ {custo_ingressos:.2f}")
print(f"Custo dos lanches: R$ {custo_lanches:.2f}")
print(f"Custo do ônibus: R$ {onibus:.2f}")
print(f"Custo total do passeio: R$ {custo_total:.2f}")
print(f"Valor por aluno: R$ {valor_por_aluno:.2f}")

# Alterando a quantidade de alunos para 25 sem mexer nas fórmulas
alunos = 25

custo_ingressos = alunos * preco_ingresso
custo_lanches = alunos * preco_lanche
custo_total = onibus + custo_ingressos + custo_lanches
valor_por_aluno = custo_total / alunos

print("\n--- Com 25 alunos ---")
print(f"Número de alunos: {alunos}")
print(f"Custo dos ingressos: R$ {custo_ingressos:.2f}")
print(f"Custo dos lanches: R$ {custo_lanches:.2f}")
print(f"Custo do ônibus: R$ {onibus:.2f}")
print(f"Custo total do passeio: R$ {custo_total:.2f}")
print(f"Valor por aluno: R$ {valor_por_aluno:.2f}")
