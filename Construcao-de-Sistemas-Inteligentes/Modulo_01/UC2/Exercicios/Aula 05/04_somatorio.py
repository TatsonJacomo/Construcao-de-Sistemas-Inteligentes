# Solicite cinco números inteiros e apresente a soma de todos eles.

# Utilize um contador para controlar as repetições e um acumulador para guardar a soma.


contador = 1
soma = 0

while contador <= 5:
    numero = int(input("Digite umn número inteiro: "))
    soma += numero
    contador +=  1
print(f"A soma dos números escolhidos e: {soma}")