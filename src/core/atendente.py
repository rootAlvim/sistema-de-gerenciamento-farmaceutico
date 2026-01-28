#implementacao de classe Atendente
from decimal import Decimal
from src.core.funcionario import Funcionario
from src.utils.validacoes import validar_gerente
from src.core.mixins_interfaces.gerenciar_venda import GerenciarVendaMixin
class Atendente(Funcionario,GerenciarVendaMixin):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id: int,farmacia, senha:str):
        super().__init__(nome, cpf, data_nascimento, salario_base, id,farmacia, senha)
        self.__porcentagemBonusAtendente = 0.015
        self.__porcetagemComissaoVenda = 0.02
        self.__vendasRealizadas = []

    def get_bonus(self):
        '''Recebe bonus de 1.5% do salario base acrescentado ao bonus base de funcionario.'''
        calculo = super().get_bonus() + (self.get_salario_base() * Decimal(self.__porcentagemBonusAtendente))
        return calculo.quantize(Decimal('0.01')) 
    
    def get_comissao(self):
        '''Retorna valor total de comissões de vendas realizadas pelo funcionario de acordo com uma porcentagem interna.'''
        comissao = Decimal(0)
        for venda in self.getVendasRealizadas():
            comissao += venda.getPrecoTotal() * Decimal(self.__porcetagemComissaoVenda)
        return comissao.quantize(Decimal('0.01'))
    
    def getVendasRealizadas(self):
        '''Retorna lista de vendas realizadas'''
        return self.__vendasRealizadas
    
    def setVendaRealizada(self, venda):
        '''Adiciona nova venda realizada a lista de vendas do funcionario.'''
        self.__vendasRealizadas.append(venda)
    
    def removerVendaRealizada(self, farmacia, venda):
        '''Método usado por farmacia. Recebe como parametros um objeto de farmacia e venda.'''
        self.__vendasRealizadas.remove(venda)
    
    def setPorcentagemBonus(self, gerente, porcentagem: float):
        '''Recebe um objeto de gerente para validação e um novo valor para porcentagem de bonus salarial.'''
        validar_gerente(gerente)

        if not porcentagem > 0:
            raise ValueError("Porcentagem deve ser maior que zero")

        self.__porcentagemBonusAtendente = porcentagem / 100
    
    def setPorcentagemComissao(self, gerente, porcentagem: float):
        '''Recebe um objeto de gerente para validação e um novo valor para porcentagem de comissão de vendas.'''
        validar_gerente(gerente)

        if not porcentagem > 0:
            raise ValueError("Porcentagem deve ser maior que zero")

        self.__porcetagemComissaoVenda = porcentagem / 100
        
    def registrarCliente(self, nome : str, cpf : str, data_nascimento = None):
        '''Recebe atributos de cliente, registra um novo cliente em farmacia e retorna seu id'''
        return self.getFarmacia()._registrarCliente(self, nome, cpf, data_nascimento)

    def __repr__(self):
        return f'Atendente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'