#O programa abaixo deveria mostrar o nome de um curso, o valor da mensalidade e se a matrícula está ativa, mas contém erros:


# nome curso = "Python básico"
# mensalidade = 89,90
# matricula_ativa = true

# print("Curso:", nome_curso)
# print("Mensalidade:", Mensalidade)
# print("Matrícula ativa:", matricula_ativa)



# Reescreva o código corrigindo:

# o nome da variável que contém um espaço;
# a escrita do número decimal;
# a escrita do valor booleano;
# a diferença entre maiúsculas e minúsculas no nome da variável.


# Para cada correção, escreva um comentário explicando a regra da aula que foi aplicada.
# Ao final, mostre também type(mensalidade) para verificar se o valor é um float.



# Correção

# 1. Correção do espaço no nome da variável:
# Nomes de variáveis não podem conter espaços. 

nome_curso = "Python básico"

# 2. Correção do número decimal:
# o separador decimal é o ponto (.) e nunca a vírgula (,).
mensalidade = 89.90

# 3. Correção do valor booleano:
# booleanos em Python devem iniciar com letra maiúscula (True ou False).
matricula_ativa = True

print("Curso:", nome_curso)

# 4. Correção da diferença entre maiúsculas e minúsculas: 
# Como a variável foi criada como 'mensalidade' (minúscula), devemos chamá-la da mesma forma.
print("Mensalidade:", mensalidade)

print("Matrícula ativa:", matricula_ativa)

# Verificação do tipo da variável mensalidade
print("Tipo da variável mensalidade:", type(mensalidade))