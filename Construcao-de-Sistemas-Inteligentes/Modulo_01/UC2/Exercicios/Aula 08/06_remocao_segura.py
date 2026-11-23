# Comece com ["Ana", "Bruno", "Ana", "Carla"].
# Leia um nome e remova apenas sua primeira ocorrência, se existir.
# Caso contrário, mostre uma mensagem. Ao final, apresente a lista e a quantidade restante.

# Teste com Ana e com um nome ausente em execuções separadas.

nomes = ["Ana", "Bruno", "Ana", "Carla"]
nome = input("Digite um nome para remover: ")

if nome in nomes:
    nomes.remove(nome)
    print(f"Nome removido: {nome}")
else:
    print(f"O nome '{nome}' não foi encontrado.")

print(f"Lista atual: {nomes}")
print(f"Quantidade restante: {len(nomes)}")