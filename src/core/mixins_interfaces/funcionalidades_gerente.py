#implementacao de classe interceface FuncionalidadesGerente
from abc import ABC, abstractmethod
class FuncionalidadesGerente(ABC):
    @abstractmethod
    def cadrastar_funcionario(self):
        pass
    @abstractmethod
    def excluir_funcionario(self):
        pass
    @abstractmethod
    def alterar_preco_produto(self):
        pass
    
