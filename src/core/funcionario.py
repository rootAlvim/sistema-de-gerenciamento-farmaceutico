#implementacao de classe abstrata Funcionario
from datetime import datetime
from src.core.pessoa import Pessoa
from Mixins_Interfaces.adicionar_produto import Adicionar_ProdutoMixin
from Mixins_Interfaces.vender_produto import Vender_ProdutoMixin
class Funcionario(Pessoa,Adicionar_ProdutoMixin,Vender_ProdutoMixin):
    def __init__(self,nome:str,cpf:str,data_nascimento:datetime,salario_base:float,id:int, cargo:str):
        super().__init__(nome,cpf,data_nascimento)
        self.__salario_base = salario_base
        self.__id = id
        self.__autenticado = True 
        self.cargo = cargo
        
        
    
    def get_salario_base(self):
        '''Retorna salario do funcionario'''
        return self.__salario_base
    
    def get_id(self):
        '''Retorna Id do funcionario'''
        return self.__id
    
    def get_isautenticado(self):
        '''Retorna True para autenticado False para não autenticado'''
        return self.__autenticado
    
    def subTotal(self, estoque):
        produtos_estoque = estoque.get_produtos()
        total = 0

        '''for registro in produtos_estoque.values():
            produto = registro["produto"]
            quantidade = registro["quantidade"]
            total += produto.preco * quantidade

        return total'''
        for dados in produtos_estoque.values():
            produto = dados["produto"]
            quantidade = dados["quantidade"]
            subtotal = produto.preco * quantidade
            print(f"{produto.nome} - R$ {subtotal:.2f}")
    
    def consultar(self,estoque):
        if not estoque.get_produtos():
            return "Estoque vazio"

        return {
        
            dados["produto"].nome: dados["quantidade"]
            for dados in estoque.get_produtos().values()
        } 
    

