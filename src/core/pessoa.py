#implementacao de classe abstrata Pessoa

from abc import ABC , abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,cpf,data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento