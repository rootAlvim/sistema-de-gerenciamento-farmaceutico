# teste de implementacoes
# python -m tests.test_estoque
from src.core.funcionario import Funcionario
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
estoque = Estoque() 
funcionario = Funcionario('João', '12345678900', '1990-01-01','1200',1)
p1 = Produto(1,'Dipirona-25mg-Comprimido',2.30,'Cimed')
p2 = Produto(2,'Dorflex-5mg-Comprimido',1.90,'Sanofi')
print(50*'-')
print('INFORMAÇÕES GERAIS DO FUNCIONARIO')
print(f'NOME: {funcionario.nome}')
print(f'CPF: {funcionario.get_cpf()}')
print(f'NASCIMENTO: {funcionario.get_data_nascimento()}')
print(f'SALÁRIO: {funcionario.get_salario_base()}')
print(f'ID: {funcionario.get_id()}')
print(50*'-')
print('TESTANDO METODOS DE FUNCIONARIO')
funcionario.adicionar_produto(p1,12,estoque)
funcionario.adicionar_produto(p2,24,estoque)
print(f'Estoque Antes da venda: {funcionario.consultar(estoque)}')
funcionario.vender_produto(1,2,estoque)
funcionario.vender_produto(2,4,estoque)
print(f'Estoque Depois da venda: {funcionario.consultar(estoque)}')