# 💊 Sistema de Gerenciamento Farmacêutico

Projeto acadêmico desenvolvido para a disciplina de **Programação Orientada a Objetos (POO) com Python** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

O sistema simula o funcionamento de uma farmácia, aplicando conceitos fundamentais de POO como **herança, encapsulamento, abstração e polimorfismo**, além de utilizar **Mixins** para organização de funcionalidades e **Pickle** para persistência de dados.

---

## 📚 Objetivo do Projeto

Desenvolver um sistema de gerenciamento farmacêutico com foco educacional, aplicando corretamente os princípios da Programação Orientada a Objetos em Python, por meio de um projeto prático e bem estruturado.

---

## 🧑‍💻 Equipe
- **Nicolas Raony** – Desenvolvimento e apoio (.[GitHub](https://github.com/NicolasRaony06))
- **Francisco Álvaro** – Desenvolvimento e apoio ([GitHub](https://github.com/rootAlvim))  
- **Artur Fernandes** – Desenvolvimento e apoio ([GitHub](https://github.com/Aruturiz))

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Tkinter** (interface gráfica)
- **Git & GitHub**
- Paradigma **POO**

---

## 📁 Estrutura do Projeto

```text
sistema-de-gerenciamento-farmaceutico/
│
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── pessoa.py
│   │   ├── funcionario.py
│   │   ├── atendente.py
|   |   ├── repositor.py
│   │   ├── gerente.py
│   │   ├── cliente.py
│   │   ├── interface.py
│   │   └── mixins_interfaces/
│   │       ├── funcionalidades_gerente.py
│   │       ├── gerenciar_estoque.py
│   │       └── gerenciar_venda.py
│   │
│   ├── interface_tkinter/
│   │   ├── main.py
│   │   └── interface.py
│   │
│   ├── farmacia/
│   │   ├── farmacia.py
│   │   ├── estoque.py
│   │   ├── produto.py
│   │   └── venda.py
│   │
│   └── utils/
│       ├── gerador_id.py
│       └── validacoes.py
│
├── tests/
│   ├── test_farmacia.py
│   ├── test_estoque.py
│   ├── test_produto.py
│   ├── test_funcionario.py
│   ├── test_gerente.py
│   └── test_venda.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Funcionalidades Implementadas

### 👤 Pessoas e Usuários
- Cadastro de clientes
- Funcionários com hierarquia (Gerente, Atendente e Repositor)
- Sistema de autenticação simples

### 📦 Produtos e Estoque
- Cadastro de produtos
- Controle de estoque
- Validações de dados
- Atualização de quantidades

### 🛒 Vendas
- Registro de vendas
- Associação de cliente e funcionário
- Cálculo de valor total
- Baixa automática no estoque

### 🏪 Farmácia
- Classe central que gerencia:
  - Estoque
  - Produtos
  - Funcionários
  - Clientes
  - Vendas

## 🖥️ Interface e Funcionalidades (Tkinter)

A interface gráfica, localizada em `src/interface_tkinter/`, é o ponto central de interação com o sistema.

### 🔑 Autenticação e Primeiro Acesso
- **Sistema de Login:** Acesso restrito baseado em credenciais de funcionários cadastrados.
- **Configuração Inicial:** O sistema identifica se não há dados salvos e solicita o cadastro do primeiro Gerente para administrar a farmácia.

### 🛡️ Gestão e Governança (Painel do Gerente)
O Gerente possui permissões administrativas exclusivas dentro da interface:
- **Logs do Sistema:** Visualização de um histórico detalhado de alterações críticas e movimentações na farmácia.
- **Sistema de Chamados:** Gestão de solicitações e alertas enviados por Atendentes e Repositores diretamente pela interface.
- **Gestão de Pessoal:** Controle total sobre o cadastro, exclusão e bonificação de funcionários.

### 📦 Persistência de Dados com Pickle
Para evitar a perda de dados ao fechar a aplicação, utilizamos o módulo **Pickle**. 
- Toda a estrutura do objeto `Farmacia` (que compõe estoque, vendas, clientes e funcionários) é serializada.
- Ao iniciar o `main.py`, o sistema verifica a existência de um arquivo de dados para restaurar o estado anterior da aplicação.

---

## 🧠 Conceitos de POO Aplicados

✔️ **Encapsulamento**  
✔️ **Herança** (`Pessoa → Funcionario → Gerente / Atendente / Repositor`)  
✔️ **Polimorfismo**  
✔️ **Abstração:** Uso de classes e métodos abstratos para padronizar o comportamento das entidades.                                                                                       ✔️ **Mixins:** Implementação de `GerenciarEstoqueMixin` e `GerenciarVendaMixin` para modularizar comportamentos específicos.   
✔️ **Composição** (Farmácia → Estoque, Funcionários, Vendas)  
✔️ **Separação de responsabilidades**  
✔️ **Organização modular do projeto**

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/NicolasRaony06/sistema-de-gerenciamento-farmaceutico.git
```

2. Acesse o diretório:
```bash
cd sistema-de-gerenciamento-farmaceutico
```

3. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o sistema:
```bash
python -m src.interface_tkinter.main
```

---

## 🚀 Melhorias Futuras

- Evolução da interface gráfica
- Banco de Dados: Transição do Pickle para um banco de dados relacional (SQLite/PostgreSQL).
- Testes Automatizados: Refatoração e implementação de suíte de testes completa utilizando Pytest para garantir a cobertura das regras de negócio.
- Relatórios: Geração de arquivos PDF com o fechamento de vendas e inventário de estoque.

---

## 📄 Licença

Projeto desenvolvido **exclusivamente para fins acadêmicos**.

---

## 📌 Observações Finais

Este projeto foi desenvolvido com foco em **aprendizado prático de POO**, seguindo boas práticas de organização, testes e versionamento, sendo totalmente adequado para avaliação acadêmica e evolução futura.

