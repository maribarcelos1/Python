

def print_tabuada(tabuada):
    for titem in tabuada:
        print(titem.alvo, " X ", titem.multiplicador, " = ", titem.resultado)


class tabuada_item:
    def __init__(self, alvo, multiplicador):
        self.alvo = alvo
        self.multiplicador = multiplicador

    def calcula(self):
        self.resultado = self.alvo * self.multiplicador


if __name__ == "__main__":
    numeroAlvo = int(input('qual o numero:'))
    tabuada = []
    for multiplicador in range(1, 11):
        tabuadaItem = tabuada_item(numeroAlvo, multiplicador)
        tabuadaItem.calcula()
        tabuada.append(tabuadaItem)
    print_tabuada(tabuada)
