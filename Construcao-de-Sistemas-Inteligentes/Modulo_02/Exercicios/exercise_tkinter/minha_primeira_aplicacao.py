# Exercício 01 — Minha primeira aplicação

# Desenvolva uma aplicação desktop que apresente uma janela com as seguintes características:


# Título: "Minha Aplicação";
# Dimensões: 300x200 pixels;
# Redimensionamento desabilitado;
# Um rótulo centralizado com o texto "Olá, mundo!".

import tkinter as tk

janela = tk.Tk()

janela.title("Minha Aplicação")
janela.geometry("300x200")
janela.resizable(False, False)

rotulo = tk.Label(janela, text="Olá, mundo!")
rotulo.pack(expand=True)

janela.mainloop()

