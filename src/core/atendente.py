#implementacao de classe Atendente
from src.core.funcionario import Funcionario

class Atendente(Funcionario):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id: int):
        super().__init__(nome, cpf, data_nascimento, salario_base, id)
