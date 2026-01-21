# python -m tests.test_gerente
from datetime import datetime
from src.farmacia.farmacia import Farmacia
from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.farmacia.produto import Produto
from decimal import Decimal
from src.farmacia.estoque import Estoque
estoque = Estoque()
farmacia = Farmacia("Pague Menos")
p1 = Produto('Dipirona-25mg-Comprimido',2.00,'Cimed')
p2 = Produto('Dorflex-5mg-Comprimido',1.90,'Sanofi')
farmacia._registrarGerente("Chico",'122.222.222-23','1-1-1998',100, 'gerente123')
fun1 = farmacia.getGerente().cadrastar_funcionario("Alvim","123.123.123-23",'1-1-1998',890)
fun2 = farmacia.getGerente().cadrastar_funcionario("LULU","123.321.123-32",'9-2-1990',22)
print(fun1)

farmacia.getGerente().remover_produto(p1.getId())
# g.adicionar_produto_estoque(p1,12,estoque)
# g.adicionar_produto_estoque(p2,2,estoque)
# print(estoque.produto_disponibilidade(p2,11))
