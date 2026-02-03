class GerenciarVendaMixin:
    def registrar_venda(self):
        '''Registra nova venda em farmacia. E adiciona Venda em lista de vendas do funcionario.'''
        return self.getFarmacia()._criarVenda(self)
    
    def adicionar_produto_venda(self, produto, quantidade):
        '''Adiciona produto em venda, ultima realizada por funcionario, caso produto esteja disponivel no estoque.'''
        estoque = self.getFarmacia().getEstoque()

        _quantidade = quantidade
        for itemVenda in self.getVendasRealizadas()[-1].getProdutos():
            if produto.getId() == itemVenda.id:
                _quantidade += itemVenda.quantidade 

        if not estoque.produto_disponibilidade(produto.getId(), _quantidade):
            raise ValueError("Produto em quantidade indisponível no estoque")
        
        self.getVendasRealizadas()[-1].adicionarProduto(self, produto, quantidade)
        # estoque.remover_produto(self, produto.getId(), quantidade)
        return True
        
    def remover_produto_venda(self, id_produto: int, quantidade: int = None):
        '''Recebe Id de produto e um inteiro para quantidade. Caso quantidade não seja passada, produto é removido por completo de venda.'''
        return self.getVendasRealizadas()[-1].removerProduto(self, id_produto, quantidade)

    def adicionar_cliente_venda(self, cliente):
        '''Adiciona cliente em ultima venda registrada pelo funcionario.'''
        self.getVendasRealizadas()[-1].adicionarCliente(self, cliente)

    def remover_venda(self, id_venda):
        '''Remove venda da lista de vendas de farmacia caso venda ainda não tenha sido finalizada. Recebe id da venda.'''
        self.getFarmacia()._removerVenda(self, id_venda)

    def finalizar_venda(self):
        '''Finaliza última venda realizada pelo funcionario. Checa se itens de venda estão disponíveis no estoque para dar baixa, caso não, retorna ValueError.'''
        estoque = self.getFarmacia().getEstoque()
        for itemVenda in self.getVendasRealizadas()[-1].getProdutos():
            if not estoque.produto_disponibilidade(itemVenda.id, itemVenda.quantidade):
                raise ValueError(f"Produto Id:{itemVenda.id} em quantidade indisponível no estoque")

        for itemVenda in self.getVendasRealizadas()[-1].getProdutos():
            estoque.remover_produto(self, itemVenda.id, itemVenda.quantidade)
            
        self.getVendasRealizadas()[-1].finalizarVenda(self)
        
