# teste de implementacoes 
# python -m tests.test_produto
from src.farmacia.produto import Produto
produto_teste = Produto(1,'Amitril',2.90,'Cimed')
print(50*'-')
print('PRODUTO-TESTE')
print(f'ID: {produto_teste.id}')
print(f'NOME: {produto_teste.nome}')
print(f'PREÇO: {produto_teste.preco}')
print(f'FABRICANTE: {produto_teste.fabricante}')
print(50*'-')