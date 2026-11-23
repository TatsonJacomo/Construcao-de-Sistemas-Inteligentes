

# Exercícios

Crie um arquivo `.py` para cada exercício. Leia os dados com `input()` e faça as conversões necessárias. Utilize apenas os recursos estudados até aqui; não é necessário usar laços, funções próprias ou tratamento de exceções.

Considere entradas numéricas no formato correto. Quando o enunciado pedir validação, verifique a faixa ou as opções com condicionais. Execute cada programa mais de uma vez para testar caminhos diferentes.

## Exercício 01 — Apresentação interativa

**Arquivo: `01_apresentacao_interativa.py`**

Peça o nome, a cidade e a idade da pessoa. Mostre uma ficha e calcule quantos anos ela terá no próximo aniversário.

## Exercício 02 — Conta da lanchonete

**Arquivo: `02_conta_lanchonete.py`**

Leia o preço de um lanche e a quantidade comprada. Calcule o total. Considere preço e quantidade positivos. Se o total for a partir de R$ 50.00, aplique 10% de desconto; caso contrário, mantenha o valor original.

Mostre o total antes do desconto, o desconto e o valor final. Para calcular 10%, multiplique o total por `0.10`. Teste totais abaixo de 50, iguais a 50 e acima de 50.

## Exercício 03 — Comparando números

**Arquivo: `03_comparando_numeros.py`**

Leia dois números inteiros. Informe se o primeiro é maior, se o segundo é maior ou se os dois são iguais. Use uma cadeia `if` / `elif` / `else`.

## Exercício 04 — Termômetro da sala

**Arquivo: `04_termometro.py`**

Leia uma temperatura e mostre apenas uma classificação:

- abaixo de 18: `Ambiente frio`;
- a partir de 18 e abaixo de 26: `Ambiente agradável`;
- a partir de 26: `Ambiente quente`.

Teste especialmente os valores `18` e `26`.

## Exercício 05 — Boletim com decisão

**Arquivo: `05_boletim_condicional.py`**

Leia duas notas de mesmo peso. Se alguma nota estiver fora da faixa de 0 a 10, mostre `Nota inválida` e não calcule a média. Caso ambas sejam válidas, calcule e mostre a média e a situação:

- média a partir de 7: aprovado;
- média a partir de 5 e abaixo de 7: recuperação;
- média abaixo de 5: reprovado.

## Exercício 06 — Acesso à oficina

**Arquivo: `06_acesso_oficina.py`**

Leia a idade e pergunte se a pessoa possui inscrição (`sim/nao`). Considere idade não negativa e uma das duas respostas indicadas. A entrada só será permitida para quem tiver pelo menos 14 anos **e** inscrição confirmada.

Use `and`. Teste uma pessoa que atende aos dois critérios, outra que atende a apenas um e outra que não atende a nenhum.

## Exercício 07 — Benefício no museu

**Arquivo: `07_beneficio_museu.py`**

Leia uma idade não negativa. Neste museu fictício, pessoas com menos de 12 anos **ou** a partir de 60 anos têm entrada gratuita. As demais pagam R$ 20.00.

Use `or` e teste as idades `11`, `12`, `59` e `60`.

## Exercício 08 — Pedido de livros

**Arquivo: `08_pedido_livros.py`**

A biblioteca tem 8 exemplares disponíveis. Leia a quantidade que a pessoa deseja retirar.

- Se a quantidade for menor ou igual a zero, informe que o pedido é inválido.
- Se for maior que o estoque, informe que não há exemplares suficientes.
- Caso contrário, confirme o pedido, atualize o estoque e mostre a quantidade restante.

O estoque só deve diminuir quando o pedido for confirmado.

## Exercício 09 — Calculadora com menu

**Arquivo: `09_calculadora_menu.py`**

Leia dois números decimais. Mostre um menu com as opções `1` para somar, `2` para subtrair, `3` para multiplicar e `4` para dividir. Leia a opção como texto.

Execute somente a operação escolhida. Se a opção não existir, mostre `Opção inválida`. Na divisão, verifique se o segundo número é zero antes de calcular; nesse caso, mostre `Não é possível dividir por zero`.

## Exercício 10 — Corrigindo decisões

**Arquivo: `10_corrigindo_decisoes.py`**

O programa deveria permitir a participação de pessoas a partir de 16 anos que tenham autorização, mas contém erros:

```text
idade = input("Idade: ")
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao = "sim"
print("Participação permitida.")
else:
    print("Participação não permitida.")
```

Reescreva o código corrigindo a conversão da idade, o operador de comparação, os dois-pontos e a indentação. Explique cada correção em um comentário. Considere uma idade não negativa e as respostas `sim` ou `nao`.

---

# Desafio extra — Loja do aventureiro

**Arquivo: `11_loja_aventureiro.py`**

Crie uma loja com atendimento de uma única compra por execução.

1. Leia o nome do aventureiro e sua quantidade de ouro, como número inteiro.
2. Se o ouro for negativo, mostre `Quantidade de ouro inválida` e não prossiga com a compra.
3. Caso contrário, mostre um menu: `1` para poção de vida (25 moedas), `2` para escudo (60 moedas) e `3` para espada (100 moedas).
4. Leia a opção como texto e verifique se ela existe.
5. Para uma opção válida, verifique se o ouro é suficiente. Se for, desconte o preço e mostre o item adquirido e o saldo restante. Caso contrário, informe quantas moedas faltam.
6. Se a opção não existir, mostre `Item inválido`.

O ouro só pode ser descontado quando a compra for confirmada. Teste uma compra com sobra de ouro, uma com o valor exato, outra com saldo insuficiente, uma opção inválida e um saldo inicial negativo.

---

# Conferência antes de entregar

- As entradas numéricas foram convertidas para os tipos adequados?
- Os blocos estão indentados e as condições terminam com `:`?
- Foi usado `==` para comparar e `=` para atribuir?
- Os limites das regras foram respeitados, incluindo os casos de igualdade?
- Cada programa foi executado com entradas que percorrem caminhos diferentes?
- Estoques e saldos só são alterados quando a operação é permitida?
- As mensagens deixam claro o resultado de cada decisão?
