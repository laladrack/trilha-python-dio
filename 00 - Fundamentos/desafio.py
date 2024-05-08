#declarar o menu principal
menu = """
-----------------
Menu de Operações
-----------------
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
-----------------"""

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
      
def sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato, /):
        if (valor > saldo):
                print("Operação falhou! Você não tem saldo suficiente.")

        elif (valor > limite):
                print("Operação falhou! O valor do saque excede o limite.")

        elif (numero_saques >= LIMITE_SAQUES):
                print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
                saldo = saldo - valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
        else:
                print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n-----------------")
    print("\n ----EXTRATO----")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-----------------")

    return extrato

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu + "\nSelecione uma opção: ")
    print("-----------------")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")