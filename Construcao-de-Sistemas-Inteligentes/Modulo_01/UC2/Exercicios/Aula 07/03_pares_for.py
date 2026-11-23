# Leia um inteiro positivo e mostre os números pares de 2 até o limite, incluindo-o quando ele for par.
#  Utilize o passo de range().

# Se o limite for 1, informe que não há pares no intervalo. 
# Para valores menores ou iguais a zero, informe que o limite é inválido.

# Teste com 1, 2, 9 e 10.


limite = int(input("Digite um número inteiro: "))

if limite <= 0:
    print("O limite é inválido!")
elif limite == 1:
    print("Não há pares no intervalo.")
else:
    for numero in range(2, limite + 1, 2):
        print(numero)
