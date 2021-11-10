from livro import Livro
from cliente import Cliente

l1 = Livro('111', 'Mestre do Python', 'Ramalho', 15.5)
l2 = Livro('222', 'Java Completo', 'Andre', 199.9)
l3 = Livro('333', 'Oracle', 'Joao')

print(l1.getTitulo())
print(l2.getTitulo())
print(l3.getTitulo())

c = Cliente("Andre", '111', 40)
print(c.getNome())