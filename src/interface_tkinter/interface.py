from tkinter import *
from tkinter import messagebox
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto
from decimal import Decimal
from datetime import datetime

class Interface:
    def __init__(self, nome_farmacia: str):
        self.__root = None
        self.__farmacia = Farmacia(nome_farmacia)
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
        self.__botaoPadrao("Registrar Repositor", self.registrarRepositor).grid(row=3, column=0)
        self.__botaoPadrao("Registrar Produto", self.registrarProduto).grid(row=2, column=1)
        self.__botaoPadrao("Consultar Estoque", self.consultarEstoque).grid(row=3, column=1)
        self.__botaoPadrao("Registrar Cliente", self.registrarCliente).grid(row=4, column=0)
        self.__botaoPadrao("Registrar Venda", self.registrarVenda).grid(row=4, column=1)

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
            from src.utils.validacoes import validar_formato_cpf
            if campo_nome.get():
                nome = campo_nome.get() 
            else: 
                self.__campoVazioMessagem(None, 'nome') 
                return
            
            if campo_cpf.get():
                try:
                    cpf = validar_formato_cpf(campo_cpf.get())
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'CPF') 
                return
             
            if campo_dataNasc.get():
                try:
                    data_nascimento = datetime.strptime(self.dataNascimentoRegex(campo_dataNasc.get()), "%d%m%Y")
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'Data de Nascimento') 
                return
            
            if campo_salario.get():
                salario = campo_salario.get()
            else: 
                self.__campoVazioMessagem(None, 'salario')
                return
            
            if campo_senha.get():
                senha = campo_senha.get()
            else: 
                self.__campoVazioMessagem(None, 'senha')
                return

            try:
                self.__farmacia._registrarGerente(nome, cpf, data_nascimento, Decimal(salario), senha)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                return
            
            self.__idFuncionarioLogado = self.__farmacia.getGerente().get_id()
            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Gerente', instanciar).grid(row=5, column=1)

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
            from src.utils.validacoes import validar_formato_cpf
            if campo_nome.get():
                nome = campo_nome.get() 
            else: 
                self.__campoVazioMessagem(None, 'nome') 
                return
            
            if campo_cpf.get():
                try:
                    cpf = validar_formato_cpf(campo_cpf.get())
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'CPF') 
                return
             
            if campo_dataNasc.get():
                try:
                    data_nascimento = datetime.strptime(self.dataNascimentoRegex(campo_dataNasc.get()), "%d%m%Y")
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'Data de Nascimento') 
                return
            
            if campo_salario.get():
                salario = campo_salario.get()
            else: 
                self.__campoVazioMessagem(None, 'salario')
                return

            try:
                self.__farmacia.getGerente().cadrastar_funcionario('atendente', nome, cpf, data_nascimento, Decimal(salario))
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

    def registrarRepositor(self):
        self.__inciarRoot()
        self.__root.title('Registrar Repositor')
        self.__temFarmacia()
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
            from src.utils.validacoes import validar_formato_cpf
            if campo_nome.get():
                nome = campo_nome.get() 
            else: 
                self.__campoVazioMessagem(None, 'nome') 
                return
            
            if campo_cpf.get():
                try:
                    cpf = validar_formato_cpf(campo_cpf.get())
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'CPF') 
                return
             
            if campo_dataNasc.get():
                try:
                    data_nascimento = datetime.strptime(self.dataNascimentoRegex(campo_dataNasc.get()), "%d%m%Y")
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'Data de Nascimento') 
                return
            
            if campo_salario.get():
                salario = campo_salario.get()
            else: 
                self.__campoVazioMessagem(None, 'salario')
                return

            try:
                self.__farmacia.getGerente().cadrastar_funcionario('repositor', nome, cpf, data_nascimento, Decimal(salario))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Repositor.", f"{erro}")
                self.registrarAtendente()

            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            campo_salario.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Repositor', instanciar).grid(row=4, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=4, column=2)

        self.__root.mainloop()

    def registrarCliente(self):
        self.__inciarRoot()
        self.__root.title('Registrar Cliente')
        self.__temFarmacia()
        self.__usuarioTipoGerenteOuAtendente()

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

        def instanciar():
            from src.utils.validacoes import validar_formato_cpf
            if campo_nome.get():
                nome = campo_nome.get() 
            else: 
                self.__campoVazioMessagem(None, 'nome') 
                return
            
            if campo_cpf.get():
                try:
                    cpf = validar_formato_cpf(campo_cpf.get())
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'CPF') 
                return
             
            if campo_dataNasc.get():
                try:
                    data_nascimento = datetime.strptime(self.dataNascimentoRegex(campo_dataNasc.get()), "%d%m%Y")
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar registrar Gerente.", f"{erro}")
                    return
            else:
                self.__campoVazioMessagem(None, 'Data de Nascimento') 
                return

            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).registrarCliente(nome, cpf, data_nascimento)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Cliente.", f"{erro}")
                self.registrarCliente()

            campo_nome.delete(0, END)
            campo_cpf.delete(0, END)
            campo_dataNasc.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Cliente', instanciar).grid(row=4, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=4, column=2)

        self.__root.mainloop()

    def registrarProduto(self):
        '''Cria objeto de produto e já adiciona em estoque''' # por enquanto fica essa solução apra produto
        self.__inciarRoot()
        self.__root.title('Registrar Produto')
        self.__temFarmacia()
        self.__usuarioTipoGerenteOuRepositor()

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
            if campo_nome.get():
                nome = campo_nome.get() 
            else: 
                self.__campoVazioMessagem(None, 'nome') 
                return
             
            if campo_fabricante.get():
                fabricante = campo_fabricante.get()
            else:
                self.__campoVazioMessagem(None, 'fabricante')
                return
            
            preco = campo_preco.get()
            quantidade = campo_qtd.get()

            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).adicionar_produto_estoque(Produto(nome, Decimal(preco), fabricante), int(quantidade))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar registrar Produto.", f"{erro}")
                return
            
            campo_nome.delete(0, END)
            campo_fabricante.delete(0, END)
            campo_preco.delete(0, END)
            self.__root.destroy()
            self.interface()

        self.__botaoPadrao('Registrar Produto', instanciar).grid(row=4, column=1)
        self.__botaoPadrao("Voltar", self.interface).grid(row=4, column=2)

        self.__root.mainloop()
    
    def registrarVenda(self, id_venda = None):
        from tkinter import ttk
        self.__inciarRoot(tamanho='800x400')
        self.__root.title('Registrar Venda')
        self.__temFarmacia()
        self.__usuarioTipoGerenteOuAtendente()

        if not id_venda:
            try:
                id_venda = self.__farmacia._criarVenda(self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar criar venda.", f"{erro}")
                self.interface()
                return

        def adicionarCliente():
            funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
            cpf = cliente_cpf.get()
            cliente_cpf.delete(0, END)
            cliente = self.__farmacia.getClientePorCpf(cpf)
            if not cliente:
                messagebox.showerror("Erro ao procurar cliente por CPF.", f'Cliente com CPF:{cpf} não existe em farmácia.')
                # self.registrarVenda(id_venda)
                return
            
            funcionario.adicionar_cliente_venda(cliente)
            Label(self.__root, text=f'{cliente}').grid(row=2, column=2)
            return
        
        def show_produtos():
            if id_venda:
                _row = 4
                for itemVenda in self.__farmacia.getVendaPorId(id_venda).getProdutos():
                    produto_label = Label(self.__root, text=itemVenda)
                    produto_label.grid(row=_row, column=2, padx=(10, 0))

                    botao_remover = self.__botaoPadrao("Remover", lambda: removerProduto(itemVenda, produto_label, botao_remover))
                    botao_remover.grid(row=_row, column=3)
                    _row += 1

        def adicionarProduto():
            funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
            campo_menu = menu.get()
            
            if campo_menu == 'Id':
                try:
                    produto = self.__farmacia._estoque.consultar_produto_por_id(funcionario, int(campo_produto.get()))
                except Exception as erro:
                    messagebox.showerror(f'Erro ao procurar produto por ID.', f'{erro}')
                    # self.registrarVenda(id_venda)
                    return
                
            elif campo_menu == 'Nome':
                try:
                    produto = self.__farmacia._estoque.consultar_produto_por_nome(funcionario, campo_produto.get())
                except Exception as erro:
                    messagebox.showerror(f'Erro ao procurar produto por Nome.', f'{erro}')
                    # self.registrarVenda(id_venda)
                    return

            if not produto:
                messagebox.showerror("Erro ao procurar produto.", f'Produto informado não existe ou não está disponível em estoque.')
                # self.registrarVenda(id_venda)
                return

            try:
                funcionario.adicionar_produto_venda(produto[0], int(campo_qtd.get()))
            except Exception as erro:
                messagebox.showerror(f'Erro ao tentar adicionar produto.', f'{erro}')
                return

            show_produtos()
            campo_produto.delete(0, END)
            campo_qtd.delete(0, END)
            campo_qtd.insert(0, 1)

        def removerProduto(itemVenda, produto_label, botao_remover):
            verificacao = messagebox.askyesno("Remover Produto", f"Você realmente deseja remover produto, id={itemVenda.id}?")

            if not verificacao:
                return
            
            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).remover_produto_venda(itemVenda.id)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar remover Produto.", f"{erro}")
                return

            try:
                produto_label.destroy()
                botao_remover.destroy()
            except:
                return

        def voltar():
            self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).remover_venda(id_venda) 
            self.interface()
            return

        Label(self.__root, text="Adicionar cliente via CPF em venda:").grid(row=1)
        cliente_cpf = Entry(self.__root, width=25, borderwidth=1)
        cliente_cpf.grid(row=2, column=0)
        self.__botaoPadrao("Adicionar cliente", adicionarCliente, pady=4).grid(row=3, column=0, pady=10)

        Label(self.__root, text="Adicionar produto em venda:").grid(row=4, column=0)
        campo_produto = Entry(self.__root, width=20, borderwidth=1)
        campo_produto.grid(row=5, column=0, sticky='e')

        opcoes_consulta = ["Id", "Nome"]
        menu = ttk.Combobox(self.__root, values=opcoes_consulta, state="readonly", width=6)
        menu.set("Id")
        menu.grid(row=5, column=0, sticky='w', padx=(5, 0))

        Label(self.__root, text="Quantidade:").grid(row=4, column=1, sticky='w')
        campo_qtd = Entry(self.__root, width=15, borderwidth=1)
        campo_qtd.insert(0, '1')
        campo_qtd.grid(row=5, column=1, padx=5)
        self.__botaoPadrao("Adicionar Produto", adicionarProduto, pady=4).grid(row=6, column=0, pady=10)

        self.__botaoPadrao('Finalizar Venda', '').grid(row=9, column=0)
        self.__botaoPadrao("Voltar", voltar).grid(row=9, column=1)

        self.__root.mainloop()

    def consultarEstoque(self):
        from tkinter import ttk
        self.__inciarRoot(tamanho="800x400")
        self.__root.title('Consultar estoque')
        self.__temFarmacia()
        self.__usuarioTipoGerenteOuRepositor()
        produto_labels = []
        botoes_remover = []

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
                self.__removerWidgets(botoes_remover)

                produto_label = Label(self.__root, text=f"{produto[0]} | Quantidade: {produto[1]}")
                produto_label.grid(row=2, column=0, columnspan=3)

                botao_editar_preco = self.__botaoPadrao("Edit Preço", lambda: self.__editarPrecoProduto(produto[0]), pady=2, padx=6)
                botao_editar_preco.grid(row=2, column=4)

                botao_remover = self.__botaoPadrao("Remover", lambda: self.__removerProduto(produto[0].getId(), produto_label, botao_remover, botao_editar_preco), pady=4)
                botao_remover.grid(row=2, column=5)

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

            botao_editar_preco = self.__botaoPadrao("Edit Preço", lambda: self.__editarPrecoProduto(produto), pady=2, padx=6)
            botao_editar_preco.grid(row=row_, column=4)

            botao_remover = self.__botaoPadrao("Remover", lambda: self.__removerProduto(produto.getId(), produto_label, botao_remover, botao_editar_preco), pady=2)
            botao_remover.grid(row=row_, column=5)

            produto_labels.append(produto_label)
            botoes_remover.append(botao_remover)
            botoes_remover.append(botao_editar_preco)
            row_ += 1
            
        self.__root.mainloop()

    def __inciarRoot(self, tamanho = "500x300"):
        try:
            self.__root.destroy()
        except:
            pass
        self.__root = Tk()
        self.__root.geometry(tamanho)

    def __temFarmacia(self):
        if not self.__farmacia:
            messagebox.showinfo("Farmácia não registrada.", "É necessário criar farmácia primeiro.")
            self.__root.destroy()
            self.interface()
        return True
    
    def __campoVazioMessagem(self, funcao = None, campo = ''):
        messagebox.showerror("Erro de Valor", f"Campo {campo} não pode estar vázio.")
        if funcao:
            funcao()

    def __autenticacaoValidacao(self):
        if not self.__idFuncionarioLogado:
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado para conseguir prosseguir.")
            self.__root.destroy()
            self.interface()

    def dataNascimentoRegex(self, data_nascimento):
        import re
        data_nascimento = re.sub(r'[-/\.]','', data_nascimento)
        return data_nascimento
        
    def __usuarioTipoGerente(self):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not funcionario.__class__.__name__ == 'Gerente':
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Gerente para conseguir prosseguir.")
            self.__root.destroy()
            self.interface()
        return True
    
    def __usuarioTipoGerenteOuRepositor(self):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not (funcionario.__class__.__name__ == 'Gerente' or funcionario.__class__.__name__ == 'Repositor'):
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Gerente ou Repositor para conseguir prosseguir.")
            self.__root.destroy()
            self.interface()
        return True
    
    def __usuarioTipoGerenteOuAtendente(self):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not (funcionario.__class__.__name__ == 'Gerente' or funcionario.__class__.__name__ == 'Atendente'):
            messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Gerente ou Atendente para conseguir prosseguir.")
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

    def __removerProduto(self, id_produto, produto_label, botao_remover, botao_editar_preco):
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
                botao_editar_preco.destroy()
            except:
                return
            
    def __editarPrecoProduto(self, produto):
        self.__inciarRoot()
        self.__root.title('Editar Preço')
        self.__temFarmacia()
        self.__usuarioTipoGerente()

        def setPreco():
            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).alterar_preco_produto(produto, Decimal(campo_preco.get()))
            except Exception as erro:
                messagebox.showerror("Erro ao tentar remover Produto.", f"{erro}")
                self.__editarPrecoProduto(produto)
                return
            self.consultarEstoque()

        Label(self.__root, text=f"Alterar preço do produto. Preço Atual: {produto.getPreco()}").grid(row=0, columnspan=3)
        Label(self.__root, text=f"Novo Preço:").grid(row=1)
        campo_preco = Entry(self.__root, width=25, borderwidth=1)
        campo_preco.grid(row=1, column=1, columnspan=1)

        self.__botaoPadrao("Alterar", setPreco, pady=4).grid(row=2, column=1)

        self.__root.mainloop()


    

    