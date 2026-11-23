# A biblioteca começa o dia com 40 livros disponíveis. Nesta ordem:
# recebe 12 livros novos;
# empresta 9 livros;
# recebe a devolução de 4 livros;
# empresta mais 6 livros.

# Previsões:
# Inicial: 40
# Recebe 12 -> 52
# Empresta 9 -> 43
# Recebe devolução 4 -> 47
# Empresta 6 -> 41

livros_disponiveis = 40

print(f"Estoque inicial: {livros_disponiveis} livros")

livros_disponiveis += 12
print(f"Depois de receber 12 livros: {livros_disponiveis} livros")

livros_disponiveis -= 9
print(f"Depois de emprestar 9 livros: {livros_disponiveis} livros")

livros_disponiveis += 4
print(f"Depois de receber 4 devoluções: {livros_disponiveis} livros")

livros_disponiveis -= 6
print(f"Depois de emprestar mais 6 livros: {livros_disponiveis} livros")
