from src.utils.validacoes import validar_produto

class Estoque:
    def __init__(self):
        self.__produtos = {}

    def get_produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto, quantidade: int):
        p_id = produto.getId()
        if p_id in self.__produtos:
            self.__produtos[p_id]["quantidade"] += quantidade
        else:
            self.__produtos[p_id] = {
                "produto": produto,
                "quantidade": quantidade
            }
    def remover_produto(self, id_produto, quantidade): 
        produtos_estoque = self.__produtos
        if id_produto in produtos_estoque:
            if produtos_estoque[id_produto]["quantidade"] >= quantidade:
                produtos_estoque[id_produto]["quantidade"] -= quantidade
                return True
            else:
                print('Quantidade insuficiente')
        else:
            print('Produto não encontrado.')
        return False       
     
    def consultar_produto_por_id(self, id_produto):
        if id_produto in self.__produtos:
            id = self.__produtos[id_produto]["produto"]
            quantidade = self.__produtos[id_produto]["quantidade"]
            #return f"ID: {id_produto} | Nome: {id.id} | Quantidade: {quantidade}"
            print(f'ID: {id.getId()} | Nome: {id.nome}| Quantidade: {quantidade} | Preço: {id.getPreco()} | Fabricante: {id.fabricante}')
        else:
            print(f'Produto com Id:[{id_produto}] Não encontrado')

    def consultar_produto_por_nome(self, nome):
        for registro in self.__produtos.values():
            produto = registro["produto"]
            quantidade = registro["quantidade"]

        if produto.nome == nome:
            #return f"Quantidade de {produto.getId()}: {quantidade:.2f}"
            print(f'ID: {produto.getId()} | Nome: {produto.nome}| Quantidade: {quantidade} | Preço: {produto.getPreco()} | Fabricante: {produto.fabricante}')
        else:
            print(f'Produto [{nome}] não encontrado')

    def produto_disponibilidade(self, produto, quantidade):
        '''Checar se produto em quantidade passada está disponível para ser vendido. Retorna valor booleano.'''
        validar_produto(produto)
        produto_estoque = self.__produtos.get(produto.getId())
        if produto_estoque:
            if produto_estoque.get("quantidade") >= quantidade:
                return True


    
