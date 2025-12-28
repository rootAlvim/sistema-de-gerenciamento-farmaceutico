from .produto import Produto
from core.funcionario import Funcionario

class Estoque:
    def __init__(self):
        self.__produtos = {}  

    def get_produtos(self):
        return self.__produtos

