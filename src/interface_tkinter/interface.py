from tkinter import *
from src.farmacia.farmacia import Farmacia
from decimal import Decimal

class Interface:
    def __init__(self):
        self.root = None
        self.farmacia = None

    def __botaoRegistrar(self, texto, funcao):
        botao_registrar = Button(
            self.root, 
            text=texto, 
            padx=10, 
            pady=10, 
            command=funcao)
        return botao_registrar

    def registrarFarmacia(self):
        from src.farmacia.farmacia import Farmacia
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Farmácia')
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=0, columnspan=2)

        def instanciar():
            nome = campo_nome.get()
            if nome:
                self.farmacia = Farmacia(nome)
                campo_nome.delete(0, END)
                self.root.destroy()

        self.__botaoRegistrar('Registrar Farmácia', instanciar).grid(row=1, column=0)

        self.root.mainloop()

    def registrarAtendente(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Atendente')

        if not self.farmacia:
            msg = Message(self.root, text='Farmacia não registrada!')
            msg.grid(row=0, column=0)
            self.root.after(3000, self.root.destroy)
            return 

        Label(self.root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.root, text="Cpf:").grid(row=1)
        campo_cpf = Entry(self.root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get()
            cpf = campo_cpf.get()
            data_nascimento = campo_dataNasc.get()
            salario = Decimal(campo_salario.get())

            try:
                self.farmacia._registrarAtendente(nome, cpf, data_nascimento, salario)
            except Exception as erro:
                msg = Message(self.root, text=f'{erro}')
                msg.grid(row=0, column=0)
                self.root.after(3000, self.root.destroy)
                return 
            
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.root.destroy()

        self.__botaoRegistrar('Registrar Atendente', instanciar).grid(row=4, column=1)

        self.root.mainloop()

    def registrarGerente(self):
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('Registrar Gerente')

        if not self.farmacia:
            msg = Message(self.root, text='Farmacia não registrada!')
            msg.grid(row=0, column=0)
            self.root.after(3000, self.root.destroy)
            return
        
        if self.farmacia.getGerente():
            msg = Message(self.root, text='Gerente já registrado!')
            msg.grid(row=0, column=0)
            self.root.after(3000, self.root.destroy)
            return 

        Label(self.root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.root, text="Cpf:").grid(row=1)
        campo_cpf = Entry(self.root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get()
            cpf = campo_cpf.get()
            data_nascimento = campo_dataNasc.get()
            salario = Decimal(campo_salario.get())

            try:
                self.farmacia._registrarGerente(nome, cpf, data_nascimento, salario)
            except Exception as erro:
                msg = Message(self.root, text=f'{erro}')
                msg.grid(row=0, column=0)
                self.root.after(3000, self.root.destroy)
                return 
            
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.root.destroy()

        self.__botaoRegistrar('Registrar Gerente', instanciar).grid(row=4, column=1)

        self.root.mainloop()