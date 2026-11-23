# Exercício 07 — Sistema de frete

# Intermediário

# Uma loja virtual deseja calcular o valor do frete com base na região do cliente e no valor da compra.

# Solicite o valor da compra e a região de entrega:
# Região             Frete
# Sul                R$ 15,00
# Sudeste            R$ 20,00
# Centro-Oeste       R$ 25,00
# Norte ou Nordeste  R$ 35,00

# Regras adicionais:
# Compras a partir de R$ 300,00 recebem frete grátis.
# Compras com valor menor ou igual a zero são inválidas.
# Regiões não reconhecidas devem apresentar Região inválida.
# Mostre o valor da compra, o frete e o total.

# Atenção: Mesmo que a compra tenha frete grátis, a região informada deverá ser válida.

valor_compra = float(input("Digite o valor da compra: R$ "))
regiao = input("Digite a região de entrega: ").strip().title()

if valor_compra <= 0:
    print("Compra inválida.")
elif regiao not in ["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"]:
    print("Região inválida.")
else:
    if valor_compra >= 300:
        frete = 0
    elif regiao == "Sul":
        frete = 15
    elif regiao == "Sudeste":
        frete = 20
    elif regiao == "Centro-Oeste":
        frete = 25
    else:
        frete = 35

    total = valor_compra + frete
    print(f"Valor da compra: R$ {valor_compra:.2f}")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Total: R$ {total:.2f}")

