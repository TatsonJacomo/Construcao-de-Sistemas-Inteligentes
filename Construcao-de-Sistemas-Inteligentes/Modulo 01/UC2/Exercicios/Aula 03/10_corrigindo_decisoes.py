# O programa deveria permitir a participação de pessoas a partir de 16 anos que tenham autorização, mas contém erros:

# idade = input("Idade: ")
# autorizacao = input("Possui autorização? (sim/nao): ")

# if idade >= 16 and autorizacao = "sim"
# print("Participação permitida.")
# else:
#     print("Participação não permitida.")


# Reescreva o código corrigindo a conversão da idade, o operador de comparação, os dois-pontos e a indentação. Explique cada correção em um comentário. Considere uma idade não negativa e as respostas sim ou nao.



# Correção 1: Converter a entrada da idade de string para inteiro usando int()
idade = int(input("Idade: ")) 

# Correção 2: Adicionar .strip().lower() para padronizar o texto digitado (ex: "Sim" -> "sim")
autorizacao = input("Possui autorização? (sim/nao): ").strip().lower()

# Correção 3: Trocar o operador de atribuição (=) por igualdade (==) e adicionar os dois-pontos (:) no final do if
if idade >= 16 and autorizacao == "sim":
    print("Participação permitida.")
else:
    # Correção 4: Ajustar a indentação do bloco else para alinhar corretamente com o if
    print("Participação não permitida.")