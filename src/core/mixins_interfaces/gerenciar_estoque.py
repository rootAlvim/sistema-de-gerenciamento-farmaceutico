class GerenciarEstoqueMixin:
    def adicionar_produto_estoque(self,produto , quantidade):
        """Adiciona qtd ao estoque chamando o metodo do obj Estoque"""
        estoque = self.getFarmacia()
        estoque._estoque.adicionar_produto(self, produto, quantidade)
        
    def remover_produto(self, id, quantidade = None):
       '''Recebe um inteiro do Id de Produto e, remove ou reduz sua quantidade do estoque, caso parametro 'quantidade' tenha um valor inteiro positivo.'''
       estoque = self.getFarmacia()
       estoque.remover_produto(self, id, quantidade)
            
    def consultar_estoque(self):
        '''Retorna um dicionario contendo todos os produtos e suas quantidades em estoque.'''
        estoque = self.getFarmacia()._estoque

        return {
        
            dados["produto"]: dados["quantidade"]
            for dados in estoque.get_produtos(self).values()
        }
    
    def consultar_produto_por_id(self, id_produto):
        '''Recebe id do produto e retorna seu objeto e quantidade em estoque.'''
        estoque = self.getFarmacia()._estoque
        return estoque.consultar_produto_por_id(self, id_produto)

    def consultar_produto_por_nome(self, nome ):
        '''Recebe nome do produto e retorna seu objeto e quantidade em estoque.'''
        estoque = self.getFarmacia()._estoque
        return estoque.consultar_produto_por_nome(self, nome)