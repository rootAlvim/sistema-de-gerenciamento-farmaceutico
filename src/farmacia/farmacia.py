#implementacao de classe Farmacia
from decimal import Decimal
from src.farmacia.estoque import Estoque
from src.utils.validacoes import validar_funcionario
from random import randint

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__listaVendas = []
        self._estoque = Estoque()
        self.gerente = None
        self.funcionarios = []
        self.__clientes = []
        self.__idGerentes = 0
        self.__idAtendentes = 0
        self.__idVendas = 0

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def getClientes(self):
        '''Retorna uma lista contendo todos os objetos de Cliente registrados'''
        return self.__clientes
    
    def getClientePorCpf(self, cpf):
        '''Retorna objeto de cliente caso exista um com o mesmo cpf recebido.'''
        import re
        cpf = re.sub(r'\D', '', cpf)
        
        for cliente in self.__clientes:
            cpf_cliente = re.sub(r'\D', '', cliente.get_cpf())
            if cpf == cpf_cliente:
                return cliente

    def criarVenda(self, funcionario):
        '''Cria um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        from src.farmacia.venda import Venda
        validar_funcionario(funcionario)
        self.__idVendas += 1
        venda = Venda(self.__idVendas, funcionario)
        self.__listaVendas.append(venda)

        return self.__listaVendas.index(venda)
     
    def registrarGerente(self, nome, cpf, data_nasc, salario):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        from src.core.gerente import Gerente
        self.__idGerentes += 1
        self.gerente = Gerente(nome, cpf, data_nasc, salario, self.__idGerentes)
        
    def registrarAtendente(self, nome, cpf, data_nasc, salario):
        '''Recebe como parametros atributos de um Atendente e cria um novo objeto do tipo Atendente. Retorna seu indice na lista de funcionarios.'''
        from src.core.atendente import Atendente
        self.__idAtendentes += 1
        atendente = Atendente(nome, cpf, data_nasc, salario, self.__idAtendentes)
        
        self.funcionarios.append(atendente)
        return self.funcionarios.index(atendente)
    
    def registrarCliente(self, nome : str, cpf : str, data_nascimento = None):
        '''Recebe como parametros atributos de um Cliente e cria um novo objeto do tipo Cliente. Retorna seu indice na lista de clientes.'''
        from src.core.cliente import Cliente
        cliente = Cliente(nome, cpf, data_nascimento)

        self.__clientes.append(cliente)
        return self.__clientes.index(cliente)

