# Exercício 04 — Calculadora simples

# Crie uma aplicação que receba dois valores numéricos e possua quatro botões, 
# um para cada operação matemática: soma, subtração, multiplicação e divisão.

# O resultado deverá ser apresentado na própria interface. 
# Não se esqueça de validar os valores informados e impedir divisões por zero.



# +---------------------------------+
# | Calculadora simples             |
# +---------------------------------+
# | Primeiro valor: [ 10          ] |
# | Segundo valor:  [ 5           ] |
# |                                 |
# |    [ + ] [ - ] [ * ] [ / ]      |
# |                                 |
# |          Resultado: 15          |
# +---------------------------------+

import tkinter as tk


janela = tk.Tk()
janela.title("Calculadora simples")
janela.geometry("400x220")
janela.resizable(False, False)

resultado = tk.Label(janela, text="Resultado:")
resultado.grid(row=3, column=0, columnspan=2, pady=15)



def obter_valores():
    try:
        primeiro = float(primeiro_valor.get())
        segundo = float(segundo_valor.get())
        return primeiro, segundo
    except ValueError:
        resultado.config(text="Resultado: informe valores numéricos válidos")
        return None


def calcular(operacao):
    valores = obter_valores()
    if valores is None:
        return

    primeiro, segundo = valores

    if operacao == "/" and segundo == 0:
        resultado.config(text="Resultado: divisão por zero não é permitida")
        return

    if operacao == "+":
        valor = primeiro + segundo
    elif operacao == "-":
        valor = primeiro - segundo
    elif operacao == "*":
        valor = primeiro * segundo
    else:
        valor = primeiro / segundo

    resultado.config(text=f"Resultado: {valor:g}")


tk.Label(janela, text="Primeiro valor:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
primeiro_valor = tk.Entry(janela)
primeiro_valor.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Segundo valor:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
segundo_valor = tk.Entry(janela)
segundo_valor.grid(row=1, column=1, padx=10, pady=10)

botoes = tk.Frame(janela)
botoes.grid(row=2, column=0, columnspan=2, pady=10)

for indice, operacao in enumerate(("+", "-", "*", "/")):
    tk.Button(
        botoes,
        text=operacao,
        width=5,
        command=lambda simbolo=operacao: calcular(simbolo),
    ).grid(row=0, column=indice, padx=5)

janela.mainloop()

