# Leia um número inteiro positivo e mostre os números de 1 até ele, incluindo o limite.
# Se a entrada for menor ou igual a zero, mostre uma mensagem de valor inválido.

# Teste com 1, 5 e 0.


numero = int(input("Digite um número inteiro positivo: "))

if numero >= 0:
    for numero in range(1, numero + 1 ):
        print(numero)
else:
    print("Valor inválido. Digite um número maior que zero.")