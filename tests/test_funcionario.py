# teste de implementacoes - python -m tests.test_funcionario
from datetime import datetime
from src.farmacia.farmacia import Farmacia
from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.farmacia.produto import Produto
from decimal import Decimal

farmacia = Farmacia("Pague mais")
# A = farmacia._registrarAtendente('a','130.654.134-43',datetime(2000, 8, 25), 1500.0)
# B = farmacia._registrarAtendente('b','130.654.134-43',datetime(2000, 8, 25), 1500.0)
# G = farmacia._registrarGerente('nick','123.122.345-67','1-1-1900',190)
# print(G.cadrastar_funcionario('Luciene','121.123.456-45','1-1-2020',1200))
'''print(farmacia.getFuncionarios())
G.excluir_funcionario(B)
print(farmacia.getFuncionarios())

# print(farmacia._registrarCliente('Alvim','130.654.134-43','1-1-1990'))
# print(farmacia._registrarCliente('Alvaro','130.654.134-43','1-1-1190'))
#print(farmacia.getLogAlteracoes())
id_funcionario1 = farmacia._registrarAtendente('teste', '055.678.501-08', datetime(2000, 8, 25), 1500.0)

id_venda = farmacia.getFuncionarioPorId(id_funcionario1).registrar_venda() # tetse de mixin
print(farmacia.getListaVendas())
print(farmacia.getFuncionarioPorId(id_funcionario1).getVendasRealizadas()) # verificacao se venda foi add em funcionario

produto1 = Produto("Teste Produto", 14.5, "Tester")
farmacia._estoque.adicionar_produto(produto1, 3) # teste adicionar produto, esse teste nao inclui gerenciamento de estoque via funcionario

print(farmacia.getFuncionarioPorId(id_funcionario1).adicionar_produto_venda(produto1, 1)) # teste de add produto em venda via mixin, deve retornar True caso tenha sido bem sucedida
print(farmacia._estoque.get_produtos())

cliente = Cliente('teste', '123.458.136-08', 12)
farmacia.getFuncionarioPorId(id_funcionario1).adicionar_cliente_venda(cliente)
print(farmacia.getVendaPorId(id_venda).getCliente())

print(farmacia.getVendaPorId(id_venda).getPrecoTotal())
farmacia.getFuncionarioPorId(id_funcionario1).finalizar_venda() # finalizando venda via mixin de funcionario
print(farmacia.getVendaPorId(id_venda).getPrecoTotal())'''

A = Atendente('a','123.123.345-43','1-1-1000',1,1,farmacia,'12')
print(A.consultar_estoque())