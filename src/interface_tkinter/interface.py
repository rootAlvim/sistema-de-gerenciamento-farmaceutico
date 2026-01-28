from tkinter import *
from tkinter import messagebox
from src.farmacia.salvar_farmacia import salvar_farmacia, carregar_farmacia, excluir_farmacia
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto
from decimal import Decimal
from datetime import datetime

class Interface:
    def __init__(self, nome_farmacia: str):
        self.__root = None
        self.__farmacia = carregar_farmacia() if carregar_farmacia() else Farmacia(nome_farmacia)
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
        
        if not self.__idFuncionarioLogado:
            self.login()
            return
        
        if self.__atendenteRepositorPrimeiroAcesso(retornarBool=True):
            self.__atendenteRepositorPrimeiroAcesso()
            return
        
        self.__inciarRoot(tamanho="900x400")
        self.__root.title(f'Farmacia {self.__farmacia.nome}')

        self.__root.rowconfigure(0, weight=1)
        self.__root.rowconfigure(1, weight=1)
        self.__root.rowconfigure(2, weight=1)
        self.__root.rowconfigure(3, weight=1)
        self.__root.rowconfigure(4, weight=1)
        self.__root.columnconfigure(0, weight=3)
        self.__root.columnconfigure(1, weight=1)
        self.__root.columnconfigure(2, weight=1)

        row_base = 0
        column_base = 0

        Label(self.__root, text=f"Farmácia {self.__farmacia.nome}", font=("Arial", 25, "bold")).grid(row=row_base+1, column=column_base)

        try:
            funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
            Label(self.__root, text=f"Bem vindo, {funcionario.nome}", font=("Arial", 15)).grid(row=row_base+2, column=column_base, sticky='N')
        except:
            pass
        
        self.__botaoPadrao("Meu Perfil", self.perfilFuncionario, pady=3, padx=5).grid(row=row_base, column=column_base+1, sticky='N')
        self.__botaoPadrao("Login", self.login, pady=3, padx=5).grid(row=row_base, column=column_base+2, sticky="NW", padx=0)
        self.__botaoPadrao("Logout", self.logout, pady=3, padx=5).grid(row=row_base, column=column_base+2, sticky="NW",padx=(60, 0)) 
        
        self.__botaoPadrao("Registrar Atendente", self.registrarAtendente).grid(row=row_base+1, column=column_base+1, sticky='SE')
        self.__botaoPadrao("Registrar Repositor", self.registrarRepositor, padx=12.5).grid(row=row_base+2, column=column_base+1, sticky='NE', pady=(0,0))
        self.__botaoPadrao("Registrar Produto", self.registrarProduto, padx=16.5).grid(row=row_base+2, column=column_base+1, sticky="SE", pady=(0,0))
        self.__botaoPadrao("Consultar Estoque", self.consultarEstoque, padx=15.4).grid(row=row_base+3, column=column_base+1, sticky="NE")
        self.__botaoPadrao("Registrar Cliente", self.registrarCliente, padx=21).grid(row=row_base+1, column=column_base+2,sticky='SW')
        self.__botaoPadrao("Registrar Venda", self.registrarVenda, padx=23).grid(row=row_base+2, column=column_base+2,sticky='NW',pady=(0,0))
        self.__botaoPadrao("Consultar Vendas", self.consultarVendasFarmacia, padx=18).grid(row=row_base+2, column=column_base+2, sticky="SW", pady=(0,0))
        self.__botaoPadrao("Consultar Funcionarios", self.consultarFuncionarios, padx=3).grid(row=row_base+3, column=column_base+2, sticky="NW")

        self.__root.mainloop()

    def logout(self):
        '''Reseta valor de idFuncionarioLogado para None.'''      
        if not self.__idFuncionarioLogado:
            messagebox.showinfo("Logout interrompido", f"Você não está logado.")
            return
            
        self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).desautenticar() 
        self.__idFuncionarioLogado = None

        messagebox.showinfo("Logout Sucesso", f"Você foi deslogado do sistema.")
        self.login()
        return 

    def login(self):
        '''Atribui um Id a idFuncionarioLogado.'''
        self.__temFarmacia()
        if self.__idFuncionarioLogado:
            messagebox.showinfo("Login interrompido", f"Você já está logado.")
            return
        
        self.__inciarRoot()
        self.__root.title('Login')

        Label(self.__root, text="ID de Funcionário:").grid(row=0)
        campo_id = Entry(self.__root, width=25, borderwidth=1)
        campo_id.grid(row=0, column=1, columnspan=2)

        Label(self.__root, text="Senha:").grid(row=1)
        campo_senha = Entry(self.__root, show="*", width=25, borderwidth=1)
        campo_senha.grid(row=1, column=1, columnspan=2)

        def instanciar():
            id = campo_id.get() if campo_id.get() else self.__campoVazioMessagem(self.login, 'id')
            senha = campo_senha.get() if campo_senha.get() else self.__campoVazioMessagem(self.login, 'senha')
            
            try:
                funcionario = self.__farmacia.getFuncionarioPorId(int(id))            
            except Exception as erro:
                messagebox.showerror("Erro ao tentar logar.", f"{erro}")
                self.login()
                return

            if not funcionario:
                messagebox.showerror("Login erro.", f"Funcionario com Id: {id} não encontrado.")
                self.login()
                return

            try:
                funcionario.setAutenticacao(int(id), senha)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar logar.", f"{erro}")
                self.login()
                return
            
            self.__idFuncionarioLogado = int(id)
            messagebox.showinfo("Login Sucesso", f"Login feito com sucesso. {funcionario.nome}")
            self.__root.destroy()
            self.interface()
            return

        self.__botaoPadrao('Logar', instanciar ,pady=5).grid(row=2, column=1, sticky='W', pady=(10,0))

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
            return

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
                    data_nascimento = datetime.strptime(self.__dataRegex(campo_dataNasc.get()), "%d%m%Y")
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
                    data_nascimento = datetime.strptime(self.__dataRegex(campo_dataNasc.get()), "%d%m%Y")
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
                    data_nascimento = datetime.strptime(self.__dataRegex(campo_dataNasc.get()), "%d%m%Y")
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
                    data_nascimento = datetime.strptime(self.__dataRegex(campo_dataNasc.get()), "%d%m%Y")
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
        self.__labels_produto = []

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
                self.__removerWidgets(self.__labels_produto)
                _row = 4
                for itemVenda in self.__farmacia.getVendaPorId(id_venda).getProdutos():
                    produto_label = Label(self.__root, text=itemVenda)
                    produto_label.grid(row=_row, column=2, padx=(10, 0))

                    botao_remover = self.__botaoPadrao("Remover", lambda: removerProduto(itemVenda))
                    botao_remover.grid(row=_row, column=3)
                    self.__labels_produto.append(produto_label)
                    self.__labels_produto.append(botao_remover)
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

        def removerProduto(itemVenda):
            verificacao = messagebox.askyesno("Remover Produto", f"Você realmente deseja remover produto, id={itemVenda.id}?")

            if not verificacao:
                return
            
            try:
                self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).remover_produto_venda(itemVenda.id)
            except Exception as erro:
                messagebox.showerror("Erro ao tentar remover Produto.", f"{erro}")
                return
            
            show_produtos()
            
        def voltar():
            self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).remover_venda(id_venda) 
            self.interface()
            return
        
        def finalizarVenda():
            funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
            try:
                funcionario.finalizar_venda()
            except Exception as erro:
                messagebox.showerror("Erro ao tentar finalizar venda.", f"{erro}")
                return
            
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

        self.__botaoPadrao('Finalizar Venda', finalizarVenda).grid(row=9, column=0)
        self.__botaoPadrao("Voltar", voltar).grid(row=9, column=1)

        self.__root.mainloop()

    def consultarVendasFarmacia(self):
        from tkinter import ttk
        self.__inciarRoot(tamanho='700x300')
        self.__root.title('Consultar Vendas')
        self.__temFarmacia()
        self.__usuarioTipoGerente()
        self.__labels_venda = []

        vendas = self.__farmacia.getListaVendas()
        if not vendas:
            Label(self.__root, text="Nenhuma venda foi feita ainda.").grid(row=2)

        def consultar():
            consulta_valor = campo_consulta.get()
            campo_consulta.delete(0,END)
            vendas_consulta = None
            venda_consulta = None

            if menu.get() == 'Id':
                self.__removerWidgets(self.__labels_venda)
                try:
                    venda_consulta = self.__farmacia.getVendaPorId(int(consulta_valor))
                except Exception as erro:
                    messagebox.showerror("Erro ao procurar por venda", f'{erro}')
                    self.consultarVendasFarmacia()
                    return
            elif menu.get() == 'Funcionario ID':
                self.__removerWidgets(self.__labels_venda)
                try:
                    vendas_consulta = self.__farmacia.getFuncionarioPorId(int(consulta_valor)).getVendasRealizadas()
                except Exception as erro:
                    messagebox.showerror("Erro ao procurar por venda", f'{erro}')
                    self.consultarVendasFarmacia()
                    return
            elif menu.get() == 'Data':
                try:
                    consulta_valor = datetime.strptime(self.__dataRegex(consulta_valor), "%d%m%Y").date()
                except Exception as erro:
                    messagebox.showerror("Erro ao procurar por venda", f'{erro}')
                    self.consultarVendasFarmacia()
                    return
                
                vendas_consulta = []
                for venda in self.__farmacia.getListaVendas():
                    if venda.getDataVenda().date() == consulta_valor:
                        vendas_consulta.append(venda)

            if (not venda_consulta) and (not vendas_consulta):
                messagebox.showerror("Erro ao procurar por venda", f'Venda com {menu.get()}:{consulta_valor} não existe.')
                self.consultarVendasFarmacia()
                return

            if vendas_consulta:
                row_ = 4
                for venda in vendas_consulta:
                    label_venda = Label(self.__root, text=venda)
                    label_venda.grid(row=row_, columnspan=10, padx=(25, 10))

                    botao_venda = self.__botaoPadrao("Ver venda", lambda: self.__showVenda(venda), pady=5)
                    botao_venda.grid(row=row_, column=11)

                    self.__labels_venda.append(label_venda)
                    self.__labels_venda.append(botao_venda)
                    row_ += 1
                return

            label_venda = Label(self.__root, text=venda_consulta)
            label_venda.grid(row=4, columnspan=10, padx=(25, 10))

            botao_venda = self.__botaoPadrao("Ver venda", lambda: self.__showVenda(venda_consulta), pady=5)
            botao_venda.grid(row=4, column=11)

            self.__labels_venda.append(label_venda)
            self.__labels_venda.append(botao_venda)

        Label(self.__root, text="Consultar Venda:").grid(row=0, column=0, pady=(10, 1), padx=0, sticky='w')
        opcoes_consulta = ["Id", "Funcionario ID", "Data"]
        menu = ttk.Combobox(self.__root, values=opcoes_consulta, state="readonly", width=15)
        menu.set("Id")
        menu.grid(row=1, column=1, pady=(0, 20))

        campo_consulta = Entry(self.__root, width=25, borderwidth=1)
        campo_consulta.grid(row=1, column=0, pady=(0, 20))

        self.__botaoPadrao("Consultar", consultar, pady=4).grid(row=1, column=2, pady=(0, 20))
        self.__botaoPadrao("Limpar", self.consultarVendasFarmacia, pady=4).grid(row=1, column=3, pady=(0, 20))
        self.__botaoPadrao("Voltar", self.interface, pady=4).grid(row=1, column=4, pady=(0, 20))

        row_ = 4
        for venda in vendas:
            label_venda = Label(self.__root, text=venda)
            label_venda.grid(row=row_, columnspan=10, padx=(25, 10))

            botao_venda = self.__botaoPadrao("Ver venda", lambda: self.__showVenda(venda), pady=5)
            botao_venda.grid(row=row_, column=11)

            self.__labels_venda.append(label_venda)
            self.__labels_venda.append(botao_venda)
            row_ += 1

        self.__root.mainloop()

    def consultarFuncionarios(self):
        from tkinter import ttk
        self.__inciarRoot(tamanho='700x300')
        self.__root.title('Consultar Funcionario')
        self.__temFarmacia()
        self.__usuarioTipoGerente()
        self.__labels_funcionarios = []

        funcionarios = self.__farmacia.getFuncionarios()
        if not funcionarios:
            Label(self.__root, text="Nenhuma funcionario foi cadastrado ainda.").grid(row=2, column=1, columnspan=2)

        def consultar():
            consulta_valor = campo_consulta.get()
            campo_consulta.delete(0,END)
            funcionarios_consulta = None
            funcionario_consulta = None

            if menu.get() == 'Id':
                self.__removerWidgets(self.__labels_funcionarios)
                try:
                    funcionario_consulta = self.__farmacia.getFuncionarioPorId(int(consulta_valor))
                except Exception as erro:
                    messagebox.showerror("Erro ao procurar por funcionario", f'{erro}')
                    self.consultarVendasFarmacia()
                    return
                
            elif menu.get() == 'Cargo':
                self.__removerWidgets(self.__labels_funcionarios)
                funcionarios_consulta = []
                for funcionario in self.__farmacia.getFuncionarios():
                    if funcionario.__class__.__name__ == consulta_valor:
                        funcionarios_consulta.append(funcionario)
                
            elif menu.get() == 'Nome':
                self.__removerWidgets(self.__labels_funcionarios)
                funcionarios_consulta = []
                for funcionario in self.__farmacia.getFuncionarios():
                    if (funcionario.nome).lower() == consulta_valor.lower():
                        funcionarios_consulta.append(funcionario)

            if (not funcionario_consulta) and (not funcionarios_consulta):
                messagebox.showerror("Erro ao procurar por funcionario", f'Funcionario com {menu.get()}:{consulta_valor} não existe.')
                self.consultarFuncionarios()
                return

            if funcionarios_consulta:
                row_ = 4
                for funcionario in funcionarios_consulta:
                    funcionario_label = Label(self.__root, text=funcionario)
                    funcionario_label.grid(row=row_, columnspan=10, padx=(25, 10))

                    botao_remover = self.__botaoPadrao("Excluir", lambda: self.__removerFuncionario(funcionario, funcionario_label, botao_remover), pady=5)
                    botao_remover.grid(row=row_, column=11)

                    self.__labels_funcionarios.append(funcionario_label)
                    self.__labels_funcionarios.append(botao_remover)
                    row_ += 1
                return

            funcionario_label = Label(self.__root, text=funcionario_consulta)
            funcionario_label.grid(row=4, columnspan=10, padx=(25, 10))

            botao_remover = self.__botaoPadrao("Excluir", lambda: self.__removerFuncionario(funcionario, funcionario_label, botao_remover), pady=5)
            botao_remover.grid(row=4, column=11)

            self.__labels_funcionarios.append(funcionario_label)
            self.__labels_funcionarios.append(botao_remover)

        Label(self.__root, text="Consultar Funcionario:").grid(row=0, column=0, pady=(10, 0), padx=0, sticky='w')
        opcoes_consulta = ["Id", "Cargo", "Nome"]
        menu = ttk.Combobox(self.__root, values=opcoes_consulta, state="readonly", width=15)
        menu.set("Id")
        menu.grid(row=1, column=1, pady=(0, 20))

        campo_consulta = Entry(self.__root, width=25, borderwidth=1)
        campo_consulta.grid(row=1, column=0, pady=(0, 20), padx=(10, 0))

        self.__botaoPadrao("Consultar", consultar, pady=4).grid(row=1, column=2, pady=(0, 20))
        self.__botaoPadrao("Limpar", self.consultarFuncionarios, pady=4).grid(row=1, column=3, pady=(0, 20))
        self.__botaoPadrao("Voltar", self.interface, pady=4).grid(row=1, column=4, pady=(0, 20))

        row_ = 4
        for funcionario in funcionarios:
            funcionario_label = Label(self.__root, text=funcionario)
            funcionario_label.grid(row=row_, columnspan=10, padx=(25, 10))

            botao_remover = self.__botaoPadrao("Excluir", lambda: self.__removerFuncionario(funcionario, funcionario_label, botao_remover), pady=5)
            botao_remover.grid(row=row_, column=11)

            self.__labels_funcionarios.append(funcionario_label)
            self.__labels_funcionarios.append(botao_remover)
            row_ += 1

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

    def perfilFuncionario(self):
        self.__inciarRoot(tamanho='600x400')
        self.__root.title("Meu Perfil")
        self.__temFarmacia()
        self.__autenticacaoValidacao()
        
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)

        self.__root.rowconfigure(0, weight=0)
        self.__root.columnconfigure(0, weight=0)
        row_base = 0
        column_base = 0

        self.__botaoPadrao('Voltar', self.interface, padx=5, pady=5).grid(row=row_base, column=column_base, sticky='W', padx=(10,0))
        
        Label(self.__root, text=f'Seu perfil - {funcionario.__class__.__name__}: {funcionario.nome}', font=('', 15)).grid(row=row_base, columnspan=5, column=column_base+1)
        

        Label(self.__root, text=f'Seus dados pessoais:', font=('', 12)).grid(row=row_base+1, column=column_base, columnspan=2, pady=(20, 0))
        Label(self.__root, text=f'ID: {funcionario.get_id()}').grid(row=row_base+2, column=column_base, sticky='W', padx=(20,0))
        Label(self.__root, text=f'Nome: {funcionario.nome}').grid(row=row_base+3, column=column_base, sticky='W', padx=(20,0))
        Label(self.__root, text=f'CPF: {funcionario.get_cpf()}').grid(row=row_base+4, column=column_base, sticky='W', padx=(20,0))
        Label(self.__root, text=f'Data Nascimento: {funcionario.get_data_nascimento().date()}').grid(row=row_base+5, column=column_base, sticky='W', padx=(20,0))

        Label(self.__root, text=f'Dados salarial:', font=('', 12)).grid(row=row_base+6, column=0, columnspan=2, pady=(20,0))
        Label(self.__root, text=f'Salário Base: R${funcionario.get_salario_base()}').grid(row=row_base+7, column=column_base, sticky='W', padx=(20,0))
        Label(self.__root, text=f'Bonus salarial: R${funcionario.get_bonus()}').grid(row=row_base+8, column=column_base, sticky='W', padx=(20,0))

        if self.__usuarioTipoGerente(messagemBox=False):
            Label(self.__root, text=f'Controle Farmácia:', font=('', 12)).grid(row=row_base+9, column=column_base, columnspan=2, pady=(20,5))
            Button(self.__root, text="Excluir Farmacia", command=self.__excluirFarmacia, pady=3, padx=5, bg='red', fg='white', font=('','10','bold')).grid(row=row_base+10, column=column_base, sticky='E')

        if self.__usuarioTipoAtendente(messagemBox=False):
            Label(self.__root, text=f'Comissões por vendas: R${funcionario.get_comissao()}').grid(row=row_base+9, column=column_base, sticky='W', padx=(20,0))

            vendas = funcionario.getVendasRealizadas()
            row_base += 1
            Label(self.__root, text=f'Suas Vendas (Total: {len(vendas)}):', font=('', 12)).grid(row=row_base, column=column_base+2, columnspan=2, pady=(20, 5))
            if vendas:
                for venda in vendas:
                    row_base += 1
                    Label(self.__root, text=f'Venda: Id={venda.getId()}| Data={venda.getDataVenda().date()}| Preço={venda.getPrecoTotal()}').grid(row=row_base, column=column_base+2, columnspan=4, sticky='W', padx=(0,0))
            else:
                Label(self.__root, text=f'Nenhuma Venda feita ainda.').grid(row=row_base+1, column=column_base+2, sticky='W', padx=(0,0))

        self.__root.mainloop()
        
    def __inciarRoot(self, tamanho = "500x300"):
        try:
            self.__root.destroy()
        except:
            pass
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.__salvarFarmacia)
        self.__root.geometry(tamanho)

    def __salvarFarmacia(self):
        salvar_farmacia(self.__farmacia)
        self.__root.destroy()
        return

    def __excluirFarmacia(self):
            verificacao = messagebox.askyesno("Excluir Farmácia", f"Você realmente deseja excluir Farmácia, {self.__farmacia.nome}?")

            if not verificacao:
                self.perfilFuncionario()
                return
            
            def excluir():
                try:
                    confirmacao = self.__farmacia.getGerente().setAutenticacao(self.__idFuncionarioLogado, campo_senha.get())
                except Exception as erro:
                    messagebox.showerror("Erro ao tentar confirmar senha.", f'{erro}')
                    return

                if confirmacao:
                    try:
                        excluir_farmacia()
                        self.__farmacia = None
                    except Exception as erro:
                        messagebox.showerror("Erro ao tentar exluir Farmácia.", f"{erro}")
                        self.perfilFuncionario()
                        return
                    self.interface()
                    return
                
                messagebox.showerror("Erro ao tentar exluir Farmácia.", f"Autenticação de Gerente falhou.")
                self.perfilFuncionario()
                return

            self.__inciarRoot(tamanho='250x150')
            self.__root.title("Excluir Farmácia")

            Label(self.__root, text="Confirme sua senha", font=("", '12', 'bold')).grid(row=0, column=0, columnspan=3, pady=(20,10))
            Label(self.__root, text="Senha:").grid(row=1, sticky="W", padx=(10, 0))
            campo_senha = Entry(self.__root, width='25', show="*")
            campo_senha.grid(row=1, column=1)

            Button(self.__root, text="Excluir", command=excluir, bg="red", fg="white", pady=2, font=('', '9', 'bold')).grid(row=2, column=1, sticky='W', pady=(10,0))
            Button(self.__root, text="Voltar", command=self.perfilFuncionario, pady=3, padx=10, font=('', '9', '')).grid(row=2, column=1, sticky='E',pady=(10,0))

            self.__root.mainloop()

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
            return
        return True

    def __dataRegex(self, data):
        import re
        data = re.sub(r'[-/\.]','', data)
        return data
        
    def __usuarioTipoGerente(self, messagemBox = True):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not funcionario.__class__.__name__ == 'Gerente':
            if messagemBox:
                messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Gerente para conseguir prosseguir.")
                self.__root.destroy()
                self.interface()
                return
            return False
        return True
    
    def __usuarioTipoAtendente(self, messagemBox = True):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not funcionario.__class__.__name__ == 'Atendente':
            if messagemBox:
                messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Atendente para conseguir prosseguir.")
                self.__root.destroy()
                self.interface()
                return
            return False
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
    
    def __usuarioTipoAtendenteOuRepositor(self, messagemBox = True):
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)
        if not (funcionario.__class__.__name__ == 'Repositor' or funcionario.__class__.__name__ == 'Atendente'):
            if messagemBox:
                messagebox.showerror("Erro de Autenticação", f"É preciso estar logado como Repositor ou Atendente para conseguir prosseguir.")
                self.__root.destroy()
                self.interface()
                return
            return False
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

    def __showVenda(self, venda):
        self.__inciarRoot()
        self.__root.title(f'Venda {venda.getId()}')
        self.__temFarmacia()
        self.__usuarioTipoGerente()
        
        self.__botaoPadrao("Voltar", self.consultarVendasFarmacia).grid(row=2, column=1)
        Label(self.__root, text=f"Id: {venda.getId()}").grid(row=3, column=1, sticky='w')
        Label(self.__root, text=f"Data da Venda: {venda.getDataVenda()}").grid(row=4, column=1, sticky='w')
        Label(self.__root, text=f"Funcionario: {venda.getFuncionario()}").grid(row=5, column=1, sticky='w')
        Label(self.__root, text=f"Cliente: {venda.getCliente()}").grid(row=6, column=1, sticky='w')
        Label(self.__root, text=f"Preço total: {venda.getPrecoTotal()}").grid(row=7, column=1, sticky='w')

        Label(self.__root, text=f"Produtos de venda:").grid(row=8, column=1, sticky='w', pady=(10, 0))
        row_ = 9
        for produto in venda.getProdutos():
            Label(self.__root, text=produto).grid(row=row_, column=1, sticky='w', padx=(10, 0))
            row_ += 1

        row_ += 1
        Label(self.__root, text=f"Log de alterações:").grid(row=row_, column=1, sticky='w', pady=(10, 0))
        for log in venda.getLogAlteracoes():
            row_ += 1  
            Label(self.__root, text=log).grid(row=row_, column=1, sticky='w', padx=(10, 0))
               
        self.__root.mainloop()

    def __removerFuncionario(self, funcionario, funcionario_label, botao_remover):
        verificacao = messagebox.askyesno("Remover Funcionario", f"Você realmente deseja remover funcionario, id={funcionario.get_id()}?")

        if not verificacao:
            self.consultarFuncionarios()
            return
        
        try:
            self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado).excluir_funcionario(funcionario)
        except Exception as erro:
            messagebox.showerror("Erro ao tentar remover Funcionario.", f"{erro}")
            self.consultarFuncionarios()

        try:
            funcionario_label.destroy()
            botao_remover.destroy()
        except:
            return
        
    def __atendenteRepositorPrimeiroAcesso(self, retornarBool = False):
        self.__temFarmacia()
        if not self.__usuarioTipoAtendenteOuRepositor(messagemBox=False):
            return
    
        funcionario = self.__farmacia.getFuncionarioPorId(self.__idFuncionarioLogado)

        def alterarSenha():
            try:
                funcionario.setNovaSenha(senha_antiga.get(), senha_nova.get())
            except Exception as erro:
                messagebox.showerror(f"Erro ao tentar alterar senha.", f'{erro}')
                return
            self.interface()
            return 

        if funcionario.get_senha(self.__farmacia) == funcionario.get_cpf():
            if retornarBool:
                return True
            
            self.__inciarRoot()
            self.__root.title("Alterar senha")
            self.__root.rowconfigure(0, weight=0)
            self.__root.columnconfigure(0, weight=0)

            Label(self.__root, text="Altere sua senha de primeiro acesso.", font=('',10,'')).grid(row=0, column=0, columnspan=2, sticky='W')
            Label(self.__root, text="Senha Antiga:").grid(row=1, column=0,sticky='W', pady=(5,2))
            Label(self.__root, text="Senha Nova:").grid(row=2, column=0,sticky='W',pady=(0,2), padx=(0, 1))

            senha_antiga = Entry(self.__root, show='*', width=25, borderwidth=1)
            senha_antiga.grid(row=1, column=1,sticky='E',pady=(5,2))
            senha_nova = Entry(self.__root, show='*', width=25, borderwidth=1)
            senha_nova.grid(row=2, column=1,sticky='E',pady=(0,2))

            self.__botaoPadrao("Alterar", alterarSenha).grid(row=3, column=1)

            self.__root.mainloop()


        
    

    

    