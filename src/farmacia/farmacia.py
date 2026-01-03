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
        self._estoque = Estoque()
        self.gerente = None
        self.funcionarios = []

    def getIdUnico(self, idParaVenda = False, idParaProduto = False, idParaAtendente = False):
        '''Recebe como paramentro um valor Booleano que define se o metodo deve retornar um Id para Venda,para Produto ou para Atendente. Verifica todos os ids existentes de venda, produto ou atendente torna um novo Id unico aleatorio.'''
        if (not idParaVenda and not idParaProduto and not idParaAtendente) or (idParaVenda and idParaProduto and idParaAtendente):
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
            if self._estoque.get_produtos():
                allIds = []
                for produto in self._estoque.get_produtos().keys():
                    allIds.append(produto.getId())
                
                Id = 0
                while Id in allIds:
                    Id = randint(1, 2048)
                return Id
            return randint(1, 2048)
        
        if idParaAtendente:
            allIds = []
            for atendente in self.funcionarios:
                allIds.append(atendente.get_id())

            Id = 0
            while Id in allIds:
                Id = randint(1, 2048)
            return Id

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def criarVenda(self, funcionario: Funcionario):
        '''Cria um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        venda = Venda(self.getIdUnico(idParaVenda=True), funcionario)
        self.__listaVendas.append(venda)

        return self.__listaVendas.index(venda)
     
    def registrarGerente(self, nome, cpf, data_nasc, salario):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        id_novo = randint(1, 100)
        self.gerente = Gerente(nome, cpf, data_nasc, salario, id_novo)
        
    def registrarAtendente(self, nome, cpf, data_nasc, salario):
        '''Recebe como parametros atributos de um Atendente e cria um novo objeto do tipo Atendente. Retorna seu indice na lista de funcionarios.'''
        id_novo = self.getIdUnico(idParaAtendente=True)
        atendente = Atendente(nome, cpf, data_nasc, salario, id_novo)
        self.funcionarios.append(atendente)
        return self.funcionarios.index(atendente)


