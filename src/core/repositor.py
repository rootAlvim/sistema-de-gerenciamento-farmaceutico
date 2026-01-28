#implementacao de classe Atendente
from decimal import Decimal
from src.core.funcionario import Funcionario
from src.utils.validacoes import validar_gerente
from src.core.mixins_interfaces.gerenciar_estoque import GerenciarEstoqueMixin

class Repositor(Funcionario,GerenciarEstoqueMixin):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id: int,farmacia, senha:str):
        super().__init__(nome, cpf, data_nascimento, salario_base, id,farmacia, senha)
        self.__porcentagemBonusRepositor = 0.025
  
    def get_bonus(self):
        '''Recebe bonus de 2.5% do salario base acrescentado ao bonus base de funcionario.'''
        calculo = super().get_bonus() + (self.get_salario_base() * Decimal(self.__porcentagemBonusRepositor))
        return calculo.quantize(Decimal('0.01')) 
    
    def setPorcentagemBonus(self, gerente, porcentagem: float):
        '''Recebe um objeto de gerente para validação e um novo valor para porcentagem de bonus salarial.'''
        validar_gerente(gerente)

        if not porcentagem > 0:
            raise ValueError("Porcentagem deve ser maior que zero")

        self.__porcentagemBonusRepositor = porcentagem / 100
    
    def __repr__(self):
        return f'Repositor("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'