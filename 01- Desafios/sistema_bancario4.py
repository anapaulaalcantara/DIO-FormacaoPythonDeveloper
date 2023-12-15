import textwrap

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"Usuário: {self.nome} - CPF: {self.cpf} - Endereço: {self.endereco}"

def cadastrar_usuario(lista_usuarios):
    nome = input("Digite seu nome completo (sem abreviações): ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
    
    # Solicitar CPF até que seja fornecido um válido (apenas números e tamanho 11)
    while True:
        cpf = input("Digite o CPF (apenas números): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("xXx CPF inválido xXx. Digite apenas números e certifique-se de ter 11 dígitos.")

    endereco = input("Digite o endereço (logradouro, número - Bairro - Cidade/sigla_estado): ")

    # Verificar se já existe um usuário com o mesmo CPF
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            print("xXx Já existe um usuário cadastrado com este CPF. xXx\nNão é permitido cadastrar o mesmo CPF novamente.")
            return

    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)

    # Adicionar o novo usuário à lista de usuários
    lista_usuarios.append(novo_usuario)

    print("--> Usuário cadastrado com sucesso!")


def menu():
    menu = """\n
    ================= MENU =================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Novo Usuário
    [5] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(valor_deposito, saldo, extrato, /):
    if valor_deposito > 0:
        transacao_deposito = f"Depósito: R$ {valor_deposito:.2f}\n"
        extrato.append(transacao_deposito)
        saldo += valor_deposito
        print(f"\n--> Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso.")
    
    else:
        print("\nxXx Operação não realizada xXx.\nValor inválido.\nO valor deve ser maior que 0.")
    
    return saldo, extrato

def sacar(*, valor_saque, saldo, extrato, limite_por_saque, numero_saques, LIMITE_NUMERO_SAQUES):
    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_por_saque and numero_saques < LIMITE_NUMERO_SAQUES:
        transacao_saque = f"Saque: R$ {valor_saque:.2f}\n"
        extrato.append(transacao_saque)
        saldo -= valor_saque
        numero_saques += 1
        print(f"\n--> Saque de R$ {valor_saque:.2f} foi realizado com sucesso.")
        if numero_saques == LIMITE_NUMERO_SAQUES:
            print("\nAtenção: Limite de saques diários atingido.")
        
    else:
        print("\nxXx Operação não realizada xXx.")
        if valor_saque <= 0:
            print("O valor do saque deve ser maior que 0.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_por_saque:
            print("O valor do saque excede o limite por saque.")
        elif numero_saques == LIMITE_NUMERO_SAQUES:
            print("Limite de saques diários atingido.")
    
    return saldo, extrato, numero_saques

def extrato_detalhado(saldo, /, *, extrato):    
    print(" EXTRATO ".center(40, "="))
    if not extrato:
        print("\nNão foram realizadas movimentações no período.")
    else: 
        for valor in extrato:
            print(valor)
    print("=".center(40, "="))
    print(f"Saldo: R$ {saldo:.2f}")
    print("".center(40, "="))


def main():

    saldo = 30 
    extrato = []
    limite_por_saque = 500
    numero_saques = 0
    LIMITE_NUMERO_SAQUES = 3
    lista_de_usuarios = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor_deposito = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(valor_deposito, saldo, extrato)

        elif opcao == "2":
            # cabeçalho
            print(" Informaçoes ".center(40, "="))
            print(f"Saldo disponível  R$ {saldo:.2f}")
            print(f"Limite por saque  R$ {limite_por_saque:.2f}")
            print("=".center(40, "="))

            valor_saque = float(input("\nInforme o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                valor_saque=valor_saque,
                saldo=saldo,
                extrato=extrato,
                limite_por_saque=limite_por_saque,
                numero_saques=numero_saques,
                LIMITE_NUMERO_SAQUES=LIMITE_NUMERO_SAQUES,
            )

        elif opcao == "3":
            extrato_detalhado(saldo, extrato=extrato)

        elif opcao == "4":
            cadastrar_usuario(lista_de_usuarios)

        elif opcao == "5":
            break

        else:
            print("xXx Operação inválida xXx.\nPor favor, selecione a operação desejada.")

main()