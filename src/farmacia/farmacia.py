#implementacao de classe Farmacia
from decimal import Decimal
from core.funcionario import Funcionario
from core.atendente import Atendente
from core.gerente import Gerente
from venda import Venda

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__listaVendas = []
        self.gerente = None
        self.funcionarios = []

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def criarVenda(self, funcionario: Funcionario):
        '''Cria e retorna um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        venda = Venda(funcionario)
        self.__listaVendas.append(venda)

        return self.__listaVendas.index(venda)
        
    def registrarGerente(self):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        self.gerente = Gerente() # a ser implementado apos a criacao de gerente
        pass

    def registrarAtendente(self):
        '''Recebe como parametros atributos de um Atendente e cria um novo objeto do tipo Atendente. Retorna seu indice na lista de funcionarios.'''
        atendente = Atendente()
        self.funcionarios.append(atendente)
        return self.funcionarios.index(atendente)


