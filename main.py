from system import deposito, saque, extrato, cadastrar_usuario, criar_cc, buscar_usuario

menu = '''
ESCOLHA A SUA OPÇÃO:
SAQUE                   [S]
DEPÓSITO                [D]
EXTRATO                 [E]
CADASTRAR USUARIO       [C]
CADASTRAR CONTA         [X]
SAIR                    [Q]
=> '''

saldo = 0
limite = 500
numero_saques=0
usuarios = []
contas = []

LIMITE_SAQUES=3


saques = []
depositos = []

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        saldo = deposito(saldo, depositos)

    if opcao == "s" or opcao == "S":
        saldo = saque(saldo = saldo, saques = saques, numero_saques = numero_saques)

    if opcao == "e" or opcao == "E":
        extrato(saques, depositos = depositos)

    if opcao == "c" or opcao == "C":
        cadastrar_usuario(usuarios)

    if opcao == "x" or opcao == "X":
        criar_cc(contas=contas, usuarios=usuarios)
        print(contas)

    if opcao == "q" or opcao == "Q":
        break;
