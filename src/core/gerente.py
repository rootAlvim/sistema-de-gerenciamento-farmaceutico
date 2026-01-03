#implementacao de classe Gerente
from src.core.funcionario import Funcionario
from src.core.mixins_interfaces.funcionalidades_gerente import FuncionalidadesGerente

class Gerente(Funcionario,FuncionalidadesGerente):
    def __init__(self,nome,cpf,data_nascimento,salario_base,id):
        super().__init__(nome,cpf,data_nascimento,salario_base,id, cargo = 'Gerente')

    def cadrastar_funcionario(self):
        pass
    def excluir_funcionario(self):
        pass
    def alterar_preco_produto(self):
        pass