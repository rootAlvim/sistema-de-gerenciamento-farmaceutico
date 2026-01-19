class GerenciarVendaMixin:
    def registrar_venda(self):
        '''Registra nova venda em farmacia. E adiciona Venda em lista de vendas do funcionario.'''
        return self.getFarmacia()._criarVenda(self)
    
    def adicionar_produto_venda(self, produto, quantidade):
        '''Adiciona produto em venda, ultima realizada por funcionario, caso produto esteja disponivel no estoque.'''
        estoque = self.getFarmacia()._estoque
        if estoque.produto_disponibilidade(produto, quantidade):
            self.getVendasRealizadas()[-1].adicionarProduto(produto, quantidade)
            estoque.remover_produto(self, produto.getId(), quantidade)
            return True
        raise ValueError("Produto indisponível no estoque")

    def adicionar_cliente_venda(self, cliente):
        '''Adiciona cliente em ultima venda registrada pelo funcionario.'''
        self.getVendasRealizadas()[-1].adicionarCliente(cliente)

    def finalizar_venda(self):
        '''Finaliza ultima venda realizada pelo funcionario.'''
        self.getVendasRealizadas()[-1].finalizarVenda()
        
