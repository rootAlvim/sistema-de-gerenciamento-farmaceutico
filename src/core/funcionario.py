#implementacao de classe abstrata Funcionario
from datetime import datetime
from abc import abstractmethod
from decimal import Decimal
from src.core.pessoa import Pessoa
from src.utils.validacoes import validar_farmacia

class Funcionario(Pessoa):
    def __init__(self, nome:str, cpf:str, data_nascimento:datetime, salario_base:Decimal, id:int,farmacia, senha:str):
        super().__init__(nome,cpf,data_nascimento)
        self.__salario_base = Decimal(salario_base)
        self.__id = id
        self.__senha = senha
        self.__farmacia = farmacia
        self.__autenticado = False 
        
    def get_bonus(self):
        '''Retorna um bonus salarial base de 5%'''
        return self.__salario_base * Decimal(0.05)

    def getFarmacia(self): 
        '''Retorna objeto farmacia '''
        return self.__farmacia  
    
    def get_salario_base(self):
        '''Retorna salario do funcionario'''
        return self.__salario_base.quantize(Decimal('0.01'))
    
    def get_id(self):
        '''Retorna Id do funcionario'''
        return self.__id
    
    def get_senha(self, farmacia):
        '''Recebe objeto de Farmácia como validação. Retorna senha atual do funcionário.'''
        validar_farmacia(farmacia)
        senha = self.__senha
        return senha

    def get_isautenticado(self):
        '''Retorna True para autenticado False para não autenticado'''
        return self.__autenticado
    
    def setAutenticacao(self, id:int, senha:str):
        '''Recebe Id e senha de Funcionario e verifica se são validos. Retorna true e altera atributo privado caso dados sejam verdadeiros.'''
        if not id == self.__id: # Se o id passado não for igual ao id do funcionario
            raise ValueError("Id não correspondente")
        
        if not senha == self.__senha: # Se a senha passada não for igual a senha do funcionario
            raise ValueError("Senha não correspondente")
        
        self.__autenticado = True
        return True

    def desautenticar(self):
        '''Alterar atributo 'autenticado' para False.'''
        self.__autenticado = False

    def setNovaSenha(self, senhaAntiga:str, senhaNova:str):
        '''Altera senha de funcionario. Recebe confirmacao de senha antiga e uma nova senha, ambas strings.'''
        if not senhaAntiga == self.__senha: # Verifica se a senha passada e a senha do usuarui 
            raise ValueError("Confirmação de senha não corresponde à senha antiga")
        
        if not len(senhaNova) >= 5:
            raise ValueError("Nova senha deve conter no mínimo 5 caracteres")
        
        self.__senha = senhaNova
        return True
    
    def __str__(self):
        return f"ID {self.__id} | Nome: {self.nome} | Cargo: {self.__class__.__name__} | Salário: R$ {self.__salario_base:.2f}"
