class Adicionar_ProdutoMixin:
    def adicionar_produto_estoque(self, produto, quantidade, estoque_obj):
        """Adiciona qtd ao estoque chamando o metodo do obj Estoque"""
        estoque_obj.adicionar_produto(produto, quantidade)
        print(f"[{self.cargo}] Adicionado {quantidade}x {produto.nome}")
    