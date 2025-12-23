#implementacao de classe abstrata Funcionario

from abc import ABC , abstractmethod
from . pessoa import Pessoa

class Funcionario(Pessoa):
    def registrar_produto(self, estoque, produto, quantidade):
        estoque.adicionar_produto(produto, quantidade)

    def registrar_venda(self, estoque, produto, quantidade):
        return estoque.vender_produto(produto, quantidade)

    def consultar_estoque(self, estoque):
        return estoque.consultar()