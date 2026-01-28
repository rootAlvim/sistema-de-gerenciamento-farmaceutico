# 💊 Sistema de Gerenciamento Farmacêutico

Projeto acadêmico desenvolvido para a disciplina de **Programação Orientada a Objetos (POO) com Python** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

O sistema simula o funcionamento básico de uma farmácia, aplicando conceitos fundamentais de POO como **herança, encapsulamento, abstração, polimorfismo**, além de **interfaces, mixins, organização modular e testes automatizados**.

---

## 📚 Objetivo do Projeto

Desenvolver um sistema de gerenciamento farmacêutico com foco educacional, aplicando corretamente os princípios da Programação Orientada a Objetos em Python, por meio de um projeto prático e bem estruturado.

---

## 🧑‍💻 Equipe

- **Nicolas Raony** – Desenvolvedor e mantenedor do repositório  
- **Francisco Alvaro** – Desenvolvimento e apoio ([GitHub](https://github.com/rootAlvim))  
- **Arthur Fernades** – Desenvolvimento e apoio ([GitHub](https://github.com/Aruturiz))

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Tkinter** (interface gráfica)
- **Pytest** (testes automatizados)
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
│   │   └── produto.py
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
- Funcionários com hierarquia (Atendente e Gerente)
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

### 🖥️ Interface Gráfica (Tkinter)
- Implementação gráfica simples utilizando **Tkinter**
- Interface localizada em `src/core/interface.py`
- Permite interação básica com o sistema sem uso do terminal

---

## 🧠 Conceitos de POO Aplicados

✔️ **Encapsulamento**  
✔️ **Herança** (`Pessoa → Funcionario → Gerente / Atendente`)  
✔️ **Polimorfismo**  
✔️ **Abstração** (classe abstrata `Pessoa` e interfaces)  
✔️ **Interfaces** (`FuncionalidadesGerente`)  
✔️ **Mixins** (`GerenciarEstoqueMixin`, `GerenciarVendaMixin`)  
✔️ **Composição** (Farmácia → Estoque, Funcionários, Vendas)  
✔️ **Separação de responsabilidades**  
✔️ **Organização modular do projeto**

---

## 🧪 Testes Automatizados

O projeto utiliza **Pytest** para garantir a confiabilidade das regras de negócio.

### Executar os testes:

```bash
pytest
```

Os testes cobrem:
- Produtos
- Estoque
- Funcionários
- Gerente
- Vendas
- Farmácia

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
python src/main.py
```

---

## 🚀 Melhorias Futuras

- Evolução da interface gráfica
- Persistência em banco de dados
- Relatórios de vendas
- Sistema de login com níveis de acesso
- API REST
- Documentação automática

---

## 📄 Licença

Projeto desenvolvido **exclusivamente para fins acadêmicos**.

---

## 📌 Observações Finais

Este projeto foi desenvolvido com foco em **aprendizado prático de POO**, seguindo boas práticas de organização, testes e versionamento, sendo totalmente adequado para avaliação acadêmica e evolução futura.

