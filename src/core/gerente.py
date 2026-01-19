#implementacao de classe Gerente
from datetime import datetime
from src.core.funcionario import Funcionario
from src.core.mixins_interfaces.funcionalidades_gerente import FuncionalidadesGerente
from decimal import Decimal
from src.utils.validacoes import validar_produto , validar_funcionario 

class Gerente(Funcionario,FuncionalidadesGerente):
    def __init__(self,nome,cpf,data_nascimento,salario_base, id: int,farmacia, senha: str):
        super().__init__(nome,cpf,data_nascimento,salario_base, id,farmacia, senha)

    def get_bonus(Self):
        pass

    def cadrastar_funcionario(self, nome : str , cpf : str, data_nasc : datetime , salario : Decimal):
        '''Cadrasta funcionario e retorna o objeto criado'''
        from random import randint
        senha = str(randint(10000, 99999))
        return self.getFarmacia()._registrarAtendente(self,nome,cpf,data_nasc,salario,senha)
    
    def excluir_funcionario(self,funcionario):
        '''Remove o funcionario desejado da lista de funcionarios'''
        # Implementaçao a ser discutida!!
        validar_funcionario(funcionario)
        lista = self.getfarmacia().getFuncionarios()
        if funcionario in lista:
            lista.remove(funcionario)
            return True
        return False

    def alterar_preco_produto(self, produto, preco: Decimal,): #precisei implementar para testar algumas coisas em produto
        '''Alterar preço de produto. Recebe preço em Decimal e objeto de Produto'''
        validar_produto(produto)
        produto.setPreco(self, preco)
        
    def __repr__(self):
        return f'Gerente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'


