from abc import ABC, abstractclassmethod, abstractproperty
import datetime as dt

contas = [] 


class Cliente:
    def __init__(self, endereco, contas = []):
        self._endereco  = endereco
        self._contas    = contas

    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
        pass


    def adicionar_conta(self, cliente, contas):
        conta = ContaCorrente.nova_conta(cliente, contas)
        self._contas.append(conta) # type: ignore

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        return (f'''
        Class_name: {__class__.__name__}
        CPF: {self._cpf}
        Nome: {self._nome}
        Nascimento: {self._data_nascimento}
        Endereço: {self._endereco}
        ''')

class Conta:

    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
        self._valor_limite_saque = 0
        self._limite_de_saques = 0

    def __str__(self):
        return (f'''
        Saldo inicial: R$ {self._saldo}
        CPF: {self._cliente._cpf}
        Agência: {self._agencia}
        Conta-Corrente: {self._numero}
        Limite de saques: {self._limite_de_saques}
        Valor máximo para saques: {self._valor_limite_saque}
        ''')
    
    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, PessoaFisica, contas):
        conta = ContaCorrente(3,500,0, (len(contas)+1), "0001", PessoaFisica, [])
        contas.append(conta)
        PessoaFisica._contas.append(conta)
        return conta

    def sacar(self, valor):
        self._saldo -= valor
        return True


    def depositar(self, valor):
        self._saldo += valor
        return True

class ContaCorrente(Conta):
    def __init__(self, limite_de_saques, valor_limite_saque, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite_de_saques = 3
        self._valor_limite_saque = 500
        self._numero_saques = 0

    def sacar(self, valor):

        excedeu_limite = valor > self._valor_limite_saque
        excedeu_saques = self._numero_saques > (self._limite_de_saques - 1)
        saldo_negativo = self._saldo < valor

        if excedeu_limite:
            print("Valor limite de saque excedido")
            return False

        elif excedeu_saques:
            print("Quantidade de saques excedido")
            return False

        elif saldo_negativo:
            print("Saldo insuficiente!")
            return False

        else: 
            super().sacar(valor)
            print("Saque realizado com sucesso!")
            self._numero_saques +=1
            return True


    def depositar(self, valor):
        if valor>0: 
            super().depositar(valor)
            print("Depósito realizado com Sucesso!")
            print(f"Saldo atual: R$ {self._saldo:.2f} ")
            return True

        else: 
            print("Valor invalido. Tente novamente")
            return False

class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

    def __str__(self):
        output = "\n"

        for transacao in self._transacoes:
            output += f"Data: {transacao['data']}\n"
            output += f"Tipo: {transacao['tipo']}\n"
            output += f"Valor: R$ {transacao['valor']:.2f}\n\n" 

        return output          

class Transacao(ABC):
    
    @property # type: ignore
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)

class MainMenu:

    @classmethod
    def criar_usuario(cls, usuarios):
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome do cliente: ")
        nasc = input("Digite a data de nascimento: ")
        end = input("Digite o endereço: ")

        usuarios.append(PessoaFisica(cpf,nome,nasc,end))

        print(f'''

        Usuário criado!

        Dados

        Nome: {nome}
        CPF: {cpf}
        Nascimento: {nasc}
        Endereço: {end}

        ''')
    @classmethod
    def bu(cls, usuarios):
        cpf = input("Digite o CPF do titular da conta: ")
        
        for indice, usuario in enumerate(usuarios):
            if usuarios[indice]._cpf == cpf: 
                return indice

            else: 
                print("CPF não encontrado na base de dados...")
        return -1
        
    @classmethod
    def cc(cls, usuario, contas):
        
        indice = MainMenu.bu(usuario)
        MainMenu.criar_conta(usuario[indice],contas)
                

    
    @classmethod
    def criar_conta(cls, usuario, contas):
        tmp = ContaCorrente.nova_conta(usuario, contas)
        print(f'''

        Conta criada com sucesso!

        CPF titular: {usuario._cpf}
        Agência: {tmp._agencia}
        C/C: {tmp._numero:04}

        ''')

    @classmethod
    def extrato(cls, usuario):
        i_usuario = MainMenu.bu(usuario)
        numero_contas = len(usuario[i_usuario]._contas)


        print(f"O usuario possui {numero_contas} conta(s).")
        print(usuario[i_usuario]._contas)
        for i in range(numero_contas):
            print(f"{(i+1)} - {(usuario[i_usuario]._contas[i]._numero):04}")

        i_conta = int(input("Escolha a conta => "))
        i_conta -= 1

        print(i_conta)


        print(usuario[i_usuario]._contas[i_conta])
        nao_tem_conta = numero_contas<=0
        extrato_zerado =  len(usuario[i_usuario]._contas[i_conta]._historico._transacoes) == 0



        if extrato_zerado and nao_tem_conta==False:
            print(f'''
            EXTRATO BANCÁRIO

            Saldo atual: R$ {usuario[i_usuario]._contas[i_conta]._saldo:.2f}

            Não há movimentações atuais...
            ''')
        
        elif nao_tem_conta:
            print(f"Contas não encontradas para o CPF {usuario[i_usuario]._cpf}")


        else:
            print('''
            EXTRATO BANCÁRIO

            ''')
            print(usuario[i_usuario]._contas[i_conta]._historico)
        
    @classmethod
    def saque(cls, usuarios):
        print("SAQUE: ")
        i_usuario = int(MainMenu.bu(usuarios))
        i_conta= int(input("Digite o numero da conta (Apenas o digito, sem os Zeros à Esquerda: "))
        valor = float(input("Digite o valor da operação:"))
        tmp = Saque(valor)
        tmp.registrar(usuarios[i_usuario]._contas[i_conta])

    @classmethod
    def deposito(cls, usuarios):
        print("DEPOSITO: ")
        i_usuario = int(MainMenu.bu(usuarios))
        i_conta= int(input("Digite o numero da conta (Apenas o digito, sem os Zeros à Esquerda: )"))
        valor = float(input("Digite o valor da operação:"))
        tmp = Deposito(valor)
        tmp.registrar(usuarios[i_usuario]._contas[i_conta-1])
        