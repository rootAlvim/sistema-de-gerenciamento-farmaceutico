#implementacao de classe Farmacia
from decimal import Decimal
from src.core.funcionario import Funcionario
from src.core.atendente import Atendente
from src.core.gerente import Gerente
from src.farmacia.venda import Venda
from src.farmacia.estoque import Estoque
from random import randint

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__listaVendas = []
        self._estoque = None
        self.gerente = None
        self.funcionarios = []

    def getIdUnico(self, idParaVenda = False, idParaProduto = False):
        '''Recebe como paramentro um valor Booleano que define se o metodo deve retornar um Id para Venda ou para Produto. Verifica todos os ids existentes de venda ou produto e retorna um novo int unico aleatorio.'''
        if (not idParaVenda and not idParaProduto) or (idParaVenda and idParaProduto):
            raise ValueError("Parametro incorreto: forneca apenas um valor booleano corretamente")
        
        if idParaVenda:
            allIds = []
            for venda in self.__listaVendas:
                allIds.append(venda.getId())

            Id = 0
            while Id in allIds:
                Id = randint(1, 2048)
            return Id
        
        if idParaProduto:
            if self._estoque and self._estoque.get_produtos():
                allIds = []
                for produto in self._estoque.get_produtos():
                    allIds.append(produto[0].getId())

                Id = 0
                while Id in allIds:
                    Id = randint(1, 2048)
                return Id
            return randint(1, 2048)

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def criarVenda(self, funcionario: Funcionario):
        '''Cria um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        venda = Venda(self.getIdUnico(idParaVenda=True), funcionario)
        self.__listaVendas.append(venda)

        return self.__listaVendas.index(venda)
    
    def criarEstoque(self):
        '''Cria um objeto do tipo Estoque. Atribui ele a self._estoque'''
        self._estoque = Estoque()
        
    def registrarGerente(self):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        self.gerente = Gerente() # a ser implementado apos a criacao de gerente
        pass

    def registrarAtendente(self):
        '''Recebe como parametros atributos de um Atendente e cria um novo objeto do tipo Atendente. Retorna seu indice na lista de funcionarios.'''
        atendente = Atendente()
        self.funcionarios.append(atendente)
        return self.funcionarios.index(atendente)


