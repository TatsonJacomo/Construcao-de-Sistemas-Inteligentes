# importe a biblioteca tkinter com o apelido de "tk"
import tkinter as tk

# a função TK() vem pronta da biblioteca  tkinter
# cria a janela principal do nosso programa
janela = tk.Tk()

#janela.title() -> funçao do tkinter para dar nome a essa janela
janela.title("Minha primeira aplicação")
#janela.geometry() -> função do tkinter para dar tamanho á janela, em pixels
janela.geometry("400x300")

# vamos criar um conponente de texto
texto = tk.Label(
    janela, # em que tela que ele aparece
    text="Seja bem-vindo(a)", # qual o texto dele
    font= ("Arial", 14), # qual a fonte de texto e o tamanho
    fg= "blue" # qual a cor do texto
)

texto.pack(pady=20)

# cria um compenente que permite digitar texto 
entrada = tk.Entry(
    janela, # em qual tela ele vai
    width=30
) 

entrada.pack(pady=10)


def exibir_mensagem():
    print(f"Texto: {entrada.get()}")

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=exibir_mensagem
)

botao.pack(pady=10)


janela.mainloop()