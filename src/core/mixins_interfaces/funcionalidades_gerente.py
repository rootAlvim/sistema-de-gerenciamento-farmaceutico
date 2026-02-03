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
    @abstractmethod
    def consultar_log_alteracoes_farmacia(self):
        pass
    @abstractmethod
    def consultar_chamados(self):
        pass
    @abstractmethod
    def alterar_status_chamado(self):
        pass
    
