# -*- coding: utf-8 -*-

# Use a lista ["corda", "água", "mapa", "água"].
# Leia o nome de um item e informe se ele existe e quantas vezes aparece.
# Diferencie maiúsculas e minúsculas.

# Teste com água (duas ocorrências), mapa (uma) e lanterna (nenhuma).


lista = ["corda", "água", "mapa", "água"]

item = input("Digite o nome do item: ")
quantidade = lista.count(item)

if quantidade > 0:
    print(f"O item '{item}' existe e aparece {quantidade} vez(es) na lista.")
else:
    print(f"O item '{item}' não existe na lista.")