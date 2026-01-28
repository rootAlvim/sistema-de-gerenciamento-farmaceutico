#implementacao de classe Venda
from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from src.utils.gerador_id import getIdProduto
from src.utils.validacoes import validar_cliente, validar_produto, validar_funcionario

class Venda:
    allIds = []
    def __init__(self, id : int, funcionario):
        self.__id = id
        self.__funcionario = funcionario
        self.__cliente = None
        self.__precoTotal = Decimal("0")
        self.__itens = []
        self.__dataVenda = datetime.now()
        self.__logAlteracoes = []

    def getId(self):
        '''Retorna ID de venda.'''
        return self.__id
    
    def getDataVenda(self):
        '''Retorna data de criação da venda.'''
        return self.__dataVenda
    
    def getFuncionario(self):
        '''Retorna um objeto do tipo Funcionario.'''
        return self.__funcionario
    
    def getPrecoTotal(self):
        '''Retorna preço total da Venda.'''
        return self.__precoTotal.quantize(Decimal('0.01'))
    
    def getProdutos(self):
        '''Retorna lista com objetos de ItemVenda contendo dados dos produtos e suas quantidades.'''
        return self.__itens
    
    def getLogAlteracoes(self):
        '''Retorna lista de tuplas sobre alterações de Venda'''
        return self.__logAlteracoes
    
    def getCliente(self):
        '''Retorna cliente caso exista em Venda'''
        return self.__cliente
    
    def adicionarCliente(self, funcionario, cliente):
        '''Adiciona um cliente em Venda. Recebe objeto de funcionario e de cliente.'''
        validar_funcionario(funcionario)
        validar_cliente(cliente)

        if self.__precoTotal :
            raise PermissionError('Venda já finalizada. Não é mais possível adicionar cliente')
        
        self.__cliente = cliente
        self.__cliente._addCompra(self)

        log =(
            f'adicionarCliente()', 
            f'Data:{datetime.now()}',
            f'{cliente.__repr__()}'
        )

        self.__logAlteracoes.append(log)
    
    def adicionarProduto(self, funcionario, produto, quantidade : int):
        '''Adiciona produto em Venda, caso produto já exista, a sua quantidade é somada. Recebe como parâmetro objeto de funcionario, um objeto do tipo Produto e uma quantidade inteira. Não é possível adicionar produto se venda tiver sido finalizada'''
        validar_funcionario(funcionario)
        validar_produto(produto) 
        
        if self.__precoTotal :
            raise PermissionError('Venda já finalizada. Não é mais possível adicionar produtos')
        
        if int(quantidade) <= 0:
            raise ValueError('Quantidade deve ser maior que 0')
        
        for itemVenda in self.__itens:   
            if produto.getId() == itemVenda.id:
                itemVenda.quantidade += quantidade
                return True

        self.__itens.append(
            ItemVenda(
                produto.getId(),
                produto.nome,
                produto.getPreco(),
                int(quantidade)
            )
        )

    def removerProduto(self, funcionario, id_produto: int, quantidade: int = None):
        '''Recebe objeto de funcionario para validação, Id de produto e um inteiro para quantidade. Caso quantidade não seja passada, produto é removido por completo de venda.'''
        validar_funcionario(funcionario)
        if self.__precoTotal:
            raise PermissionError("Venda já foi finalizada. Não é mais possível remover produto")

        for itemVenda in self.__itens:   
            if int(id_produto) == itemVenda.id:
                if not quantidade:
                    self.__itens.remove(itemVenda)
                    return True
                
                if quantidade > itemVenda.quantidade:
                    raise ValueError("Quantidade excede valor disponível para remoção")
                
                itemVenda.quantidade = itemVenda.quantidade - quantidade
                return True
        raise ValueError("Produto não está adicionado em venda")
    
    def finalizarVenda(self, funcionario):
        '''Altera preco total da venda com base em produtos já adicionados e suas quantidades. Recebe um objeto do tipo Funcionario. Esse metodo sinaliza a finalização da compra.'''
        validar_funcionario(funcionario)
        
        if self.__precoTotal :
            raise PermissionError("Venda já finalizada")
        
        if not self.__subTotal():
            raise ValueError("Venda precisa de pelo menos um produto para ser finalizada")

        self.__precoTotal = self.__subTotal()
        log = (
            f'finalizarVenda()', 
            f'Data:{datetime.now()}',
            f'Preco:{self.__precoTotal}')

        self.__logAlteracoes.append(log)
    
    def __subTotal(self):
        '''Método privado para calcular subtotal da venda.'''
        from src.farmacia.produto import Produto
        subTotal = Decimal(0)
        for itemVenda in self.__itens:
            subTotal += itemVenda.subTotal()
        return subTotal
    
    def __str__(self):
        return f'Venda: Id={self.__id}| Funcionario=({self.__funcionario.__str__()})| Data={self.__dataVenda.date()}'

    def __repr__(self):
        return f'Venda({self.__id}, {self.__funcionario.__repr__()})'
    
class ItemVenda:
    def __init__(self, id: int, nome: str, preco: Decimal, quantidade: int):
        self.id = id
        self.nome = nome
        self.preco = Decimal(preco).quantize(Decimal('0.01'))
        self.quantidade = quantidade

    def subTotal(self):
        '''Retorna o subtotal do item, multiplicando preço do produto por sua quantidade.'''
        return self.preco * Decimal(self.quantidade)
    
    def __str__(self):
        return f'Produto: Id={self.id} | Nome={self.nome} | Preço={self.preco} | Quantidade={self.quantidade}'
