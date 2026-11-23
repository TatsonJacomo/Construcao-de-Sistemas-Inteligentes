# Exercício 04 — Análise de empréstimo

# Intermediário

# Um banco deseja automatizar a análise inicial de empréstimos.

# Solicite as seguintes informações:
# Salário mensal do cliente.
# Valor solicitado para empréstimo.
# Quantidade de parcelas.

# O empréstimo só poderá ser aprovado se todas as condições forem atendidas:
# O salário deve ser de pelo menos R$ 2.000,00.
# O valor solicitado não pode ultrapassar 10 vezes o salário.
# O valor de cada parcela não pode ultrapassar 30% do salário.
# A quantidade de parcelas deve estar entre 1 e 48.

# Caso alguma condição não seja atendida, informe que o empréstimo foi recusado.
# Desafio: Apresente o motivo da recusa.

# Considere um empréstimo sem juros, apenas para fins de exercício.

salario = float(input("Salário mensal: R$ "))
valor_solicitado = float(input("Valor solicitado para empréstimo: R$ "))
quantidade_parcelas = int(input("Quantidade de parcelas: "))

motivos_recusa = []

if salario < 2000:
    motivos_recusa.append("O salário deve ser de pelo menos R$ 2.000,00.")

if valor_solicitado > salario * 10:
    motivos_recusa.append("O valor solicitado não pode ultrapassar 10 vezes o salário.")

if quantidade_parcelas < 1 or quantidade_parcelas > 48:
    motivos_recusa.append("A quantidade de parcelas deve estar entre 1 e 48.")

if quantidade_parcelas > 0:
    valor_parcela = valor_solicitado / quantidade_parcelas
    if valor_parcela > salario * 0.30:
        motivos_recusa.append("O valor de cada parcela não pode ultrapassar 30% do salário.")

if motivos_recusa:
    print("Empréstimo recusado.")
    print("Motivos:")
    for motivo in motivos_recusa:
        print(f"- {motivo}")
else:
    print("Empréstimo aprovado.")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")


