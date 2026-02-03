class GerenciarEstoqueMixin:
    def adicionar_produto_estoque(self,produto , quantidade):
        """Adiciona qtd ao estoque chamando o metodo do obj Estoque"""
        self.getFarmacia().getEstoque().adicionar_produto(self, produto, quantidade)
        
    def remover_produto(self, id, quantidade = None):
       '''Recebe um inteiro do Id de Produto e, remove ou reduz sua quantidade do estoque, caso parametro 'quantidade' tenha um valor inteiro positivo.'''
       self.getFarmacia().getEstoque().remover_produto(self, id, quantidade)
            
    def consultar_estoque(self):
        '''Retorna um dicionario contendo todos os produtos e suas quantidades em estoque.'''
        estoque = self.getFarmacia().getEstoque()

        return {
        #Para cada dados do estoque pegue o produto e  quantidadee e coloque isso em um novo dicionáio
            dados["produto"]: dados["quantidade"]
            for dados in estoque.get_produtos(self).values()
        }
    
    def consultar_produto_por_id(self, id_produto):
        '''Recebe id do produto e retorna seu objeto e quantidade em estoque.'''
        estoque = self.getFarmacia().getEstoque()
        return estoque.consultar_produto_por_id(self, id_produto)

    def consultar_produto_por_nome(self, nome ):
        '''Recebe nome do produto e retorna seu objeto e quantidade em estoque.'''
        estoque = self.getFarmacia().getEstoque()
        return estoque.consultar_produto_por_nome(self, nome)
    
    def subTotal_estoque(self):
        '''Retorna o subtotal do estoque.'''
        from decimal import Decimal
        
        produtos_estoque = self.getFarmacia().getEstoque().get_produtos(self)
        total = 0
        for dados in produtos_estoque.values():
            produto = dados["produto"]
            quantidade = dados["quantidade"]
            subtotal = produto.getPreco() * Decimal(quantidade)
            total += subtotal
            
        return total