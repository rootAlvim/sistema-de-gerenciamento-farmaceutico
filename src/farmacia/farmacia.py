#implementacao de classe Farmacia
from decimal import Decimal
from core.funcionario import Funcionario
from venda import Venda

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__listaVendas = []
        self.__funcionarios = []

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def criarVenda(self, id: int, funcionario: Funcionario):
        '''Cria e retorna um objeto do tipo Venda. Adiciona obejto em Lista de Vendas'''
        # a ser implementado
        pass

    def registrarGerente(self):
        '''Cria um novo objeto do tipo Gerente e retorna o seu ID. Adiciona novo Gerente a lista de funcionarios'''
        pass

    def registrarAtendente(self):
        '''Cria um novo objeto do tipo Atentende e retorna o seu ID. Adiciona novo Antende a lista de funcionarios'''
        pass

