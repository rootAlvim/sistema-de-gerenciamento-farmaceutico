from abc import ABC , abstractmethod
class Pessoa(ABC):
    def __init__(self,nome,cpf,data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
class Funcionario(Pessoa):
    def registrar_produto(self, estoque, produto, quantidade):
        estoque.adicionar_produto(produto, quantidade)

    def registrar_venda(self, estoque, produto, quantidade):
        return estoque.vender_produto(produto, quantidade)

    def consultar_estoque(self, estoque):
        return estoque.consultar()

class Produto:
    def __init__(self,id,nome,preco,fabricante):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante
        pass
class Estoque:
    def __init__(self):
        self.produtos = {}  # {Produto: quantidade}

    def adicionar_produto(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade

    def vender_produto(self, produto, quantidade):
        if produto in self.produtos and self.produtos[produto] >= quantidade:
            self.produtos[produto] -= quantidade
            return True
        return False

    def consultar(self):
        return {
            produto.nome: qtd for produto, qtd in self.produtos.items()
        }

    
estoque = Estoque()

tadala = Produto('p1', 'tadala', 10.0, 'cimed')
nebacetin = Produto('p2', 'nebacetin', 8.5, 'cimed')

funcionario = Funcionario('João', '12345678900', '1990-01-01')

funcionario.registrar_produto(estoque, tadala, 5)
funcionario.registrar_produto(estoque, nebacetin, 3)

print("Estoque inicial:", funcionario.consultar_estoque(estoque))

funcionario.registrar_venda(estoque, tadala, 2)

print("Estoque após venda:", funcionario.consultar_estoque(estoque))