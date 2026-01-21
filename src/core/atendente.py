#implementacao de classe Atendente
from decimal import Decimal
from src.core.funcionario import Funcionario

class Atendente(Funcionario):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id: int,farmacia, senha:str):
        super().__init__(nome, cpf, data_nascimento, salario_base, id,farmacia, senha)
        self.__porcentagemBonusAtendente = 0.015

    def get_bonus(self):
        '''Recebe bonus de 1.5% do salario base acrescentado ao bonus base de funcionario.'''
        calculo = super().get_bonus() + (self.get_salario_base() * Decimal(self.__porcentagemBonusAtendente))
        return calculo.quantize(Decimal('0.01')) 

    def __repr__(self):
        return f'Atendente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'