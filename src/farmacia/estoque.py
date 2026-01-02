class Estoque:
    def __init__(self):
        self.__produtos = [] # possivel mudanca, ao inves de um dicionario, uma lista com tuplas, ex.: [(produto1, 123), (produto2, 189)]

    def get_produtos(self):
        return self.__produtos
