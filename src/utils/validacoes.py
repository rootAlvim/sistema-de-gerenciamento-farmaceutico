'''
Funções auxiliares que não são entidades do negócio, por exemplo:
-Validação de CPF
-Formatação de datas
-Conversões
'''
import re 
def validar_formato_cpf(cpf: str):
    padrao = r"^\d{3}(\.?\d{3}){2}-?\d{2}$"
    if re.match(padrao, cpf):
        return True
    return False