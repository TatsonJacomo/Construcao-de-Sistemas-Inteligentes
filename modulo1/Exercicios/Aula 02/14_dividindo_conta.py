# 14 — Dividindo a conta
# Arquivo: 14_dividindo_conta.py

# Quatro amigos compraram uma pizza de R$ 48.00 e uma bebida de R$ 12.00. A conta será dividida igualmente.

# Crie variáveis para o preço da pizza, o preço da bebida e a quantidade de amigos.
# Calcule o total da conta em uma nova variável.
# Calcule quanto cada amigo deverá pagar.
# Mostre o total e o valor por pessoa com descrições.
# Use type() para mostrar o tipo do valor por pessoa.
# Para pensar: o resultado da divisão é um int ou um float, mesmo quando não há centavos?

pizza = 48.00
bebida = 12.00
amigos = 4


resultado = pizza + bebida
total_pessoa = resultado / amigos

print("O valor Total da compra e: R$" resultado) # valor total da conta
print("Cada amigo vai pagar: R$" total_pessoa, type(total_pessoa)) # cada amiga vai pagar!
