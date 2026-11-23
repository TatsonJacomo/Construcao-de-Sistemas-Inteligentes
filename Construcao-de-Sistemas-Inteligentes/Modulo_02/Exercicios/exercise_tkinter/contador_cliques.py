# Exercício 02 — Contador de cliques


# Desenvolva uma aplicação que possua um botão e um rótulo. 
# A cada clique no botão, incremente um contador e atualize o rótulo apresentando a
# quantidade de cliques realizados.


# +----------------------------+
# | Contador de cliques        |
# +----------------------------+
# |         Cliques: 0         |
# |       [ Clique aqui ]      |
# +----------------------------+




import tkinter as tk

janela = tk.Tk()
janela.title("Contador de cliques")
janela.geometry("400x200")
janela.resizable(False, False)

cliques = 0

rotulo = tk.Label(janela, text="Cliques: 0")
rotulo.pack(pady=20)


def clicar():
    global cliques
    cliques += 1
    rotulo.config(text=f"Cliques: {cliques}")


botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack()

janela.mainloop()
