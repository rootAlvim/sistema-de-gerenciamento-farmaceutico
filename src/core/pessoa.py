#implementacao de classe abstrata Pessoa
from datetime import datetime
from typing import Optional
from src.utils.validacoes import validar_formato_cpf
from abc import ABC , abstractmethod
class Pessoa(ABC):
    def __init__(self,nome:str,cpf:str,data_nascimento:Optional[datetime] = None):
        self.nome = nome
        self.__cpf = validar_formato_cpf(cpf) # Valida CPF
        self.__data_nascimento = data_nascimento or datetime.now()

    @abstractmethod
    def __str__(self):
        pass
    
    def get_cpf(self):
        '''Retorna CPF da pessoa'''
        return self.__cpf
    
    def get_data_nascimento(self):
        '''Retorna a data de nascimento da pessoa'''
        return self.__data_nascimento
    
    def set_cpf(self,cpf):
        '''Validação do recadrasto do CPF'''
        if not validar_formato_cpf(cpf):
            raise ValueError ("CPF inválido") #|Execulta quando a condição e falsa
        else:
            self.__cpf = cpf #|Execulta quando a condicao e verdadeira
            return True

        


