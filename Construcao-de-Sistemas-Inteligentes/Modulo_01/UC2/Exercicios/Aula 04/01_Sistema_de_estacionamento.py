# Um estacionamento precisa calcular o valor cobrado de seus clientes de acordo com o tempo de permanência.

# Desenvolva um programa que solicite a quantidade de horas que um veículo permaneceu estacionado.

# As regras são:
# Até 2 horas: R$ 10,00
# Mais de 2 até 5 horas: R$ 20,00
# Mais de 5 horas: R$ 30,00

# Requisitos:
# A quantidade de horas deve ser maior que zero.
# Caso seja informado um valor inválido, apresente uma mensagem.
# Exiba o valor total a pagar.

horas = float(input("Digite a quantidade de horas estacionadas: "))

if horas <= 0:
    print("Valor inválido. A quantidade de horas deve ser maior que zero.")
elif horas <= 2:
    valor = 10
elif horas <= 5:
    valor = 20
else:
    valor = 30

print(f"Valor total a pagar: R$ {valor:.2f}")

