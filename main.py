

menu = '''
ESCOLHA A SUA OPÇÃO:
SAQUE           [S]
DEPÓSITO        [D]
EXTRATO         [E]
SAIR            [Q]

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques=0
LIMITE_SAQUES=3

saques = []
depositos = []

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        while True:
            tmp = input("Digite o valor do depósito => ")
            tmp = float(tmp)
            if tmp >= 0: break
            else:print("Valor invalido")
        depositos.append(tmp)
        saldo += (tmp)
        print(f"Deposito realizado com sucesso. Seu saldo agora é de R$ {saldo}")

    if opcao == "s" or opcao == "S":
        if numero_saques<=2:
            while True:
                tmp = input("Digite o valor do saque (limite máximo de R$ 500,00 p/ saque => ")
                tmp = float(tmp)
                if tmp <= 500 and tmp >=0: break
                else:print("Valor invalido")
            saques.append(tmp)
            saldo -= tmp
            numero_saques +=1
            print(f"Saque realizado com sucesso. Seu saldo agora é de R$ {saldo}")
        else: print("limite de saque diario atingido")
            

    if opcao == "e" or opcao == "E":
        somasaque = 0
        somadeposito = 0
        print("extrato bancário".center(20))
        print("")
        print("Saques:")
        for i in range(len(saques)):
            somasaque += saques[i]
            print(f"{i+1}. -R$ {saques[i]:,.2f}")
        print("")
        print("Depósitos")
        for i in range(len(depositos)):
            somadeposito += depositos[i]
            print(f"{i+1}. R$ {depositos[i]:,.2f}")

        print(f"total de Depósitos => R$ {somadeposito:,.2f}".center(20))
        print(f"total de Saques => -R$ {somasaque:,.2f}")
        print(f"saldo final => R$ {(somadeposito - somasaque):,.2f}")

    if opcao == "q" or opcao == "Q":
        break;


