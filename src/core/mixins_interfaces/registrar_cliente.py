class RegistrarClienteMixin:
    def registrar_cliente(self, nome: str, cpf: str, data_nascimento = None):
        self.getFarmacia()._registrarCliente(self, nome, cpf, data_nascimento)