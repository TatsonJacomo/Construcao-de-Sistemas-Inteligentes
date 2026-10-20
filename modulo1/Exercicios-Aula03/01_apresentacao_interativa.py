# Peça o nome, a cidade e a idade da pessoa. 
# Mostre uma ficha e calcule quantos anos ela terá no próximo aniversário.

nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
cidade = input("Qual sua cidade: ")
soma = idade + 1

print("------- Ficha ----------")
print(f"Olá, {nome}, seja bem vindo!")
print(f"Você tem {idade} anos!")
print(f"Você mora em {cidade}!")
print(f"No próximo ano você terá {soma} anos!")