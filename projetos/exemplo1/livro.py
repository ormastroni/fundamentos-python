class Livro:

  def __init__(self, isbn, titulo, autor, preco=0):
    self._isbn = isbn
    self._titulo = titulo
    self._autor = autor
    self._preco = preco
    self._estoque = 10

  def getTitulo(self):
    return self._titulo

  def getAutor(self):
    return self._autor

  def getPreco(self):
    return self._preco

  def getEstoque(self):
    return self._estoque

  def atualizaEstoque(self, novo):
    self._estoque = novo