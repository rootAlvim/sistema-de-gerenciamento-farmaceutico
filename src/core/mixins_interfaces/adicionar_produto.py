class AdicionarProdutoMixin:
    def adicionar_produto_estoque(self, produto, quantidade):
        """Adiciona qtd ao estoque chamando o metodo do obj Estoque"""
        self.getFarmacia()._estoque.adicionar_produto(self, produto, quantidade)
    