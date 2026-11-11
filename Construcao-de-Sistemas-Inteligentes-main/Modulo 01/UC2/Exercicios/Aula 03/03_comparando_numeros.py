# Leia dois números inteiros.
# Informe se o primeiro é maior, se o segundo é maior ou se os dois são iguais.
# Use uma cadeia if / elif / else.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1 > num2:
    print("O primeiro numero e maior.")
elif num2 > num1:
    print("O segundo numero e maior.")
else:
    print("Os dois sao iguais")