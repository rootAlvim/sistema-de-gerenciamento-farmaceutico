#implementacao de classe Venda
from core.funcionario import Funcionario
from datetime import datetime
from decimal import Decimal

class Venda:
    def __init__(self, funcionario: Funcionario):
        self.__id = 0
        self.__funcionario = funcionario
        self.__precoTotal = Decimal("0")
        self.__produtos = []
        self.__dataVenda = datetime.now()
        self.__logAlteracoes = []

    def getId(self):
        '''Returna ID de venda'''
        return self.__id
    
    def getFuncionario(self):
        '''Returna um objeto do tipo Funcionario'''
        return self.__funcionario
    
    def getPrecoTotal(self):
        '''Returna preco total da Venda'''
        return self.__precoTotal
    
    def setPrecoTotal(self, funcionario: Funcionario, valor: Decimal):
        '''Setter para alterar preco total da venda. Recebe um objeto do tipo Funcionario e um valor do tipo Decimal. Adiciona a atual modificacao ao Log de Alteracoes'''
        if valor > 0:
            self.__precoTotal = valor
            log = f'Data:{datetime.now()};Funcionario:{funcionario};Valor:{valor}'
            self.__logAlteracoes.append(log)

        raise ValueError("O valor de preço total deve ser maior que 0")