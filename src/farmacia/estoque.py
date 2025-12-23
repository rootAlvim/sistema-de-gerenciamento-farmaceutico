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