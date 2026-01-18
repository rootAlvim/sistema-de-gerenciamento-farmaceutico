from tkinter import *
from tkinter import messagebox
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto
from decimal import Decimal
from datetime import datetime

class Interface:
    def __init__(self):
        self.__root = None
        self.__farmacia = None
        self.__idFuncionarioLogado = None
    
    def interface(self):
        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Interface')

        botao_registrarFarmacia = Button(
            self.__root, 
            text="Registrar Farmacia", 
            padx=10, 
            pady=10, 
            command=self.registrarFarmacia).grid(row=0, column=0)
        
        botao_registrarGerente = Button(
            self.__root, 
            text="Registrar Gerente", 
            padx=10, 
            pady=10, 
            command=self.registrarGerente).grid(row=0, column=1)
        
        botao_registrarAtendente = Button(
            self.__root, 
            text="Registrar Atendente", 
            padx=10, 
            pady=10, 
            command=self.registrarAtendente).grid(row=2, column=0)
        
        botao_registrarProduto = Button(
            self.__root, 
            text="Registrar Produto", 
            padx=10, 
            pady=10, 
            command=self.registrarProduto).grid(row=2, column=1)
        
        self.__root.mainloop()

    def __temFarmacia(self):
        if not self.__farmacia:
            messagebox.showinfo("Farmácia não registrada.", "É necessário criar farmácia primeiro.")
            self.__root.destroy()
            self.interface()
        return True
    
    def __campoVazioMessagem(self, funcao):
        messagebox.showerror("Erro de Valor", f"Campo não pode estar vázio.")
        funcao()

    def __autenticacaoValidacao(self):
        if not self.__idFuncionarioLogado:
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado para conseguir prosseguir.")
            self.__root.destroy()
            self.interface()

    def __usuarioTipoGerente(self):
        idGerente = self.__farmacia.getGerente().get_id()
        if not self.__idFuncionarioLogado == idGerente:
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Gerente para conseguir prosseguir.")
            self.__root.destroy()
            self.interface()

    def __botaoRegistrar(self, texto, funcao):
        botao_registrar = Button(
            self.__root, 
            text=texto, 
            padx=10, 
            pady=10, 
            command=funcao)
        return botao_registrar

    def registrarFarmacia(self):
        from src.farmacia.farmacia import Farmacia
        self.__root.destroy()
        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Registrar Farmácia')

        campo_nome = Entry(self.__root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=0, columnspan=2)

        def instanciar():
            nome = campo_nome.get()
            if nome:
                self.__farmacia = Farmacia(nome)
                campo_nome.delete(0, END)
                self.__root.destroy()
                self.interface()

        self.__botaoRegistrar('Registrar Farmácia', instanciar).grid(row=1, column=0)

        self.__root.mainloop()

    def registrarAtendente(self):
        self.__root.destroy()
        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Registrar Atendente')
        self.__temFarmacia()
        self.__autenticacaoValidacao()
        self.__usuarioTipoGerente()

        Label(self.__root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.__root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.__root, text="CPF:").grid(row=1)
        campo_cpf = Entry(self.__root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.__root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.__root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.__root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.__root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarAtendente)
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get()

            try:
                id = self.__farmacia.getGerente().cadrastar_funcionario(nome, cpf, data_nascimento, Decimal(salario))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Atendente.", f"{erro}")
                self.registrarAtendente()
            print(self.__idFuncionarioLogado)
            self.__idFuncionarioLogado = id # !!!!!!! remover
            print(self.__idFuncionarioLogado)
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Atendente', instanciar).grid(row=4, column=1)

        self.__root.mainloop()

    def registrarGerente(self):
        self.__root.destroy()
        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Registrar Gerente')
        self.__temFarmacia()
        
        if self.__farmacia.getGerente():
            messagebox.showinfo("Gerente já registrado", "Gerente só pode ser registrado uma única vez.")
            self.__root.destroy()
            self.interface()

        Label(self.__root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.__root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.__root, text="CPF:").grid(row=1)
        campo_cpf = Entry(self.__root, width=25, borderwidth=1)
        campo_cpf.grid(row=1, column=1, columnspan=2)

        Label(self.__root, text="Data de Nascimento:").grid(row=2)
        campo_dataNasc = Entry(self.__root, width=25, borderwidth=1)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.__root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.__root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        Label(self.__root, text="Senha:").grid(row=4)
        campo_senha = Entry(self.__root, width=25, borderwidth=1)
        campo_senha.grid(row=4, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarGerente)
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get()
            senha = campo_senha.get() if campo_senha.get() else self.__campoVazioMessagem(self.registrarGerente)

            try:
                self.__farmacia._registrarGerente(nome, cpf, data_nascimento, Decimal(salario), senha)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                self.registrarGerente()
            
            self.__idFuncionarioLogado = self.__farmacia.getGerente().get_id()
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Gerente', instanciar).grid(row=5, column=1)

        self.__root.mainloop()

    def registrarProduto(self):
        '''Cria objeto de produto e já adiciona em estoque''' # por enquanto fica essa solução apra produto
        self.__root.destroy()
        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Registrar Produto')
        self.__temFarmacia()

        Label(self.__root, text="Nome:").grid(row=0)
        campo_nome = Entry(self.__root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        Label(self.__root, text="Preço:").grid(row=1)
        campo_preco = Entry(self.__root, width=25, borderwidth=1)
        campo_preco.grid(row=1, column=1, columnspan=2)

        Label(self.__root, text="Fabricante:").grid(row=2)
        campo_fabricante = Entry(self.__root, width=25, borderwidth=1)
        campo_fabricante.grid(row=2, column=1, columnspan=2)

        Label(self.__root, text="Quantidade:").grid(row=3)
        campo_qtd = Entry(self.__root, width=25, borderwidth=1)
        campo_qtd.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarProduto)
            fabricante = campo_fabricante.get() if campo_fabricante.get() else self.__campoVazioMessagem(self.registrarProduto)
            preco = campo_preco.get()
            quantidade = campo_qtd.get()

            try:
                self.__farmacia._estoque.adicionar_produto(Produto(nome, Decimal(preco), fabricante), int(quantidade))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Produto.", f"{erro}")
                self.registrarProduto()
            
            campo_nome.delete(0, END)
            campo_fabricante.delete(0, END)
            campo_preco.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoRegistrar('Registrar Produto', instanciar).grid(row=4, column=1)

        self.__root.mainloop()

    