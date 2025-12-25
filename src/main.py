'''
-Ponto de entrada do sistema:
-Menu inicial
-Simulação de uso
-Chamadas principais
'''

from farmacia.estoque import Estoque 
from farmacia.produto import Produto 
from core.funcionario import Funcionario
funcionario = Funcionario('João', '12345678900', '1990-01-01','1200','1')
estoque = Estoque()
while True:
        print("\n1 - Registrar produto")
        print("2 - Registrar venda")
        print("3 - Consultar estoque")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input('Nome do produto: ')
            id = input("ID do produto: ")
            preco = input('Preço do produto: ')
            fabricante = input('Fabricante do produto: ')
            qtd = int(input("Quantidade: "))
            p = Produto(id,nome,preco,fabricante)
            funcionario.registrar_produto(estoque,p,qtd)

        elif opcao == "2":
            
            if p is not None:
                nome = input('Digite o nome do produto: ')
                qtd = int(input("Quantidade: "))
                funcionario.registrar_venda(estoque, p , qtd)
            else:
                print('Não ha estoque')
            
        
        elif opcao == "3":
            print(funcionario.consultar_estoque(estoque))
            break    