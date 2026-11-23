# Uma sala possui duas lâmpadas que podem ser ligadas e desligadas separadamente.
# Classe: Lampada
# Atributos: local e ligada
# Comportamentos: ligar() e desligar()

class Lampada:
    def __init__(self, local):
        self.local = local
        self.ligada = False

    def ligar(self):
        if self.ligada:
            return False
        self.ligada = True
        return True

    def desligar(self):
        if not self.ligada:
            return False
        self.ligada = False
        return True


entrada = Lampada("entrada")
fundo = Lampada("fundo")

print(entrada.ligar())
print(entrada.ligar())
print(entrada.desligar())
print(entrada.desligar())

print("Entrada ligada:", entrada.ligada)
print("Fundo ligada:", fundo.ligada)

# O retorno do método informa se a operação mudou o estado da lâmpada.
# O valor de 'ligada' mostra o estado atual depois da operação.
# Exemplo: ao chamar ligar(), o retorno pode ser True e o atributo ligado passa a ser True;
# se a lâmpada já estiver ligada, o retorno será False e o atributo continua True.


