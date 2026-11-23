# Exercício 05 — Desafio: Cadastro de personagens

# Desenvolva uma interface gráfica para cadastrar personagens de um RPG.
# Cada personagem deverá possuir nome, classe, nível e quantidade de pontos de vida.

# Ao clicar no botão "Cadastrar personagem", o programa deverá validar as informações,
#  adicionar o personagem a uma lista e apresentar os personagens cadastrados na interface.



# Tip

# Utilize os conhecimentos de Programação Orientada a Objetos para criar uma classe Personagem
#  e instanciar um novo objeto a cada cadastro.

import tkinter as tk


class Personagem:
    def __init__(self, nome, classe, nivel, pontos_vida):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.pontos_vida = pontos_vida

    def __str__(self):
        return f"{self.nome} | Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.pontos_vida}"


janela = tk.Tk()
janela.title("Cadastro de personagens")
janela.geometry("500x400")
janela.resizable(False, False)

personagens = []

entradas = {}
for linha, (campo, texto) in enumerate((
    ("nome", "Nome:"),
    ("classe", "Classe:"),
    ("nivel", "Nível:"),
    ("vida", "Pontos de vida:"),
)):
    tk.Label(janela, text=texto).grid(row=linha, column=0, sticky="e", padx=10, pady=5)
    entradas[campo] = tk.Entry(janela, width=30)
    entradas[campo].grid(row=linha, column=1, padx=10, pady=5)

mensagem = tk.Label(janela, text="")
mensagem.grid(row=4, column=0, columnspan=2, pady=5)

lista = tk.Listbox(janela, width=60, height=10)
lista.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def cadastrar_personagem():
    nome = entradas["nome"].get().strip()
    classe = entradas["classe"].get().strip()
    nivel_texto = entradas["nivel"].get().strip()
    vida_texto = entradas["vida"].get().strip()

    if not all((nome, classe, nivel_texto, vida_texto)):
        mensagem.config(text="Preencha todos os campos.")
        return

    try:
        nivel = int(nivel_texto)
        pontos_vida = int(vida_texto)
    except ValueError:
        mensagem.config(text="Nível e pontos de vida devem ser números inteiros.")
        return

    if nivel < 1:
        mensagem.config(text="O nível deve ser maior ou igual a 1.")
        return

    if pontos_vida < 0:
        mensagem.config(text="Os pontos de vida não podem ser negativos.")
        return

    personagem = Personagem(nome, classe, nivel, pontos_vida)
    personagens.append(personagem)
    lista.insert(tk.END, str(personagem))
    mensagem.config(text="Personagem cadastrado com sucesso!")

    for entrada in entradas.values():
        entrada.delete(0, tk.END)


tk.Button(
    janela,
    text="Cadastrar personagem",
    command=cadastrar_personagem,
).grid(row=5, column=0, columnspan=2, pady=10)

janela.mainloop()


