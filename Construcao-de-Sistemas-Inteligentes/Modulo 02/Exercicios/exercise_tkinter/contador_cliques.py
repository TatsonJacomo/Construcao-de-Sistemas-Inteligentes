import tkinter as tk

janela = tk.Tk()
janela.title("contador de Cliques")
janela.geometry("400x200")

rotulo = tk.Label(
    janela,
    text="Clique no botão",
    fg="blue"
)
rotulo.pack(pady=10)

cliques = 0
def clicar():
    cliques += 1
    rotulo.config(text=f"Quantidade de cliques: {cliques}")


botao = tk.Button(
    janela,
    text= "Clique-me",
    command=clicar
)


janela.mainloop()