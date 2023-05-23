from classes import MainMenu as mn

menu = '''
ESCOLHA A SUA OPÇÃO:
SAQUE                   [S]
DEPÓSITO                [D]
EXTRATO                 [E]
CADASTRAR USUARIO       [C]
CADASTRAR CONTA         [X]
SAIR                    [Q]
=> '''

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        mn.deposito(usuarios)

    if opcao == "s" or opcao == "S":
        mn.saque(usuarios)

    if opcao == "e" or opcao == "E":
        mn.extrato(usuarios)
       
    if opcao == "c" or opcao == "C":
        mn.criar_usuario(usuarios) 

    if opcao == "x" or opcao == "X":
        mn.cc(usuarios, contas)
       
    if opcao == "q" or opcao == "Q":
        break
       
