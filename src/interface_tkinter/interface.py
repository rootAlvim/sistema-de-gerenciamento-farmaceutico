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
        try:
            self.__root.destroy()
        except:
            pass

        if not self.__farmacia:
            self.registrarFarmacia()
            return
        
        if not self.__farmacia.getGerente():
            self.registrarGerente()
            return

        self.__root = Tk()
        self.__root.geometry("500x300")
        self.__root.title('Interface')

        self.__botaoPadrao("Login", self.login).grid(row=0, column=0)
        self.__botaoPadrao("Logout", self.logout).grid(row=0, column=1)
        self.__botaoPadrao("Registrar Atendente", self.registrarAtendente).grid(row=2, column=0)
        self.__botaoPadrao("Registrar Produto", self.registrarProduto).grid(row=2, column=1)
        self.__botaoPadrao("Consultar Estoque", self.consultarEstoque).grid(row=3, column=1)

        self.__root.mainloop()

    def logout(self):
        '''Reseta valor de idFuncionarioLogado para None.'''      
        if not self.__idFuncionarioLogado:
            messagebox.showinfo("Logout interrompido", f"Você não está logado.")
            return
        
        # if self.__usuarioTipoGerente():
        #     self.__farmacia.getGerente().desautenticar() 
        #     self.__idFuncionarioLogado = None
        #     messagebox.showinfo("Logout Sucesso", f"Você foi deslogado do sistema.")
        #     return
            
        self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).desautenticar() 
        self.__idFuncionarioLogado = None

        messagebox.showinfo("Logout Sucesso", f"Você foi deslogado do sistema.")

    def login(self):
        '''Atribui um Id a idFuncionarioLogado.'''
        self.__temFarmacia()
        if self.__idFuncionarioLogado:
            messagebox.showinfo("Login interrompido", f"Você já está logado.")
            return
        
        self.__inciarRoot()
        self.__root.title('Login')

        Label(self.__root, text="Id de Funcionário:").grid(row=0)
        campo_id = Entry(self.__root, width=25, borderwidth=1)
        campo_id.grid(row=0, column=1, columnspan=2)

        Label(self.__root, text="Senha:").grid(row=1)
        campo_senha = Entry(self.__root, width=25, borderwidth=1)
        campo_senha.grid(row=1, column=1, columnspan=2)

        def instanciar():
            id = campo_id.get() if campo_id.get() else self.__campoVazioMessagem(self.login, 'id')
            senha = campo_senha.get() if campo_senha.get() else self.__campoVazioMessagem(self.login, 'senha')
            
            try:
                funcionario = self.__farmacia.getFuncionarioPorId(int(id))
                # if self.__farmacia.getGerente().get_id() == int(id):
                #     funcionario = self.__farmacia.getGerente()                
            except Exception as erro:
                messagebox.showerror("Erro ao tentar logar.", f"{erro}")
                self.login()

            if not funcionario:
                messagebox.showerror("Login erro.", f"Funcionario com Id: {id} não encontrado.")
                self.login()

            try:
                funcionario.setAutenticacao(int(id), senha)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar logar.", f"{erro}")
                self.login()
            
            self.__idFuncionarioLogado = int(id)
            messagebox.showinfo("Login Sucesso", f"Login feito com sucesso. {funcionario.nome}")
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Logar', instanciar).grid(row=2, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=2, column=2)

        self.__root.mainloop()

    def registrarFarmacia(self):
        from src.farmacia.farmacia import Farmacia
        self.__inciarRoot()
        self.__root.title('Registrar Farmácia')

        if self.__farmacia:
            messagebox.showinfo("Farmácia Info", "Farmácia já foi criada.")
            self.__root.destroy()
            self.interface()

        Label(self.__root, text="Nome da Farmácia:").grid(row=0)
        campo_nome = Entry(self.__root, width=25, borderwidth=1)
        campo_nome.grid(row=0, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarFarmacia, 'nome')
            if nome:
                self.__farmacia = Farmacia(nome)
                self.__root.destroy()
                self.interface()

        self.__botaoPadrao('Registrar Farmácia', instanciar).grid(row=1, column=1)

        self.__root.mainloop()

    def registrarAtendente(self):
        self.__inciarRoot()
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
        Label(self.__root, text="Ex.: 00-00-0000").grid(row=2, column=3)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.__root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.__root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarAtendente, 'nome')
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get() if campo_salario.get() else self.__campoVazioMessagem(self.registrarAtendente, 'salario')

            try:
                self.__farmacia.getGerente().cadrastar_funcionario(nome, cpf, data_nascimento, Decimal(salario))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Atendente.", f"{erro}")
                self.registrarAtendente()

            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Atendente', instanciar).grid(row=4, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=4, column=2)

        self.__root.mainloop()

    def registrarGerente(self):
        self.__inciarRoot()
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
        Label(self.__root, text="Ex.: 00-00-0000").grid(row=2, column=3)
        campo_dataNasc.grid(row=2, column=1, columnspan=2)

        Label(self.__root, text="Salario:").grid(row=3)
        campo_salario = Entry(self.__root, width=25, borderwidth=1)
        campo_salario.grid(row=3, column=1, columnspan=2)

        Label(self.__root, text="Senha:").grid(row=4)
        campo_senha = Entry(self.__root, width=25, borderwidth=1)
        campo_senha.grid(row=4, column=1, columnspan=2)

        def instanciar():
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarGerente, 'nome')
            cpf = campo_cpf.get()
            data_nascimento = datetime.strptime(campo_dataNasc.get(), "%d-%m-%Y") if campo_dataNasc.get() else None
            salario = campo_salario.get() if campo_salario.get() else self.__campoVazioMessagem(self.registrarGerente, 'salario')
            senha = campo_senha.get() if campo_senha.get() else self.__campoVazioMessagem(self.registrarGerente, 'senha')

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

        self.__botaoPadrao('Registrar Gerente', instanciar).grid(row=5, column=1)

        self.__root.mainloop()

    def registrarProduto(self):
        '''Cria objeto de produto e já adiciona em estoque''' # por enquanto fica essa solução apra produto
        self.__inciarRoot()
        self.__root.title('Registrar Produto')
        self.__temFarmacia()
        self.__autenticacaoValidacao()

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
            nome = campo_nome.get() if campo_nome.get() else self.__campoVazioMessagem(self.registrarProduto, 'nome')
            fabricante = campo_fabricante.get() if campo_fabricante.get() else self.__campoVazioMessagem(self.registrarProduto, 'fabricante')
            preco = campo_preco.get()
            quantidade = campo_qtd.get()

            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).adicionar_produto_estoque(Produto(nome, Decimal(preco), fabricante), int(quantidade))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Produto.", f"{erro}")
                self.registrarProduto()
            
            campo_nome.delete(0, END)
            campo_fabricante.delete(0, END)
            campo_preco.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Produto', instanciar).grid(row=4, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=4, column=2)

        self.__root.mainloop()

    def consultarEstoque(self):
        from tkinter import ttk
        self.__inciarRoot()
        self.__root.title('Consultar estoque')
        self.__temFarmacia()
        self.__autenticacaoValidacao()
        produto_labels = []

        def removerProduto(id_produto, produto_label, botao_remover):
            verificacao = messagebox.askyesno("Remover Produto", f"Você realmente deseja remover produto, id={id_produto}?")

            if not verificacao:
                self.consultarEstoque()
                return
            
            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).remover_produto(id_produto)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar remover Produto.", f"{erro}")
                self.consultarEstoque()

            try:
                produto_label.destroy()
                botao_remover.destroy()
            except:
                return

        def consultar():
            consultar_por = menu.get()
            valor = consulta_campo.get()
            produto = None

            if not valor:
                return

            if consultar_por == "Id":
                produto = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).consultar_produto_por_id(int(valor))
            elif consultar_por == "Nome":
                produto = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).consultar_produto_por_nome(valor)
            
            if produto:
                self.__removerWidgets(produto_labels)

                produto_label = Label(self.__root, text=f"{produto[0]} | Quantidade: {produto[1]}")
                produto_label.grid(row=2, column=0, columnspan=3)
                produto_labels.append(produto_label)
                return
            return

        consulta_campo = Entry(self.__root, width=25, borderwidth=1)
        consulta_campo.grid(row=1, column=0, columnspan=1)

        Label(self.__root, text="Consultar por:").grid(row=0, column=2)
        opcoes_consulta = ["Id", "Nome"]
        menu = ttk.Combobox(self.__root, values=opcoes_consulta, state="readonly")
        menu.set("Id")
        menu.grid(row=1, column=2)

        self.__botaoPadrao("Consultar", consultar, pady=4).grid(row=1, column=4)
        self.__botaoPadrao("Limpar", self.consultarEstoque, pady=4).grid(row=1, column=5)
        self.__botaoPadrao("Voltar", self.interface, pady=4).grid(row=1, column=6)

        produtos = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).consultar_estoque()
        row_ = 2
        for produto, qtd in produtos.items():
            produto_label = Label(self.__root, text=f"{produto} | Quantidade: {qtd}")
            produto_label.grid(row=row_, column=0, columnspan=3)
            botao_remover = self.__botaoPadrao("Remover", lambda: removerProduto(produto.getId(), produto_label, botao_remover), pady=4)
            botao_remover.grid(row=row_, column=4)
            produto_labels.append(produto_label)
            row_ += 1
            
        self.__root.mainloop()


    def __inciarRoot(self):
        try:
            self.__root.destroy()
        except:
            pass
        self.__root = Tk()
        self.__root.geometry("500x300")

    def __temFarmacia(self):
        if not self.__farmacia:
            messagebox.showinfo("Farmácia não registrada.", "É necessário criar farmácia primeiro.")
            self.__root.destroy()
            self.interface()
        return True
    
    def __campoVazioMessagem(self, funcao, campo = ''):
        messagebox.showerror("Erro de Valor", f"Campo {campo} não pode estar vázio.")
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
        return True

    def __botaoPadrao(self, texto, funcao, padx=10, pady=10):
        botao_padrao = Button(
            self.__root, 
            text=texto, 
            padx=padx, 
            pady=pady, 
            command=funcao)
        return botao_padrao
    
    def __removerWidgets(self, widgets):
        for widget in widgets:
            try:
                widget.destroy()
            except:
                continue
    

    