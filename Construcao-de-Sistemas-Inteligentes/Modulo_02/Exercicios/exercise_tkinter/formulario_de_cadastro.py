# Exercício 03 — Formulário de cadastro


# Crie um formulário utilizando o gerenciador de layout grid().
#  O formulário deverá possuir campos para nome, idade e e-mail, além de um botão "Cadastrar".


# Ao clicar no botão, verifique se todos os campos foram preenchidos e apresente as informações 
# cadastradas em um rótulo na própria interface.

import tkinter as tk


janela = tk.Tk()
janela.title("Formulário de cadastro")
janela.geometry("400x220")
janela.resizable(False, False)

entrada_nome = tk.Entry(janela)
entrada_idade = tk.Entry(janela)
entrada_email = tk.Entry(janela)
resultado = tk.Label(janela, text="")


def cadastrar():
    nome = entrada_nome.get().strip()
    idade = entrada_idade.get().strip()
    email = entrada_email.get().strip()

    if not nome or not idade or not email:
        resultado.config(text="Preencha todos os campos.")
        return

    try:
        idade_numero = int(idade)
    except ValueError:
        resultado.config(text="Informe uma idade válida.")
        return

    resultado.config(
        text=f"Nome: {nome}\nIdade: {idade_numero}\nE-mail: {email}"
    )


tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_idade.grid(row=1, column=1, padx=10, pady=10)

tk.Label(janela, text="E-mail:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entrada_email.grid(row=2, column=1, padx=10, pady=10)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(
    row=3, column=0, columnspan=2, pady=10
)
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()
