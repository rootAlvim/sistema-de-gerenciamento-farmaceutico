from src.farmacia.farmacia import Farmacia

class Produto:
    def __init__(self, nome, preco, fabricante):
        self.__id = None
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante

    def getId(self):
        return self.__id
    
    def setIdUnico(self, farmacia: Farmacia):
        if not self.__id:
            self.__id = farmacia.getIdUnico(idParaProduto=True)
            return self.getId()
        raise ValueError("Id de Produto so pode ser alterado apenas uma vez")