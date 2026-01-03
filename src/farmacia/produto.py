class Produto:
    def __init__(self, nome, preco, fabricante):
        self.__id = None
        self.nome = nome
        self.__preco = preco
        self.fabricante = fabricante
        self.__logAlteracoes = []

    def getId(self):
        return self.__id
    
    def getPreco(self):
        return self.__preco
    
    def setIdUnico(self, farmacia):
        from src.farmacia.farmacia import Farmacia
        if not isinstance(farmacia, Farmacia):
            raise ValueError("Parametro farmacia deve ser uma instacia do tipo Farmacia")
        
        if not self.__id:
            self.__id = farmacia.getIdUnico(idParaProduto=True)
            return self.getId()
        raise ValueError("Id de Produto so pode ser alterado apenas uma vez")
    
    def __repr__(self):
        return f'Produto({self.nome}, {self.__preco}, {self.fabricante})'