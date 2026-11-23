# Uma aplicação possui um sistema simples de autenticação.

# Considere as credenciais cadastradas:


# usuario_correto = "admin"senha_correta = "python123"


# Solicite que a pessoa informe seu usuário e sua senha.

# O programa deverá apresentar uma das seguintes mensagens:

# Acesso autorizado! — quando ambos estiverem corretos.
# Senha incorreta! — quando o usuário estiver correto, mas a senha errada.
# Usuário não encontrado! — quando o usuário não existir.


# Desafio: Utilize condições aninhadas para verificar primeiro o usuário e depois a senha.

usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Informe o usuário: ")
senha = input("Informe a senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado!")
