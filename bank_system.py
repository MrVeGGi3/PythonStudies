banco_nome = "SISTEMA BANCÁRIO MR MONEY"
print(banco_nome)
nome = input(f"""Digite o nome do usuário da conta:
    """)
saques_restantes = 3 
dinheiro_total = float(1000) 
LIMITE_SAQUE = 500
mensagem_saída = (f"""

Obrigado!! Até Mais!!
""")
menu_principal = (f"""
==================================================================    
    {banco_nome}
    {nome.upper()}
    
    1 - Depositar
    2 - Sacar
    3 - Sair
    
    Saques restantes = {saques_restantes}
    Dinheiro Total = R$ {dinheiro_total} 
==================================================================
    """
)
print(menu_principal)
opção = input(f"""Digite a Opção desejada:
""")


while True :
    if(opção == '1'):
        valor_depósito = float(input('Digite o Valor á ser depositado:'))
        dinheiro_total += valor_depósito
        print(f""" Depósito Realizado com SUCESSO
         O valor atual é de: R$ {dinheiro_total}
        """)
        ult_opção = input(f"""Deseja mais alguma coisa?
            Sim (S) ou Não(N)?""")
        if (ult_opção == 'S'):
            print(menu_principal)
        elif(ult_opção == 'N'):
            print(mensagem_saída)
            break
        else:
            print("Entrada Incorreta!")
        break
    if(opção == '2'):
        valor_saque = float(input(f""" Digite o Valor para Sacar até R$ {LIMITE_SAQUE}:
            """
        ))
        if(valor_saque > LIMITE_SAQUE or valor_saque < 0):
            print("Valor Incorreto")
        else:
            dinheiro_total -= valor_saque
            print(f""" Saque Realizado com SUCESSO! 
                    Dinheiro Total: R${dinheiro_total}
            """)
            ult_opção = input(f"""Deseja mais alguma coisa?
            Sim (S) ou Não(N)?
            """)
        if (ult_opção == 'S'):
            print(menu_principal)
        elif(ult_opção == 'N'):
            print(mensagem_saída)
            break
        else:
            print("Entrada Incorreta!")
        break
    if(opção == '3'):
        print("Confirma a Saída?")
        ult_opção = input(f"""Sim(S) ou Não(N)?
        """)
        if(ult_opção == 'N'):
            print(menu_principal)
        if(ult_opção == 'S'):
            print(mensagem_saída)
            break
        break
        
    
    