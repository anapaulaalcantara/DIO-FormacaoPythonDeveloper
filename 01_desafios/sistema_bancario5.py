'''
Sistema Bancário Simplificado (sistema_bancario1.py)

1-depósito
    valores positivos
    armazenado em uma variável e exibidos no extrato
2-saque
    3 saques diários
    limite maximo de R$500 por saque
    caso saldo < saque "Saldo insuficiente para realizar o saque."    
    armazenado em uma variável e exibidos no extrato          
3-extrato
    listar todos depositos e saques
    no final exibir saldo atual R$xxx.xx

Sistema Bancário Otimizado (sistema_bancario2.py)
->>> Otimização
1-Criar função depositar
    argumentos (position only)
    retorno: saldo, extrato

2-Cria fução sacar
    argumentos (keyword only)
    retorno: saldo, extrato

3-Criar função extrato
    argumentos (position only, keywordonly)
        positon only: saldo
        keyword only: extrato

==============================================================================================
->>> Novas funcionalidades (sistema_bancario5.py)

4-cadastrar usuário (cliente)
    armazenar os usuários em uma lista
    usuário: nome, data de nascimento, cpf, endereço
        endereço = string no formato (logradouro, numero - bairro - cidade/sigla_estado)
        cpf = string(apenas numeros)
        apenas um usuário por cpf

5-cadastrar conta bancária (vincular com o usuário)
    armazenar contas em uma lista
    conta: agência, número da conta, usuário
        numero da conta: é sequencial, iniciando em 1
        número da agencia: fixo "0001"
        *** O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    vincular um usuário a uma conta, flitre a lista de usuários bucando o número de cpf

==============================================================================================
'''

import textwrap

def menu():
    menu = """\n
    ================= MENU =================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Novo Usuário
    [5] Cadastrar Nova Conta
    [6] Listar Contas
    [7] Sair
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
        if usuario['cpf'] == cpf:
            print("xXx Já existe um usuário cadastrado com este CPF. xXx\nNão é permitido cadastrar o mesmo CPF novamente.")
            return

    # Adicionar o novo usuário à lista de usuários
    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--> Usuário cadastrado com sucesso!")


def cadastrar_conta(lista_contas, lista_usuarios):
    AGENCIA = "0001"
    # Solicitar CPF até que seja fornecido um válido (apenas números e tamanho 11)
    while True:
        cpf = input("Digite o CPF do titular da conta (apenas números): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("xXx CPF inválido xXx. Digite apenas números e certifique-se de ter 11 dígitos.")

    # Verificar se o usuário com o CPF informado existe
    usuario_encontrado = None
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("\nxXx Usuário não encontrado xXx\nNão é possível cadastrar uma conta sem um usuário associado.")
        return

    # Criar a conta
    numero_conta = len(lista_contas) + 1  # Número sequencial iniciando em 1
        
    # Vincular o usuário à conta
    conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario_encontrado}
    
    # Adicionar a nova conta à lista de contas
    lista_contas.append(conta)

    print(f"--> Conta cadastrada com sucesso! Número da conta: {numero_conta}")
    

def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))


def main():
    
    
    lista_contas = []
    saldo = 30 
    extrato = []
    limite_por_saque = 500
    numero_saques = 0
    LIMITE_NUMERO_SAQUES = 3
    lista_usuarios = []

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
            cadastrar_usuario(lista_usuarios)

        elif opcao == "5":
            #numero_conta = len(contas) + 1
            #conta = criar_conta(AGENCIA, numero_conta, usuarios)
            cadastrar_conta(lista_contas, lista_usuarios)

        elif opcao == "6":
            listar_contas(lista_contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()