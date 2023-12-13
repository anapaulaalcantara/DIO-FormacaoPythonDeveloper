def depositar(valor_deposito, saldo, extrato):
    if valor_deposito > 0:
        transacao_deposito = f"Depósito: R$ {valor_deposito:.2f}\n"
        extrato.append(transacao_deposito)
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso.")
        return saldo, extrato
    else:
        print("Operação não realizada.\nValor inválido.\nO valor deve ser maior que 0.")
        return saldo, extrato

def sacar(valor_saque, saldo, extrato, limite_por_saque, numero_saques, LIMITE_NUMERO_SAQUES):
    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_por_saque and numero_saques < LIMITE_NUMERO_SAQUES:
        transacao_saque = f"Saque: R$ {valor_saque:.2f}\n"
        extrato.append(transacao_saque)
        saldo -= valor_saque
        numero_saques += 1
        print(f"Saque de R$ {valor_saque:.2f} foi realizado com sucesso.")
        if numero_saques == LIMITE_NUMERO_SAQUES:
            print("Limite de saques diários atingido.")
        return saldo, extrato, numero_saques
    else:
        print("Operação não realizada.")
        if valor_saque <= 0:
            print("O valor do saque deve ser maior que 0.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_por_saque:
            print("O valor do saque excede o limite por saque.")
        elif numero_saques == LIMITE_NUMERO_SAQUES:
            print("Limite de saques diários atingido.")
        return saldo, extrato, numero_saques

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
limite_por_saque = 500
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        saldo, extrato = depositar(valor_deposito, saldo, extrato)
    elif opcao == "2":
        valor_saque = float(input(f"Limite por saque é R$ {limite_por_saque:.2f}\nInforme o valor do saque: R$ "))
        saldo, extrato, numero_saques = sacar(valor_saque, saldo, extrato, limite_por_saque, numero_saques, LIMITE_NUMERO_SAQUES)
    elif opcao == "3":
        extrato_detalhado(extrato)
    elif opcao == "4":
        break
    else:
        print("Operação inválida.\nPor favor, selecione a operação desejada.")
