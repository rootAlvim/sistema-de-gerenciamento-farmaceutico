# teste de implementacoes - python -m tests.test_venda
from datetime import datetime
from src.farmacia.farmacia import Farmacia
from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.farmacia.produto import Produto
from decimal import Decimal
p1 = Produto('Dipirona-25mg-Comprimido',2.30,'Cimed')
p2 = Produto('Dorflex-5mg-Comprimido',1.90,'Sanofi')
farmacia = Farmacia("Farmácia Popular")
atendente = farmacia._registrarAtendente('Jose','123.123.123-23','1-1-1990',900)
venda = farmacia._criarVenda(atendente)
venda.adicionarProduto(p1, 10)
venda.adicionarProduto(p2, 1)
cliente = farmacia._registrarCliente(atendente, "João", "123.456.789-00")
venda.adicionarCliente(cliente)
venda.finalizarVenda()

atendente2 = farmacia._registrarAtendente('Joaasse','123.123.123-23','1-1-1990',9200)
venda2 = farmacia._criarVenda(atendente2)
cliente2 = farmacia._registrarCliente(atendente2, "Carlos", "222.111.111-11")
venda2.adicionarCliente(cliente2)
venda2.adicionarProduto(p2, 1)
venda2.finalizarVenda()

print(farmacia.getListaVendas())
print(venda.getLogAlteracoes())
'''farm = Farmacia("Pague mais")
id_funcionario1 = farm._registrarAtendente('teste', '055.678.501-08', datetime(2000, 8, 25), 1500.0)

#teste de id automatico
print(farm.getListaVendas())
id_venda1 = farm._criarVenda(farm.getFuncionarioPorId(id_funcionario1))
# print(farm.getListaVendas()[0].getId())
# farm.criarVenda(atendente)
# print(farm.getListaVendas()[1].getId())
# farm.criarVenda(atendente)
# print(farm.getListaVendas()[2].getId())

produto_teste = Produto('Amitril',2.90,'Cimed')
produto_teste2 = Produto('Cesol',8.25,'Farmacol')

farm.getVendaPorId(id_venda1).adicionarProduto(produto_teste, 1)

print(farm.getVendaPorId(id_venda1).getProdutos())

farm.getVendaPorId(id_venda1).adicionarProduto(produto_teste, 1)
print(farm.getVendaPorId(id_venda1).getProdutos())

farm.getVendaPorId(id_venda1).adicionarProduto(produto_teste2, 2)
print(farm.getVendaPorId(id_venda1).getProdutos())

cliente = Cliente('teste', '123.458.136-08', 12)
farm.getVendaPorId(id_venda1).adicionarCliente(farm.getFuncionarioPorId(id_funcionario1), cliente)
print(farm.getVendaPorId(id_venda1).getCliente())
print(cliente.getCompras())
print(farm.getVendaPorId(id_venda1).getLogAlteracoes())

print(farm.getVendaPorId(id_venda1).getPrecoTotal()) 
farm.getVendaPorId(id_venda1).setPrecoTotal(farm.getFuncionarioPorId(id_funcionario1)) # finalizando venda
print(farm.getVendaPorId(id_venda1).getPrecoTotal()) 

# farm.getListaVendas()[0].adicionarProduto(produto_teste2, 2) # testando erro de tentar adicionar produto com venda finalizada

# farm.getListaVendas()[0].adicionarCliente(atendente,Cliente('teste', '123.458.136-08', 12)) # testando add cliente apos venda finalizada
print('\n')
logs = farm.getVendaPorId(id_venda1).getLogAlteracoes() # testando logs
for log in logs:
    print(log, end=2*'\n')'''