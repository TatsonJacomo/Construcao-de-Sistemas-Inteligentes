# Leia um inteiro maior ou igual a zero.
# Mostre a contagem desse número até zero e, ao final, Lançamento realizado!. 
# Para uma entrada negativa, apresente uma mensagem de valor inválido e não realize o lançamento.

# Teste com 3, 0 e -1.

numero = int(input("Digite um número inteiro: "))

if numero >= 0:
    for numero in range(numero, -1, -1):
        print(numero, end= " ")
    print("\nLançamento realizado!")
else: 
    print("valor Inválido")
