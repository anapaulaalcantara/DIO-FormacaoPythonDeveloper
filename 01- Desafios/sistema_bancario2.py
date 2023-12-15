'''
Sistema Bancário Simplificado

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

Sistema Bancário Otimizado 
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

->>> Novas funcionalidades

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


'''
# ============Funções============
# 1- Depositar
def depositar(valor_deposito):
    """
    Realiza um depósito na conta bancária.

    Parâmetros:
    - valor_deposito (float): O valor a ser depositado na conta.

    Retorna:
    - float: O saldo atualizado após o depósito.

    A função verifica se o valor do depósito é maior que zero. Se for,
    atualiza o saldo da conta, registra o depósito no histórico e imprime
    uma mensagem de sucesso. Caso contrário, exibe uma mensagem de erro
    indicando que a operação não foi realizada devido a um valor inválido.
    """
    global saldo

    if valor_deposito > 0:
        # Adiciona o valor do depósito ao histórico
        transacao_deposito = f"Depósito: R$ {valor_deposito:.2f}\n"
        extrato.append(transacao_deposito)

        # Atualiza o saldo da conta
        saldo += valor_deposito

        # Imprime mensagem de sucesso
        print(f"Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso.")

        # Retorna o saldo atualizado
        return saldo, extrato
    
    else:
        # Exibe mensagem de erro para valor inválido
        print("Operação não realizada.\nValor inválido.\nO valor deve ser maior que 0.")


# 2-Sacar
def sacar(valor_saque):
    """
    Realiza um saque na conta bancária.

    Parâmetros:
    - valor_saque (float): O valor a ser sacado da conta.

    Retorna:
    - tuple: Uma tupla contendo o saldo atualizado após o saque e a transação.
    """
    global saldo, extrato, limite_por_saque, numero_saques, LIMITE_NUMERO_SAQUES
    
    
    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_por_saque and numero_saques < LIMITE_NUMERO_SAQUES:
        # Adiciona o valor do saque ao histórico como uma tupla
        transacao_saque = f"Saque: R$ {valor_saque:.2f}\n"
        extrato.append(transacao_saque)

        # Atualiza o saldo da conta
        saldo -= valor_saque

        # Incrementa o número de saques
        numero_saques += 1

        # Imprime mensagem de sucesso
        print(f"Saque de R$ {valor_saque:.2f} foi realizado com sucesso.")

        # Verifica se atingiu o limite de saques
        if numero_saques == LIMITE_NUMERO_SAQUES:
            print("Limite de saques diários atingido.")

        # Retorna o saldo atualizado e a transação
        return saldo, extrato
    else:
        # Exibe mensagem de erro para valor inválido ou saldo insuficiente
        print("Operação não realizada.\n")
        if valor_saque <= 0:
            print("O valor do saque deve ser maior que 0.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_por_saque:
            print("O valor do saque excede o limite por saque.")
        elif numero_saques == LIMITE_NUMERO_SAQUES:
            print("Limite de saques diários atingido.")


# 3-Extrato
def extrato_detalhado(extrato):    
    print(" EXTRATO ".center(40, "="))
    if not extrato:
        print("\nNão foram realizadas movimentações no período.")
    else: 
        for valor in extrato:
            print(valor)
    print("=".center(40, "="))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(40, "="))


menu = '''

Escolha uma opção:

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

'''

saldo = 30 
extrato = []
depositos = []
limite_por_saque = 500
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:

    opcao = input(menu)

    # 1-Deposito
    if opcao == "1": 
       
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        depositar(valor_deposito)

    # 2-Saque
    elif opcao == "2":

        valor_saque = float(input(f"Limite por saque é R$ {limite_por_saque:.2f}\nInforme o valor do saque: R$ "))
        sacar(valor_saque)


    # 3-Extrato
    elif opcao == "3": # Extrato
        extrato_detalhado(extrato)

    # 4-Sair
    elif opcao == "4": # Sair
        break
    
    # Opção invalida
    else:
        print("Operação inválida.\nPor favor selecione a operação desejada.")
