#implementacao de classe abstrata Funcionario
from datetime import datetime
from abc import abstractmethod
from src.core.pessoa import Pessoa
from src.core.mixins_interfaces.adicionar_produto import AdicionarProdutoMixin
from src.core.mixins_interfaces.gerenciar_venda import GerenciarVendaMixin
from src.core.mixins_interfaces.registrar_cliente import RegistrarClienteMixin

class Funcionario(Pessoa,AdicionarProdutoMixin,GerenciarVendaMixin,RegistrarClienteMixin):
    def __init__(self, nome:str, cpf:str, data_nascimento:datetime, salario_base:float, id:int,farmacia, senha:str):

        super().__init__(nome,cpf,data_nascimento)
        self.__salario_base = salario_base
        self.__id = id
        self.__senha = senha
        self.__farmacia = farmacia
        self.__autenticado = False 
        self.__vendasRealizadas = []
        
    
    @abstractmethod
    def get_bonus(Self): #implementei esse metodo para que de fato classe Funcionario fosse abstrata e não pudesse ser instanciada
        '''Retorna bonus salarial de acordo com o funcionario'''
        pass
    def getFarmacia(self):
        return self.__farmacia
    
    def get_salario_base(self):
        '''Retorna salario do funcionario'''
        return self.__salario_base
    
    def get_id(self):
        '''Retorna Id do funcionario'''
        return self.__id
    
    def get_isautenticado(self):
        '''Retorna True para autenticado False para não autenticado'''
        return self.__autenticado
    
    def getVendasRealizadas(self):
        return self.__vendasRealizadas
    
    def setAutenticacao(self, id:int, senha:str):
        '''Recebe Id e senha de Funcionario e verifica se são validos. Retorna true e altera atributo privado caso dados sejam verdadeiros.'''
        if not id == self.__id:
            raise ValueError("Id não correspondente")
        
        if not senha == self.__senha:
            raise ValueError("Senha não correspondente")
        
        self.__autenticado = True
        return True

    def desautenticar(self):
        '''Alterar atributo 'autenticado' para False.'''
        self.__autenticado = False

    def setNovaSenha(self, senhaAntiga:str, senhaNova:str):
        '''Altera senha de funcionario. Recebe confirmacao de senha antiga e uma nova senha, ambas strings.'''
        if not senhaAntiga == self.__senha:
            raise ValueError("Confirmação de senha não corresponde à senha antiga")
        
        if not len(senhaNova) >= 5:
            raise ValueError("Nova senha deve conter no mínimo 5 caracteres")
        
        self.__senha = senhaNova
        return True
    
    def setVendaRealizada(self, venda):
        '''Adiciona nova venda realizada a lista de vendas do funcionario.'''
        self.__vendasRealizadas.append(venda)
    
    def __str__(self):
        return f"ID {self.__id} | Nome: {self.nome} | Cargo: {self.__class__.__name__} | Salário: R$ {self.__salario_base:.2f}"
    
    def subTotal(self, estoque):
        produtos_estoque = estoque.get_produtos()
        total = 0
        for dados in produtos_estoque.values():
            produto = dados["produto"]
            quantidade = dados["quantidade"]
            subtotal = produto.getPreco() * quantidade
            total += subtotal
        return total #Retorna subtotal do estoque 
    
    def consultar_estoque(self,estoque):
        if not estoque.get_produtos():
            return False

        return {
        
            dados["produto"].nome: dados["quantidade"]
            for dados in estoque.get_produtos().values()
        } 
    
    def consultar_produto_por_id(self, id_produto,estoque):
        return estoque.consultar_produto_por_id(id_produto)

    def consultar_produto_por_nome(self, nome ,estoque):
        return estoque.consultar_produto_por_nome(nome)
    
    #def registrar_cliente(self,nome : str, cpf : str, data_nascimento = None):
         #self.__farmacia.registrarCliente(nome,cpf,data_nascimento)
