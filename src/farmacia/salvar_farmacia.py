import pickle
import os

CAMINHO_ARQUIVO = "dados_farmacia.pkl"

def salvar_farmacia(farmacia):
    with open(CAMINHO_ARQUIVO, "wb") as arquivo:
        pickle.dump(farmacia, arquivo)

def carregar_farmacia():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return None

    with open(CAMINHO_ARQUIVO, "rb") as arquivo:
        return pickle.load(arquivo)
    
def excluir_farmacia():
    if os.path.exists(CAMINHO_ARQUIVO):
        os.remove(CAMINHO_ARQUIVO)
