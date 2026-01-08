from src.utils.gerador_id import getIdProduto
from src.utils.validacoes import validar_gerente
from decimal import Decimal
from datetime import datetime

class Produto:
    allIds = []
    def __init__(self, nome : str, preco : Decimal, fabricante : str, id : int = None, logAlteracoes : list = None):
        self.__id = id if id else getIdProduto(self)
        self.nome = nome
        self.__preco = Decimal(preco)
        self.fabricante = fabricante
        self.__logAlteracoes = logAlteracoes if logAlteracoes else []

    def getId(self):
        '''Retorna o Id de Produto.'''
        return self.__id
    
    def getPreco(self):
        '''Retorna o preco de Produto.'''
        precoTruncado = self.__preco.quantize(Decimal('0.01'))
        return precoTruncado
    
    def getLogAlteracoes(self):
        '''Retorna lista de tuplas sobre alterações de Produto'''
        return self.__logAlteracoes
    
    def setPreco(self, preco : Decimal, gerente):
        '''Recebe como parametro o novo valor de preco em Decimal e um objeto de Gerente. Altera o preco de Produto.'''
        validar_gerente(gerente)
        
        if preco < 0:
            raise ValueError('Preco deve ser maior que 0')
        
        self.__preco = preco
        log =(f'Data:{datetime.now()}',f'{gerente.__repr__()}',f'Preco:{preco}')
        self.__logAlteracoes.append(log)
    
    def __repr__(self):
        return rf'Produto("{self.nome}", {self.getPreco()}, "{self.fabricante}", {self.__id}, {self.__logAlteracoes})'