NUMERO_AGENCIA = "0001"
numero_conta = 0
bank_data = []
saques_restantes = 3
LIMITE_SAQUE = 500

def cadastrar_usuario(nome, cpf):
    global numero_conta
    cpf_repetido = False
    for registro in bank_data:
        if registro.get("cpf") == cpf:
            cpf_repetido = True
            break
                
    if cpf_repetido:
        print("CPF já cadastrado. Por favor, insira um CPF diferente.")
        return
        
    numero_conta += 1     
    registro = {'n°': numero_conta, 'nome': nome, 'cpf': cpf, 'conta': None, 'saldo': None}
    bank_data.append(registro)
    criar_conta_bancaria(nome, cpf, numero_conta)

def criar_conta_bancaria(nome, cpf, numero_conta):
    global bank_data
    conta_bancaria = f"{NUMERO_AGENCIA} - {numero_conta}"
    bank_data[numero_conta - 1]["conta"] = conta_bancaria
    bank_data[numero_conta - 1]["saldo"] = 0
    print("Conta Bancária criada com sucesso!")
    print(bank_data[numero_conta - 1])
    return 

def logar_conta():
    login_cpf = input("Digite o seu CPF:")
    cpf_repetido = False  
    for registro in bank_data:
        if registro.get("cpf") == login_cpf:
            cpf_repetido = True
            
        if cpf_repetido:
            print("Login Realizado com sucesso!")
            encontrar_cpf(login_cpf)
            
        print("CPF não registrado no sistema")

def realizar_deposito(saldo, i):
    valor_deposito = float(input("Digite o valor para o Depósito:"))
    confirmacao = input(f"Confirma o Depósito de R${valor_deposito:.2f}? (S) ou (N)")
    if confirmacao == 's':
        saldo += valor_deposito
        bank_data[i]["saldo"] = saldo
        print(f"Depósito de R${valor_deposito:.2f} realizado, valor total = R${saldo:.2f}")
    elif confirmacao == 'n':
        return
    else:
        print("Caractere Inválido")
        return
    
def saque_deposito(saldo, i):
    global saques_restantes
    pode_sacar = False
    valor_saque = float(input("Digite o valor á ser sacado:"))
    if valor_saque > LIMITE_SAQUE:
        print(f"Valor maior que R${LIMITE_SAQUE:.2f}, Digite Novamente")
        return
    elif valor_saque <= LIMITE_SAQUE:
        confirmacao = input(f"Confirma o Saque de R${valor_saque:.2f}? (S) ou (N)")
        if confirmacao == 's':
            saldo -= valor_saque
            bank_data[i]["saldo"] = saldo
            saques_restantes -= 1
            print(f"Saque de R${valor_saque:.2f} realizado, valor total = R${saldo:.2f}")
            print(f"Saques Restantes: {saques_restantes}")
            continuar_sacar = input("Continuar o Saque? (S) ou (N)")
            if continuar_sacar == 's':
                pode_sacar = True
            if continuar_sacar == 'n':
                pode_sacar = False
    if pode_sacar:
        return

def encontrar_cpf(cpf):
    for i, registro in enumerate(bank_data):
        if registro.get("cpf") == cpf:
            menu_cliente(registro.get("cpf"), registro.get("nome"), registro.get("saldo"), registro.get("conta"), i)
    return None, None, None, None, None

def sair():
    while True:
        confirmar_saida = input("Confirma a Saída? (S) ou (N)").lower()
        if confirmar_saida == 's':
            print("Saída Realizada com Sucesso. Adeus")
            break
        elif confirmar_saida == 'n':
            break
        else:
            print("Opção Inválida, por favor insira 'S' para Sim ou 'N' para Não.")

def menu_cliente(cpf, nome_cliente, saldo_cliente, conta_cliente, bank_account_position):
    menu_acess = f"""
===================================================================
    MR MONEY BANK V.2.0
    CONTA: {conta_cliente}  
    NOME: {nome_cliente.upper()}
    CPF: {cpf}
    
    1 - Realizar Depósito 
    2 - Realizar Saque
    3 - Sair
    
    Dinheiro Disponível = R$ {saldo_cliente:.2f}

===================================================================
"""
    print(menu_acess)
    opcao = input("Selecione a Opção Desejada:")
    if opcao == '1':
        realizar_deposito(saldo_cliente, bank_account_position)
    elif opcao == '2':
        saque_deposito(saldo_cliente, bank_account_position)
    elif opcao == '3':
        sair()

login_acess = """
==================================================================
    BEM VINDO AO BANCO MR MONEY V.2.0
    
    1 - Criar Conta 
    2 - Logar Conta
    3 - Sair 

==================================================================
"""

print(login_acess)

while True:
    opcao = input("Selecione a opção desejada:")
    if opcao == '1':
        nome = input("Insira seu nome completo abaixo:")
        cpf = input("Insira seu CPF:")
        cadastrar_usuario(nome, cpf)
    elif opcao == '2':
        logar_conta()
    elif opcao == '3':
        sair()
        break
    else:
        print("Opção inválida! Por favor, selecione uma das opções listadas.")