#implementacao de classe abstrata Pessoa
from datetime import datetime
from typing import Optional
from utils.validacoes import validar_formato_cpf
from abc import ABC , abstractmethod
class Pessoa(ABC):
    def __init__(self,nome:str,cpf:str,data_nascimento:Optional[datetime] = None):
        self.nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento or datetime.now()

    def get_cpf(self):
        '''Retorna CPF da pessoa'''
        return self.__cpf
    
    def get_data_nascimento(self):
        '''Retorna a data de nascimento da pessoa'''
        return self.__data_nascimento
    
    def set_cpf(self,cpf):
        '''Validação do recadrasto de cpf'''
        if validar_formato_cpf(cpf):
            self.__cpf = cpf
            print('CPF Recadrastado com sucesso!')
        else:
            print('CPF com formato inválido') 

