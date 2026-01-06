#implementacao de classe Cliente
from src.core.pessoa import Pessoa
from datetime import datetime
class Cliente(Pessoa):
    def __init__(self,nome:str,cpf:str, id_cliente:int,data_nascimento=None,):
        super().__init__(nome,cpf,data_nascimento)
        self.__id_cliente = id_cliente

    def get_id_cliente (self):
        self.get_cpf = self.__id_cliente
        return self.__id_cliente
    def __str__(self):
        return f'Nome: {self.nome} | Id: {self.get_id_cliente()}'