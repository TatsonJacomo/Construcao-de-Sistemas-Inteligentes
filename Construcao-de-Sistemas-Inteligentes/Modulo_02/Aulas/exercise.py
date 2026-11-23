# Crie uma tela que contém uma espécie de formulário:
# Ela pede nome, email e cidade.
# Crie um Entry para cada um deles. 
# Coloque um Label em cima de cada Entry.
# Crie um botão que, ao clicar, mostra a seguinte frase no terminal:
# "Olá fulano, seu email é tal e você é de tal cidade" 




import tkinter as tk

janela = tk.Tk()

janela.title("Formulário")

janela.geometry("300x400")


texto = tk.Label(
    janela,
    text="Preencha o Formulário",
    font= ("arial", 14),
    fg="red"
)

texto.pack(pady=20)

label_nome = tk.Label(janela, text="Nome")
label_nome.pack()
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=(5, 10))

label_email = tk.Label(janela, text="Email")
label_email.pack()
entrada_email = tk.Entry(janela, width=30)
entrada_email.pack(pady=(5, 10))

label_cidade = tk.Label(janela, text="Cidade")
label_cidade.pack()
entrada_cidade = tk.Entry(janela, width=30)
entrada_cidade.pack(pady=(5, 10))

def exibir_mensagem():
    nome = entrada_nome.get()
    email = entrada_email.get()
    cidade = entrada_cidade.get()
    print(f"Olá {nome}, seu email é {email} e você é de {cidade}")

botao = tk.Button(
    janela,
    text="Enviar",
    command=exibir_mensagem
)

botao.pack(pady=20)

janela.mainloop()







# Desafio: não usar nenhum tipo de IA
# criar uma calculadora de soma
