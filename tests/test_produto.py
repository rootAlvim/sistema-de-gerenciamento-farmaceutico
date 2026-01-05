# teste de implementacoes 
# python -m tests.test_produto
from src.farmacia.produto import Produto

produto_teste = Produto('Amitril',2.90,'Cimed')
print(produto_teste.getId()) # teste de gerador de id

produto_teste2 = Produto('Amitril',2.90,'Cimed')
print(produto_teste2.getId()) # teste de gerador de id

print(50*'-')
print('PRODUTO-TESTE')
print(f'ID: {produto_teste.getId()}')
print(f'NOME: {produto_teste.nome}')
print(f'PREÇO: {produto_teste.getPreco()}')
print(f'FABRICANTE: {produto_teste.fabricante}')
print(50*'-')