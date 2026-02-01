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

    def removerVendaRealizada(self, farmacia, venda):
        '''Método usado por farmacia. Recebe como parametros um objeto de farmacia e venda.'''
        self.__vendasRealizadas.remove(venda)

    def cadrastar_funcionario(self, tipo_funcionario : str,  nome : str , cpf : str, data_nasc : datetime, salario : Decimal):
        '''Recebe como um dos parametros se o método deve cadastrar um Atendente('atendente') ou Repositor('repositor'). Cadrasta funcionario e retorna o id do objeto criado'''
        from random import randint

        if tipo_funcionario == 'atendente':
            return self.getFarmacia()._registrarAtendente(self,nome,cpf,data_nasc,salario,cpf)
        elif tipo_funcionario == 'repositor':
            return self.getFarmacia()._registrarRepositor(self,nome,cpf,data_nasc,salario,cpf)
            
        raise ValueError("Parametro tipo_funcionario deve receber um dos dois valores: atendente ou repositor")
    
    def excluir_funcionario(self,funcionario):
        '''Recebe objeto de funcionário e o remove de Farmácia.'''
        validar_funcionario(funcionario)
        if funcionario in self.getFarmacia().getFuncionarios():
            self.getFarmacia().getFuncionarios().remove(funcionario)

            log =(
                f'excluir_funcionario()',
                f'Data:{datetime.now()}',
                f'{self.__str__()}'
                f'{funcionario.__str__()}'
            )
            self.getFarmacia().getLogAlteracoes(self).append(log)
            return True
        raise ValueError("Funcionário não existe em Farmácia.")

    def registrarCliente(self, nome : str, cpf : str, data_nascimento = None):
        '''Recebe atributos de cliente, registra um novo cliente em farmacia e retorna seu id'''
        return self.getFarmacia()._registrarCliente(self, nome, cpf, data_nascimento)

    def alterar_preco_produto(self, produto, preco: Decimal):
        '''Alterar preço de produto. Recebe preço em Decimal e objeto de Produto'''
        validar_produto(produto)
        if not produto.getId() in self.getFarmacia().getEstoque().get_produtos(self):
            raise ValueError("Produto não existe em estoque")
        
        produto.setPreco(self, preco)

    def consultar_log_alteracoes_farmacia(self):
        '''Retorna lista de tuplas sobre alterações em Farmácia.'''
        return self.getFarmacia().getLogAlteracoes(self)
    
    def consultar_chamados(self):
        '''Retorna lista de chamados em Farmácia.'''
        return self.getFarmacia().getChamados(self)
    
    def alterar_status_chamado(self, id: int, status: str):
        '''Recebe o id do chamado e um status (Aberto, Em processo ou Finalizado). Altera o status de um chamado em Farmácia.'''
        self.getFarmacia().setChamadoStatus(self, int(id), status)
        
    def __repr__(self):
        return f'Gerente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'


