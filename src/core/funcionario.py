#implementacao de classe abstrata Funcionario
from datetime import datetime
from .pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self,nome:str,cpf:str,data_nascimento:datetime,salario_base:float,id:int):
        super().__init__(nome,cpf,data_nascimento)
        self.__salario_base = salario_base
        self.__id = id
        self.__autenticado = True
        
    def get_salario_base(self):
        '''Retorna salario do funcionario'''
        return self.__salario_base
    
    def get_id(self):
        '''Retorna Id do funcionario'''
        return self.__id
    
    def get_isautenticado(self):
        '''Retorna True para autenticado False para não autenticado'''
        return self.__autenticado
    
    def adicionar_produto(self, produto, quantidade,estoque):
        produtos_estoque = estoque.get_produtos()
        if produto.id in produtos_estoque:
            produtos_estoque[produto.id]["quantidade"] += quantidade
        else:
            produtos_estoque[produto.id] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def vender_produto(self, id_produto, quantidade,estoque):
        produtos_estoque = estoque.get_produtos()
        if id_produto in produtos_estoque:
            if produtos_estoque[id_produto]["quantidade"] >= quantidade:
                produtos_estoque[id_produto]["quantidade"] -= quantidade
                return True
            else:
                print('Quantidade insuficiente')
        else:
            print('Produto não encontrado.')
        return False
    
    def consultar(self,estoque):
        if not estoque.get_produtos():
            return "Estoque vazio"

        return {
            dados["produto"].nome: dados["quantidade"]
            for dados in estoque.get_produtos().values()
        }