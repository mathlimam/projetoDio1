def deposito(saldo, depositos, /):
    while True:
        tmp = input("Digite o valor do depósito => ")
        tmp = float(tmp)
        if tmp >= 0: break
        else:print("Valor invalido")
    depositos.append(tmp)
    saldo+=tmp
    print(f"Deposito realizado com sucesso. Seu saldo agora é de R$ {saldo}")
    
    return saldo

def saque(*, saldo, saques, numero_saques):
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

    return saldo

def extrato(saques, *,depositos):
    somasaque = 0
    somadeposito = 0

    print("extrato bancário".center(20), end="\n\n")
    print("")
    print("Saques:")
    for i in range(len(saques)):
        somasaque += saques[i]
        print(f"{i+1}. -R$ {saques[i]:,.2f}")
    print(end="\n")
    print("Depósitos: ")
    for i in range(len(depositos)):
        somadeposito += depositos[i]
        print(f"{i+1}. R$ {depositos[i]:,.2f}")

    print(f"total de Depósitos => R$ {somadeposito:,.2f}".center(20))
    print(f"total de Saques => -R$ {somasaque:,.2f}")
    print(f"saldo final => R$ {(somadeposito - somasaque):,.2f}")    
    return

def cadastrar_usuario(usuarios):
    print(" TELA DE CADASTRO", end="\n\n")
    while True:
        cpf = int(input("Digite seu cpf => "))
        if cpf in [usuario[0] for usuario in usuarios]: print("CPF já cadastrado.")
        else: 
            nome = input("Digite seu nome => ")
            data_nascimento = input("Digite sua data de nascimento => ")
            print("Endereço:")
            logradouro = input("Digite o logradouro => ")
            nro = input("Digite o número => ")
            bairro = input("Digite o bairro => ")
            cidade = input("Digite a cidade => ") 
            uf = input("Digite o estado => ")
            endereco = f"{logradouro} - {nro} - {bairro} - {cidade}/{uf}"
            break

    usuarios.append([cpf,nome,data_nascimento,endereco])

    return usuarios

def criar_cc(contas, usuarios):
    ag = "0001"
    cc = len(contas) + 1
    while True:
        cpf = input("Digite o cpf => ")
        vd = buscar_usuario(usuarios, cpf)
        if vd == False : break
    contas.append([cpf, ag, cc])
    return contas

def buscar_usuario(usuarios, cpf):

    for usuario in usuarios:
        if cpf == usuario[0]:
            return True
    return False


