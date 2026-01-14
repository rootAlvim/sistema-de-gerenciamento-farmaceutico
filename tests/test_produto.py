# teste de implementacoes 
# python -m tests.test_produto
from src.farmacia.produto import Produto
from src.farmacia.farmacia import Farmacia

farmacia = Farmacia("Pague mais")

farmacia._registrarGerente("Teste Gerente", '598.487.125-08', '02072004', 1899)

produto_teste = Produto('Amitril',2.90,'Cimed')
print(produto_teste.getPreco()) # teste de gerador de id

farmacia.getGerente().alterar_preco_produto(produto_teste, 2.85)
print(produto_teste.getPreco())
print(produto_teste.getLogAlteracoes())

produto_teste2 = Produto('Amitril',2.90,'Cimed')
print(produto_teste2.getId()) # teste de gerador de id

print(50*'-')
print('PRODUTO-TESTE')
print(f'ID: {produto_teste.getId()}')
print(f'NOME: {produto_teste.nome}')
print(f'PREÇO: {produto_teste.getPreco()}')
print(f'FABRICANTE: {produto_teste.fabricante}')
print(50*'-')