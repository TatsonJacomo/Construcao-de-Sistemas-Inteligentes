# Solicite um número inteiro positivo e faça uma contagem regressiva até zero.

# Ao terminar, mostre Lançamento realizado!.
 

numero = int(input("Digite um número inteiro: "))
contador = numero

while contador >= 0:
    print(contador)
    contador -= 1

print("Lançamento realizado!")

