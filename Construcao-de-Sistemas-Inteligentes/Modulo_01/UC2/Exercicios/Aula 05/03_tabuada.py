# Solicite um número inteiro e apresente sua tabuada de multiplicação de 1 até 10 utilizando while.

numero = int(input("Digite um número inteiro: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1


