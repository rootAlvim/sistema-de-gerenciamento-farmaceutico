#python -m src.main
import os
import time
from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.core.funcionario import Funcionario
from src.core.gerente import Gerente
from src.core.pessoa import Pessoa
from src.core.mixins_interfaces import *
from src.farmacia.farmacia import Farmacia
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
from src.farmacia.venda import Venda
farmacia = Farmacia('Farmacia Holanda')
estoque = farmacia._estoque
gerente = farmacia._registrarGerente('Carlos','13032112390','1-1-8909',1200,123)
def limpar_tela():
    """Função auxiliar para limpar o console e deixar o menu bonito."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_medicamento():
    print("\n--- CADASTRAR NOVO MEDICAMENTO ---")
    nome = input("Nome: ")
    preco = input("Preço: ")
    fabricante = input("Fabricante: ")
    qntd = input("Quantidade: ")
    p1 = Produto(nome,preco,fabricante)
    gerente.adicionar_produto_estoque(p1,qntd)
    print(p1.getId())
    input("\nPressione Enter para voltar ao menu...")

def listar_medicamentos():
    limpar_tela()
    print("\n--- ESTOQUE DE MEDICAMENTOS ---")
    print(gerente.consultar_estoque())
    input("\nPressione Enter para voltar ao menu...")

def buscar_id():
    limpar_tela()
    id = input("Digite o Id do Produto: ")

    print(gerente.consultar_produto_por_id(id))
    input("\nPressione Enter para voltar ao menu...")
def menu():
    """Exibe as opções para o usuário."""
    limpar_tela()
    print("="*30)
    print(" SISTEMA DE FARMÁCIA v1.0 ")
    print("="*30)
    print("[1] - Cadastrar Medicamento")
    print("[2] - Listar Estoque")
    print("[3] - Buscar Medicamento por Id")
    print("[4] - Realizar Venda")
    print("[0] - Sair")
    print("="*30)

def main():
    """Função Principal (Gerente do Programa)"""
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_medicamento()
        elif opcao == '2':
            listar_medicamentos()
        elif opcao == '3':
            buscar_id()
            pass
        elif opcao == '4':
            #realizar_venda()
            pass
        elif opcao == '0':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida!")
            time.sleep(1) # Espera 1 segundo para o usuário ler o erro

# --- PONTO DE ENTRADA ---
# Isso garante que a main só rode se executarmos este arquivo diretamente
if __name__ == "__main__":
    main()