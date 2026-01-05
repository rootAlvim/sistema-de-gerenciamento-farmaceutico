# usar para tests: python -m tests.test_farmacia

from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto

farmacia = Farmacia("Pague mais")

farmacia.registrarGerente("Teste Gerente", '598.487.125-08', '02072004', 1899) # teste registro de gerente
print(farmacia.gerente.get_id())

farmacia.registrarAtendente("Teste Atendente", '64785412698', '01061999', 1550) # teste registro de Atendente
print(farmacia.funcionarios[0].get_id())

farmacia.criarVenda(farmacia.funcionarios[0]) # teste criar Venda
print(farmacia.getListaVendas()[0].getId())

produto1 = Produto("Teste Produto", 14.5, "Tester")
print(produto1.getId()) 

farmacia._estoque.adicionar_produto(produto1, 168) # teste adicionar produto
print(farmacia._estoque.get_produtos())

produto2 = Produto("Teste Produto 2", 19.5, "Tester2")
print(produto2.getId()) 

farmacia._estoque.adicionar_produto(produto2, 308) # teste adicionar produto 2
print(farmacia._estoque.get_produtos())
