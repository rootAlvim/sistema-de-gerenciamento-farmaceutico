class RegistrarClienteMixin:
    def registrar_cliente(self, nome: str, cpf: str, data_nascimento = None):
        self.__farmacia._registrarCliente(self, nome, cpf, data_nascimento)