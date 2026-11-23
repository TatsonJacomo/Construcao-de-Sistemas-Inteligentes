# Exercício 08 — Validação de triângulos

# Desafiador

# Desenvolva um programa que receba três números representando os lados de um possível triângulo.

# Para formar um triângulo, os três lados devem ser positivos e satisfazer:
# a+b>c E a+c>b E b+c>a

# Caso seja possível formar um triângulo, classifique-o:
# Equilátero: Três lados iguais
# Isósceles: Exatamente dois lados iguais
# Escaleno: Três lados diferentes

# Se os valores não formarem um triângulo, mostre Triângulo inválido.
# Desafio: Realize primeiro a validação e somente depois a classificação.

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if l1 > 0 and l2 > 0 and l3 > 0 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("Triângulo equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Triângulo inválido")


