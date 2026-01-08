#implementacao de classe Venda
from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from src.utils.gerador_id import getIdProduto
from src.utils.validacoes import validar_cliente, validar_funcionario, validar_produto

class Venda:
    allIds = []
    def __init__(self, id : int, funcionario, cliente = None):
        self.__id = id
        self.__funcionario = funcionario
        self.__cliente = cliente
        self.__precoTotal = Decimal("0")
        self.__produtos = []
        self.__dataVenda = datetime.now()
        self.__logAlteracoes = []

    def getId(self):
        '''Retorna ID de venda'''
        return self.__id
    
    def getFuncionario(self):
        '''Retorna um objeto do tipo Funcionario'''
        return self.__funcionario
    
    def getPrecoTotal(self):
        '''Retorna preço total da Venda'''
        return self.__precoTotal
    
    def getProdutos(self):
        '''Retorna lista com tuplas de produtos e suas quantidades'''
        return self.__produtos
    
    def getLogAlteracoes(self):
        '''Retorna lista de tuplas sobre alterações de Venda'''
        return self.__logAlteracoes
    
    def getCliente(self):
        '''Retorna cliente caso exista em Venda'''
        return self.__cliente
    
    def adicionarCliente(self, funcionario, cliente):
        '''Adiciona um cliente em Venda. Recebe objetos de funcionario e cliente.'''
        validar_funcionario(funcionario)
        validar_cliente(cliente)

        if self.__precoTotal:
            raise PermissionError('Venda já finalizada. Não é mais possível adicionar cliente')
        
        self.__cliente = cliente
        log =(f'Data:{datetime.now()}',f'{funcionario.__repr__()}',f'{cliente.__repr__()}')
        self.__logAlteracoes.append(log)
    
    def adicionarProduto(self, produto, quantidade : int):
        '''Adiciona produto em Venda, caso produto já exista, a sua quantidade é somada. Recebe como parâmetro um objeto do tipo Produto e uma quantidade inteira. Não é possível adicionar produto se venda tiver sido finalizada'''
        validar_produto(produto) 
        
        if self.__precoTotal:
            raise PermissionError('Venda já finalizada. Não é mais possível adicionar produtos')
        
        if int(quantidade) < 0:
            raise ValueError('Quantidade deve ser maior que 0')
        
        for index, itemVenda in enumerate(self.__produtos):
            if produto.__repr__() in itemVenda:
                self.__produtos[index] = (produto.__repr__(), itemVenda[1] + quantidade)
                return True
                
        self.__produtos.append((produto.__repr__(), quantidade))
        
    def setPrecoTotal(self, funcionario):
        '''Altera preco total da venda com base em produtos já adicionados e suas quantidades. Recebe um objeto do tipo Funcionario. Esse metodo sinaliza a finalizacao da compra'''
        validar_funcionario(funcionario)
        
        if self.__precoTotal:
            raise PermissionError('Venda já foi finalizada.')
        
        self.__precoTotal = self.__subTotal()
        log = (f'Data:{datetime.now()}',f'Funcionario:{funcionario.__repr__()}',f'Preco:{self.__precoTotal}')
        self.__logAlteracoes.append(log)
    
    def __subTotal(self):
        '''Método privado para calcular subtotal da venda.'''
        from src.farmacia.produto import Produto
        subTotal = Decimal(0)
        for itemVenda in self.__produtos:
            try:
                produto = eval(itemVenda[0])
            except Exception as e:
                raise TypeError(f"Erro ao instanciar Produto: {e}")

            subTotal += produto.getPreco() * itemVenda[1]

        return subTotal