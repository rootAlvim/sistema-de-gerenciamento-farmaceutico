'''
-Ponto de entrada do sistema:
-Menu inicial
-Simulação de uso
-Chamadas principais
'''

from farmacia.estoque import Estoque 
from farmacia.produto import Produto 
from core.funcionario import Funcionario
estoque = Estoque()
print('___')
tadala = Produto('p1', 'tadala', 10.0, 'cimed')
nebacetin = Produto('p2', 'nebacetin', 8.5, 'cimed')
dipirona = Produto('p3','dipirona',2.3,'aveloz')
funcionario = Funcionario('João', '12345678900', '1990-01-01','1200','1')

funcionario.registrar_produto(estoque, tadala, 5)
funcionario.registrar_produto(estoque, nebacetin, 3)
funcionario.registrar_produto(estoque,dipirona,10)
print("Estoque inicial:", funcionario.consultar_estoque(estoque))

funcionario.registrar_venda(estoque, tadala, 5)
funcionario.registrar_venda(estoque,dipirona,3)
print("Estoque após venda:", funcionario.consultar_estoque(estoque))