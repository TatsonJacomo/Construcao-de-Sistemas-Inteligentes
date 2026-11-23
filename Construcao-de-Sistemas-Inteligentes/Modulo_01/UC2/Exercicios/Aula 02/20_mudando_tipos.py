# Crie uma variável chamada informacao. Ela deverá receber, nesta ordem:
# o texto "42";
# o número inteiro 42;
# o número decimal 42.0;
# o valor booleano False.

# Após cada atribuição, mostre o valor e o resultado de type(informacao).
# Escreva um comentário explicando a diferença entre "42" e 42.
# Ao final, explique se a variável guarda os quatro valores ao mesmo tempo ou apenas o último valor atribuído.

# "42" é texto (str), porque está entre aspas. Já 42 é número inteiro (int).
# Em Python, uma variável pode receber valores de tipos diferentes ao longo do código,
# mas ela armazena apenas o último valor atribuído em um determinado momento.

informacao = "42"
print("Primeira atribuição:")
print(informacao)
print(type(informacao))

informacao = 42
print("\nSegunda atribuição:")
print(informacao)
print(type(informacao))

informacao = 42.0
print("\nTerceira atribuição:")
print(informacao)
print(type(informacao))

informacao = False
print("\nQuarta atribuição:")
print(informacao)
print(type(informacao))

print("\nConclusão: a variável guarda apenas o último valor atribuído em cada momento.")
