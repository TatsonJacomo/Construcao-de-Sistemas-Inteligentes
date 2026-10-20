# A biblioteca tem 8 exemplares disponíveis. Leia a quantidade que a pessoa deseja retirar.

# Se a quantidade for menor ou igual a zero, informe que o pedido é inválido.
# Se for maior que o estoque, informe que não há exemplares suficientes.
# Caso contrário, confirme o pedido, atualize o estoque e mostre a quantidade restante.
# O estoque só deve diminuir quando o pedido for confirmado.

estoque = 8

quantidade = int(input("Quantos exemplares você quer retirar? "))


if quantidade <= 0:
    print("Pedido Inválido")
elif quantidade > estoque:
    print("Não há exemplares suficientes!")
else:
    estoque -= quantidade
    print("Pedido Confirmado!")
    print(f"O estoque possui {estoque}")