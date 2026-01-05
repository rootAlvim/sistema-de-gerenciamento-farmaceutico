from random import randint

def getIdProduto(obj, maxIds = 1000):
    '''Recebe um objeto que tenha o atributo de classe 'allIds' do tipo list implementado. Parametro de geracoes de Id, 'maxIds', por padrao esta em 1000. Retorna um Id unico e erro caso o numero maximo de Id seja alcancado.'''
    id = randint(1, maxIds)
    counter = 0
    while id in obj.allIds:
        if counter > maxIds:
            raise ValueError("Numero maximo de ID alcancado")
        id = randint(1, maxIds)
        counter += 1
    obj.allIds.append(id)
    return id