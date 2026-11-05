# Leia seis números inteiros e guarde todos em uma lista.
# Mostre a lista, a soma, a média, o maior e o menor valor.

# Teste com 3, -2, 0, 7, 7, -3: soma 12, média 2.0, maior 7 e menor -3.

lista = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

print("--------------------------------------")

print("Lista:", lista)
print("--------------------------------------")
print("Soma:", sum(lista))
print("Média:", sum(lista) / len(lista))
print("Maior:", max(lista))
print("Menor:", min(lista))

print("--------------------------------------")