class Vender_ProdutoMixin:
    def vender_produto(self, id_produto, quantidade, estoque_obj):
        """Realiza a baixa no estoque chamando o metodo do obj estoque"""
        estoque_obj.remover_produto(id_produto, quantidade)
