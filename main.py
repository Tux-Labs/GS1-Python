historicos = []
histcont = 0
plantas = [['Alface', 'T°C - 22°C | Humidade: 60%'], ['Tomate', 'T°C - 22°C | Humidade: 60%'], ['Batata', 'T°C - 22°C | Humidade: 60%']]

def main():
    global histcont
    print("====================================")
    print("Bem vindo ao aplicativo sla n sei")
    print("====================================\n")
    while True:
        print("1. Solução\n2. Estufas\n3. Opção 3\n4. Opção 4\n5. Opção 5\n0. Sair")
        print("Digite a opção que você deseja acessar\n")
        op = input("- ")
        if op == '1':
            histcont += 1
            op1()
        elif op == '2':
            histcont += 1
            op2()
        elif op == '3':
            histcont += 1
            op3()
        elif op == '4':
            histcont += 1
            op4()
        elif op == '5':
            op5()
        elif op == '0':
            return
        else:
            print("Opção inválida\n")

def op1():
    historicos.append("Solução")
    print("\n---------------------------------")
    print("\nA solução consiste em uma estufa inteligente automatizada capaz de monitorar e controlar variáveis essenciais para o cultivo de plantas em Marte\nO sistema coleta dados de temperatura e umidade em tempo real e toma decisões automaticamente para manter o ambiente adequado para o desenvolvimento da plantação.")
    input("Digite algo para voltar: ")
    print("---------------------------------")

def op2():
    historicos.append("Estufas")
    print("\n---------------------------------")
    while True:
        print("Estufas ativas:")
        for planta in plantas:
            print(planta[0])
        print("\n(Digite 0 para retornar)")
        opcao = input("Digite a estufa que deseja visitar: ").lower().capitalize()
        for planta in plantas:
            if planta[0] == opcao:
                print("\n---------------------------------")
                print(planta)
                input("Digite algo para voltar: ")
                print("---------------------------------")
            elif opcao == '0':
                print("---------------------------------")
                return

def op3():
    print()

def op4():
    print()

def op5():
    print()

main()