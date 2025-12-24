#implementacao de classe abstrata Funcionario
from .pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self,nome,cpf,data_nascimento,salario_base,id):
        super().__init__(nome,cpf,data_nascimento)
        self.__salario_base = salario_base
        self.__id = id

    def get_salario_base(self):
        return self.__salario_base
    def set_salario_base(self):
        pass
    def get_id(self):
        return self.__id
    def set_id(self):
        pass

    def registrar_venda(self, estoque, produto, quantidade):
        return estoque.vender_produto(produto, quantidade)
    def registrar_produto(self, estoque, produto, quantidade):
        estoque.adicionar_produto(produto, quantidade)
    def consultar_estoque(self, estoque):
        return estoque.consultar()