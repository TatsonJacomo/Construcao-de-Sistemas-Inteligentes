# Solicite um número inteiro positivo e apresente todos os números de 1 até o valor informado.
# Exemplo:
# Digite um número: 5
# 1
# 2
# 3
# 4
# 5

numero = int(input("Digite um número: "))

contador = 1
while contador <= numero:
    print(contador)
    contador += 1
