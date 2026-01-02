# usar para tests: python -m tests.test_farmacia

from src.farmacia.farmacia import Farmacia
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto

produ1 = Produto('teste', 12.5, 'tester')
produ2 = Produto('teste', 12.5, 'tester')

farm = Farmacia("Pague mais")

# nao funciona, precisa finalizar estoque e atualizar os testes
farm._estoque = Estoque()
farm._estoque.produtos = [(produ1, 156), (produ2, 68)]

#testes de atribuicao de id unico
print(produ1.setIdUnico(farm))
print(produ2.setIdUnico(farm))

print(farm.getIdUnico(idParaProduto=True))