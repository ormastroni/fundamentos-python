class Bola:

    def __init__(self, cor, circ, material):
        self._cor = cor
        self._circunferencia = circ
        self._material = material
    
    def trocaCor(self, novacor):
        self._cor = novacor
    
    def mostraCor(self):
        return self._cor

    def mostraMaterial(self):
        return self._material

    def __str__(self):
        return self._cor + ';' + self._material

    def __eq__(self, b):
        if (self.mostraCor() == b.mostraCor()):
            return True
        return False

b1 = Bola("Vermelha", 10, "Plastico")
b2 = Bola("Vermelha", 30, "Papel")

if (b1 == b2):
    print("as bolas sao iguais")
else:
    print('as bolas sao diferentes')

print(b1)
print(b2)