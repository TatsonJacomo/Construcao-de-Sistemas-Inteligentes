# Leia um inteiro e apresente sua tabuada de multiplicação de 1 até 10, utilizando for.
# Cada linha deve mostrar os dois fatores e o resultado.

numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")


