class Marcador:
    def __init__(self, valor):
        self.valor = valor

    def somar(self, quantidade):
        self.valor = self.valor + quantidade


# Versão original: atalho referencia o mesmo objeto que primeiro.
primeiro = Marcador(10)
atalho = primeiro
segundo = Marcador(10)

atalho.somar(5)
segundo.somar(2)
print("Versão original:")
print(primeiro.valor)
print(atalho.valor)
print(segundo.valor)

# A atribuição muda a referência de atalho, sem criar objeto novo.
atalho = segundo
atalho.somar(3)
print(segundo.valor)


# Versão independente: atalho recebe um objeto diferente.
print("Versão independente:")
primeiro_independente = Marcador(10)
atalho_independente = Marcador(10)
segundo_independente = Marcador(10)

atalho_independente.somar(5)
segundo_independente.somar(2)
print(primeiro_independente.valor)
print(atalho_independente.valor)
print(segundo_independente.valor)

atalho_independente = segundo_independente
atalho_independente.somar(3)
print(segundo_independente.valor)


# Referências da versão original:
# Antes de atalho = segundo:
# primeiro -> objeto A (valor 15)
# atalho  -> objeto A (valor 15)
# segundo -> objeto B (valor 12)
# Depois:
# primeiro -> objeto A
# atalho  -> objeto B
# segundo -> objeto B

# Foram criados dois objetos na versão original. atalho = segundo apenas
# altera a referência da variável; não chama Marcador nem cria outro objeto.

# Na versão independente, primeiro_independente, atalho_independente e
# segundo_independente são três objetos separados. Somar em atalho não altera
# primeiro_independente, mas a atribuição posterior faz atalho apontar para
# segundo_independente, alterando o mesmo objeto que segundo_independente representa.

