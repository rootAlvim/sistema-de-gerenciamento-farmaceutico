from src.utils.validacoes import validar_produto

class Estoque:
    def __init__(self):
        self.__produtos = {}

    def get_produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto, quantidade: int):
        validar_produto(produto)
        p_id = produto.getId()
        if p_id in self.__produtos:
            self.__produtos[p_id]["quantidade"] += quantidade
        else:
            self.__produtos[p_id] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def remover_produto(self, produto): 
        '''Remove produto, passando como parametro o objeto produto'''
        validar_produto(produto)
        produtos_estoque = self.__produtos
        for id_produto , dados in produtos_estoque.items():
            if dados["produto"] == produto:
                del produtos_estoque[id_produto]
                return True
        return False       
     
    def consultar_produto_por_id(self, id_produto):
        if id_produto in self.__produtos:
            id = self.__produtos[id_produto]["produto"]
            quantidade = self.__produtos[id_produto]["quantidade"]
            return id.nome,quantidade #Tupla: (Nome,Quantidade)
        else:
            return False

    def consultar_produto_por_nome(self, nome):
        for registro in self.__produtos.values():
            produto = registro["produto"]
            quantidade = registro["quantidade"]

            if produto.nome == nome:
                return produto.nome,quantidade #Tupla: (Nome,Quantidade)
        
        return False

    def produto_disponibilidade(self, produto, quantidade):
        '''Checar se produto em quantidade passada está disponível para ser vendido. Retorna valor booleano.'''
        validar_produto(produto)
        produto_estoque = self.__produtos.get(produto.getId())
        if produto_estoque:
            if produto_estoque.get("quantidade") >= quantidade:
                return True
        return False


    
