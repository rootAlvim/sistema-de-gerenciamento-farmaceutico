# usar para tests: python -m tests.test_farmacia
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto

farmacia = Farmacia("Pague mais")

farmacia._registrarGerente("Teste Gerente", '598.487.125-08', '02072004', 1899) # teste registro de gerente
print(farmacia.getGerente())

id_funcionario = farmacia._registrarAtendente("Teste Atendente", '64785412698', '01061999', 1550) # teste registro de Atendente
print(farmacia.getFuncionarioPorId(id_funcionario))

farmacia.getFuncionarioPorId(id_funcionario).registrar_cliente(farmacia, "Teste Cliente", '142.648.139-26') # teste registro cliente 

print(farmacia.getClientes())
print(farmacia.getClientePorCpf('142.648.139-26')) # teste pegar cliente por cpf

id_venda1 = farmacia._criarVenda(farmacia.getFuncionarioPorId(id_funcionario)) # teste criar Venda
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





# funcionario =  farmacia._registrarAtendente('Alvim','130.654.134-42','28-07-2006',900) #Registra Atendente
# gerente = farmacia._registrarGerente('Nikolas','890.987.098-21','17-09-2000',890) #Registra Gerente
# cliente = farmacia._registrarCliente(funcionario,'Lucia','123.123.234-45') #Registra Cliente
# p1 = Produto('Dipirona-25mg-Comprimido',2.30,'Cimed')
# p2 = Produto('Dorflex-5mg-Comprimido',1.90,'Sanofi')
# #venda_teste = farmacia._criarVenda(gerente)
# venda_teste = gerente.registrar_venda(farmacia)
# venda_teste.adicionarCliente(cliente)
# venda_teste.adicionarProduto(p1,12)
# venda_teste.finalizarVenda()
# print(venda_teste.getCliente()) #Cliente da venda
# print(venda_teste.getFuncionario())#Funcionario da venda
# print(venda_teste.getId()) #Id da venda
# print(venda_teste.getProdutos()) #Produtos vendidos
# print(venda_teste.getPrecoTotal()) #preco total da venda
# #Testando gets e sets
# print(50*'=')
# print(f'Gerente: {farmacia.getGerente()}')
# print(f'Funcionarios: {farmacia.getFuncionarios()}')
# print(f'Funcionario por id {farmacia.getFuncionarioPorId(funcionario.get_id())}')
# print(farmacia.getListaVendas())
# #print(farmacia.getVendaPorId(venda.id))
# print(f'Clientes: {farmacia.getClientes()}')
# print(f'Cliente por cpf: {farmacia.getClientePorCpf(cliente.get_cpf())}')
# #print(f'Log de alteracoes: {farmacia.getLogAlteracoes()}')
# print(50*'=')
