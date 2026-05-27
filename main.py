historicos = []
histcont = 0

def main():
    global histcont
    print("====================================")
    print("Bem vindo ao aplicativo sla n sei")
    print("====================================\n")
    while True:
        print("1. Opção 1\n2. Opção 2\n3. Opção 3\n4. Opção 4\n5. Opção 5")
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
        else:
            print("Opção inválida\n")