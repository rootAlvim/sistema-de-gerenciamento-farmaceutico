'''
Funções auxiliares que não são entidades do negócio, por exemplo:
-Validação de CPF
-Formatação de datas
-Conversões
'''
import re 
def validar_formato_cpf(cpf: str):
    padrao = r"^\d{3}(\.?\d{3}){2}-?\d{2}$"
    if re.match(padrao, cpf):
        return cpf
    raise ValueError("Formato de CPF incorreto")

def validar_funcionario(funcionario):
    from src.core.funcionario import Funcionario
    if not isinstance(funcionario, Funcionario):
        raise TypeError('Método deve receber um objeto do tipo Funcionario (Gerente ou Atendente)')
    
def validar_cliente(cliente):
    from src.core.cliente import Cliente
    if not isinstance(cliente, Cliente):
        raise TypeError('Método deve receber um objeto do tipo Cliente')
    
def validar_produto(produto):
    from src.farmacia.produto import Produto
    if not isinstance(produto, Produto):
        raise TypeError('Método deve receber um objeto do tipo Produto')
    
def validar_gerente(gerente):
    from src.core.gerente import Gerente
    if not isinstance(gerente, Gerente):
        raise ValueError('Metodo deve receber um objeto do tipo Gerente')
    