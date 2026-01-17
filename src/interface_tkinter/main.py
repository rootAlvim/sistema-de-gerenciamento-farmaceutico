# python -m src.interface_tkinter.main

from src.interface_tkinter.interface import Interface

interface = Interface()

escolha = 1
while escolha > 0:
    escolha = int(input("Escolha: "))

    if escolha == 1:
        interface.registrarFarmacia()
        
    elif escolha == 2:
        print(interface.farmacia.nome)

    elif escolha == 3:
        interface.registrarAtendente()

    elif escolha == 4:
        print(interface.farmacia.getFuncionarios())

    elif escolha == 5:
        interface.registrarGerente()

    elif escolha == 6:
        print(interface.farmacia.getGerente())