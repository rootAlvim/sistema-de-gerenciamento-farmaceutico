class GerenciarVendaMixin:
    def registrar_venda(self, farmacia):
        '''Registra nova venda em farmacia. Retorna o Id da venda.'''
        id = farmacia._criarVenda(self)
        return id
    
    def adicionar_produto_venda(self, farmacia, produto, quantidade):
        '''Adiciona produto em venda, ultima realizada por funcionario, caso produto esteja disponivel no estoque.'''
        estoque = farmacia._estoque
        if estoque.produto_disponibilidade(produto, quantidade):
            self.getVendasRealizadas()[-1].adicionarProduto(produto, quantidade)
            estoque.remover_produto(produto.getId(), quantidade)
            return True

    def adicionar_cliente_venda(self, cliente):
        '''Adiciona cliente em ultima venda registrada pelo funcionario.'''
        self.getVendasRealizadas()[-1].adicionarCliente(self, cliente)

    def finalizar_venda(self):
        '''Finaliza ultima venda realizada pelo funcionario.'''
        self.getVendasRealizadas()[-1].setPrecoTotal(self)
        
