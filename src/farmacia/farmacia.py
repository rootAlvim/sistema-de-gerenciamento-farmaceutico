#implementacao de classe Farmacia
from decimal import Decimal
from datetime import datetime
from src.farmacia.estoque import Estoque
from src.utils.validacoes import validar_funcionario , validar_gerente

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__vendas = []
        self._estoque = Estoque()
        self.__gerente = None
        self.__funcionarios = []
        self.__clientes = []
        self.__idFuncionarios = 0
        self.__idVendas = 0
        self.__logAlteracoes = []

    def getGerente(self):
        '''Retorna um objeto de Gerente.'''
        return self.__gerente
    
    def getFuncionarios(self):
        '''Retorna uma lista contendo todos os objetos de Funcionarios'''
        return self.__funcionarios

    def getFuncionarioPorId(self, id):
        '''Retorna objeto de Funcionario caso exista um com o mesmo id recebido.'''
        for funcionario in self.__funcionarios:
            if funcionario.get_id() == id:
                return funcionario
            
        if self.__gerente.get_id() == id:
            return self.__gerente

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados.'''
        return self.__vendas
    
    def getVendaPorId(self, id):
        '''Retorna objeto de Venda caso exista uma venda com o mesmo Id.'''
        for venda in self.__vendas:
            if venda.getId() == id:
                return venda
    
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
            
    def getLogAlteracoes(self):
        '''Retorna lista de tuplas sobre alterações em Farmacia'''
        return self.__logAlteracoes

    def _criarVenda(self, funcionario):
        '''Cria um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        from src.farmacia.venda import Venda
        validar_funcionario(funcionario)
        
        self.__idVendas += 1
        venda = Venda(self.__idVendas, funcionario)
        self.__vendas.append(venda)
        funcionario.setVendaRealizada(venda)

        log =(
            f'criarVenda()',
            f'Data:{datetime.now()}',
            f'{venda.__repr__()}'
        )

        self.__logAlteracoes.append(log)

        return venda.getId()   

    def _registrarGerente(self, nome, cpf, data_nasc, salario, senha):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        from src.core.gerente import Gerente
        self.__idFuncionarios += 1
        self.__gerente = Gerente(nome, cpf, data_nasc, salario, self.__idFuncionarios,self, senha)

        log =(
            f'registrarGerente()', 
            f'Data:{datetime.now()}',
            f'{self.__gerente.__repr__()}'
        )
        
        self.__logAlteracoes.append(log)
        
    def _registrarAtendente(self, gerente, nome : str , cpf : str, data_nasc : datetime , salario : Decimal, senha):
        '''Recebe como parametros um objeto de Gerente para controle e atributos de um Atendente, e cria um novo objeto do tipo Atendente. Retorna seu id.'''
        validar_gerente(gerente)
        from src.core.atendente import Atendente
        self.__idFuncionarios += 1
        atendente = Atendente(nome, cpf, data_nasc, salario, self.__idFuncionarios,self, senha)
        
        self.__funcionarios.append(atendente)

        log =(
            f'registrarAtendente()',
            f'{gerente.__repr__()}'
            f'Data:{datetime.now()}',
            f'{atendente.__repr__()}'
        )

        self.__logAlteracoes.append(log)

        return atendente.get_id()
    
    def _registrarRepositor(self, gerente, nome : str , cpf : str, data_nasc : datetime , salario : Decimal, senha):
        '''Recebe como parametros um objeto de Gerente para controle e atributos de um Atendente, e cria um novo objeto do tipo Atendente. Retorna seu id.'''
        validar_gerente(gerente)
        from src.core.repositor import Repositor
        self.__idFuncionarios += 1
        repositor = Repositor(nome, cpf, data_nasc, salario, self.__idFuncionarios,self, senha)
        
        self.__funcionarios.append(repositor)

        log =(
            f'registrarRepositor()',
            f'{gerente.__repr__()}'
            f'Data:{datetime.now()}',
            f'{repositor.__repr__()}'
        )

        self.__logAlteracoes.append(log)

        return repositor.get_id()
    
    def _registrarCliente(self, funcionario, nome : str, cpf : str, data_nascimento = None):
        '''Recebe como parametros um objeto de Funcionario e atributos de um Cliente, e cria um novo objeto do tipo Cliente. Retorna Id do novo cliente.'''
        validar_funcionario(funcionario)

        from src.core.cliente import Cliente
        cliente = Cliente(nome, cpf, data_nascimento)

        self.__clientes.append(cliente)
        log =(
            f'registrarCliente()', 
            f'Data:{datetime.now()}',
            f'{cliente.__repr__()}'
        )

        self.__logAlteracoes.append(log)
        
        return cliente.get_cpf()


