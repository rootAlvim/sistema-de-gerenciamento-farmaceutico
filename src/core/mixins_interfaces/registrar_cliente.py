class RegistrarClienteMixin:
    def registrar_cliente(self, farmacia, nome: str, cpf: str, data_nascimento = None):
        farmacia._registrarCliente(self, nome, cpf, data_nascimento)