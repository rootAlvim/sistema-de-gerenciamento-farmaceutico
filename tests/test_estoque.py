# teste de implementacoes

from src.core.funcionario import Funcionario
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto

estoque = Estoque()

tadala = Produto('p1', 'tadala', 10.0, 'cimed')
nebacetin = Produto('p2', 'nebacetin', 8.5, 'cimed')

funcionario = Funcionario('João', '12345678900', '1990-01-01')

funcionario.registrar_produto(estoque, tadala, 5)
funcionario.registrar_produto(estoque, nebacetin, 3)

print("Estoque inicial:", funcionario.consultar_estoque(estoque))

funcionario.registrar_venda(estoque, tadala, 2)

print("Estoque após venda:", funcionario.consultar_estoque(estoque))