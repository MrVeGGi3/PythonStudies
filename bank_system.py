banco_nome = "SISTEMA BANCÁRIO MR MONEY"
print(banco_nome)
nome = input("Digite o nome do usuário da conta: ")

saques_restantes = 3
dinheiro_total = 1000.0
LIMITE_SAQUE = 500
mensagem_saida = "Obrigado!! Até Mais!!"

menu_principal = f"""
==================================================================
    {banco_nome}
    {nome.upper()}
    
    1 - Depositar
    2 - Sacar
    3 - Sair
    
    Saques restantes = {saques_restantes}
    Dinheiro Total = R$ {dinheiro_total:.2f} 
==================================================================
"""

print(menu_principal)

while True:
    opcao = input("Digite a Opção desejada: ")

    if opcao == '1':
        valor_deposito = float(input('Digite o Valor a ser depositado: '))
        dinheiro_total += valor_deposito
        print(f"Depósito Realizado com SUCESSO! O valor atual é de: R$ {dinheiro_total:.2f}")
        
    elif opcao == '2':
        valor_saque = float(input(f"Digite o Valor para Sacar até R$ {LIMITE_SAQUE}: "))
        if 0 < valor_saque <= LIMITE_SAQUE and valor_saque <= dinheiro_total:
            dinheiro_total -= valor_saque
            print(f"Saque Realizado com SUCESSO! Dinheiro Total: R$ {dinheiro_total:.2f}")
        else:
            print("Valor de saque inválido!")
    
    elif opcao == '3':
        confirmacao = input("Confirma a Saída? (Sim(S) ou Não(N)): ").upper()
        if confirmacao == 'S':
            print(mensagem_saida)
            break
    else:
        print("Opção inválida!")

    ult_opcao = input("Deseja mais alguma coisa? (Sim(S) ou Não(N)): ").upper()
    if ult_opcao == 'N':
        print(mensagem_saida)
        break
    elif ult_opcao != 'S':
        print("Entrada Incorreta!")