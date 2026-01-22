#implementacao de classe Gerente
from datetime import datetime
from src.core.funcionario import Funcionario
from src.core.mixins_interfaces.funcionalidades_gerente import FuncionalidadesGerente
from decimal import Decimal
from src.utils.validacoes import validar_produto , validar_funcionario 
from src.core.mixins_interfaces.gerenciar_estoque import GerenciarEstoqueMixin
from src.core.mixins_interfaces.gerenciar_venda import GerenciarVendaMixin
class Gerente(Funcionario,FuncionalidadesGerente,GerenciarEstoqueMixin,GerenciarVendaMixin):
    def __init__(self,nome,cpf,data_nascimento,salario_base, id: int,farmacia, senha: str):
        super().__init__(nome,cpf,data_nascimento,salario_base, id,farmacia, senha)
        self.__porcentagemBonusGerente = 0.1
        self.__vendasRealizadas = []

    def get_bonus(self):
        '''Recebe bonus de 10% do salario base acrescentado ao bonus base de funcionario.'''
        calculo = super().get_bonus() + (self.get_salario_base() * Decimal(self.__porcentagemBonusGerente))
        return calculo.quantize(Decimal('0.01'))
    
    def getVendasRealizadas(self):
        '''Retorna lista de vendas realizadas'''
        return self.__vendasRealizadas
    
    def setVendaRealizada(self, venda):
        '''Adiciona nova venda realizada a lista de vendas do funcionario.'''
        self.__vendasRealizadas.append(venda)

    def cadrastar_funcionario(self, nome : str , cpf : str, data_nasc : datetime , salario : Decimal):
        '''Cadrasta funcionario e retorna o objeto criado'''
        from random import randint
        senha = str(randint(10000, 99999))
        return self.getFarmacia()._registrarAtendente(self,nome,cpf,data_nasc,salario,senha)
    
    def excluir_funcionario(self,funcionario):
        '''Remove o funcionario desejado da lista de funcionarios'''
        # Implementaçao a ser discutida!!
        validar_funcionario(funcionario) #Valida se foi passado um objeto funcionario
        lista = self.getfarmacia().getFuncionarios()
        if funcionario in lista:
            lista.remove(funcionario)
            return True
        return False

    def registrarCliente(self, nome : str, cpf : str, data_nascimento = None):
        '''Recebe atributos de cliente, registra um novo cliente em farmacia e retorna seu id'''
        return self.getFarmacia()._registrarCliente(self, nome, cpf, data_nascimento)

    def alterar_preco_produto(self, produto, preco: Decimal): #precisei implementar para testar algumas coisas em produto
        '''Alterar preço de produto. Recebe preço em Decimal e objeto de Produto'''
        validar_produto(produto) #Valida se foi passado um objeto funcionario
        produto.setPreco(self, preco)
        
    def __repr__(self):
        return f'Gerente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'


