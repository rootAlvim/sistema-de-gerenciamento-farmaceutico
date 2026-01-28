from src.utils.validacoes import validar_produto
from src.utils.validacoes import validar_funcionario

class Estoque:
    def __init__(self):
        self.__produtos = {}

    def get_produtos(self, funcionario):
        '''Recebe um objeto de funcionario para validação e retorna um dicionario contendo produtos e suas quantidades.'''
        validar_funcionario(funcionario) # adicionei funcionario para servir de controle, e forçar que apenas via funcionario seja possivel consultar estoque
        return self.__produtos

    def adicionar_produto(self, funcionario, produto, quantidade: int):
        '''Recebe um objeto de funcionario para validação, um objeto de produto e sua quantidade. Adiciona novo objeto em estoque ou se caso já existir em estoque, apenas aumenta quantidade em estoque.'''
        validar_funcionario(funcionario) # adicionei funcionario para servir de controle, e forçar que apenas via funcionario seja possivel adicionar em estoque
        validar_produto(produto)
        p_id = produto.getId()
        if p_id in self.__produtos:
            self.__produtos[p_id]["quantidade"] += quantidade
        else:
            self.__produtos[p_id] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def remover_produto(self, funcionario, id, quantidade = None):
        '''Recebe um objeto de funcionario para validação, um inteiro do Id de Produto e, remove ou reduz sua quantidade do estoque, caso parametro 'quantidade' tenha um valor inteiro positivo.'''
        validar_funcionario(funcionario) # adicionei funcionario para servir de controle, e forçar que apenas via funcionario seja possivel remover em estoque

        produtos_estoque = self.__produtos
        for id_produto in produtos_estoque.keys():
            if id_produto == id:
                if quantidade and quantidade > 0:
                    if self.produto_disponibilidade(id, quantidade): #dupla verificacao, reutilizando metodo, pra caso seja um valor positivo, porem acima de permitido.
                        produtos_estoque[id]["quantidade"] -= quantidade
                        return True
                    raise ValueError("Produto em quantidade indisponível.")
                
                del produtos_estoque[id]
                return True    
     
    def consultar_produto_por_id(self, funcionario, id_produto):
        '''Recebe um objeto de funcionario para validação, id do produto e caso produto exista, retorna o seu objeto e quantidade em estoque.'''
        validar_funcionario(funcionario) # adicionei funcionario para servir de controle, e forçar que apenas via funcionario seja possivel consultar estoque

        if id_produto in self.__produtos:
            id = self.__produtos[id_produto]["produto"]
            quantidade = self.__produtos[id_produto]["quantidade"]
            return id,quantidade #Tupla: (Nome,Quantidade) mudei para (Obj, quantidade)
        # else: else fica redundante
        #     return False

    def consultar_produto_por_nome(self, funcionario, nome):
        '''Recebe um objeto de funcionario para validação, nome do produto e caso produto exista, retorna o seu objeto e quantidade em estoque.'''
        validar_funcionario(funcionario) # adicionei funcionario para servir de controle, e forçar que apenas via funcionario seja possivel consultar estoque

        for registro in self.__produtos.values():
            produto = registro["produto"]
            quantidade = registro["quantidade"]

            if str(produto.nome).lower() == str(nome).lower():
                return produto,quantidade #Tupla: (Nome,Quantidade) mudei para (Obj, quantidade)
        
        # return False fica redundante

    def produto_disponibilidade(self, id_produto, quantidade):
        '''Recebe Id de produto e sua quantidade. Checa se produto em quantidade passada está disponível para ser vendido. Retorna valor booleano.'''
        produto_estoque = self.__produtos.get(id_produto)
        if produto_estoque:
            if produto_estoque.get("quantidade") >= quantidade:
                return True
        # return False fica redundante


    
