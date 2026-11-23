# Leia oito inteiros e armazene-os em uma lista.
# Percorra essa lista para criar outra contendo apenas os números pares.
# Mostre as duas listas. Preserve a ordem e os repetidos.

# Lembre-se: numero % 2 == 0 identifica um par, incluindo zero e pares negativos.
# Teste também uma execução sem nenhum par.

numeros = []
for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Lista original: {numeros}")
print(f"Lista com números pares: {pares}")