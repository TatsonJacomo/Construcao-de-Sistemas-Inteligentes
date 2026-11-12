# Crie uma lista com cinco nomes de objetos.
# Mostre a lista completa, sua quantidade de elementos, o primeiro e o último objeto.
# Em seguida, substitua o terceiro objeto e mostre a lista atualizada.

lista = ["Casa", "Galinha", "Prato", "Rua", "Valdir"]

print("Lista completa:", lista)

#A função len() informa a quantidade de elementos, incluindo os repetidos.
print("Quantidade de elementos:", len(lista))

# mostra o prineiro objeto da lista.
print("Primeiro objeto:", lista[0])

# mostra o último objeto da lista.
print("Último objeto:", lista[-1])

# substitui o terceiro objeto da lista.
lista[2] = "Mesa"

# mostra a lista atualizada.
print("Lista atualizada:", lista)

 