# usar para tests: python -m tests.test_farmacia

from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto

farmacia = Farmacia("Pague mais")

farmacia.registrarGerente("Teste Gerente", '598.487.125-08', '02072004', 1899) # teste registro de gerente
print(farmacia.getGerente())

id_funcionario = farmacia.registrarAtendente("Teste Atendente", '64785412698', '01061999', 1550) # teste registro de Atendente
print(farmacia.getFuncionarioPorId(id_funcionario))

farmacia.registrarCliente("Teste Cliente", '142.648.139-26') # teste registro cliente
print(farmacia.getClientes())
print(farmacia.getClientePorCpf('142.648.139-26')) # teste pegar cliente por cpf

id_venda1 = farmacia.criarVenda(farmacia.getFuncionarioPorId(id_funcionario)) # teste criar Venda
print(farmacia.getListaVendas())

print(farmacia.getVendaPorId(id_venda1)) #teste pegar venda por id

produto1 = Produto("Teste Produto", 14.5, "Tester")
print(produto1.getId()) 

farmacia._estoque.adicionar_produto(produto1, 168) # teste adicionar produto
print(farmacia._estoque.get_produtos())

produto2 = Produto("Teste Produto 2", 19.5, "Tester2")
print(produto2.getId()) 

farmacia._estoque.adicionar_produto(produto2, 308) # teste adicionar produto 2
print(farmacia._estoque.get_produtos())
print('\n')
logs = farmacia.getLogAlteracoes()
for log in logs:
    print(log, end=2*'\n')
