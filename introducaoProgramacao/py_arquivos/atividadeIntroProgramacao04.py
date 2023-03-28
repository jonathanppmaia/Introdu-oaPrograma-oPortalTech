def calculadora():
    while True:
        print("Selecione a operação")
        print("1 : Soma")
        print("2 : Subtração")
        print("3 : Multiplicação")
        print("4 : Divisão")
        print("0 : Sair")
        
        operacao =input("Digite o número da operação desejada: ")
        
        if operacao == "0":
            print("Saindo do Programa")
            break
        elif operacao not in ["1", "2", "3","4"]:
            print("Essa opção não existe")
            continue
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundoo número: "))
        
        if operacao == "1":
            resultado = num1 + num2
            print(f"O resulta da soma dos números {num1} e {num2} é {resultado}")
        elif operacao == "2":
            resultado = num1 - num2
            print(f"O resulta da subtração dos números {num1} e {num2} é {resultado}")
        elif operacao == "3":
            resultado = num1 * num2
            print(f"O resulta da multiplicação dos números {num1} e {num2} é {resultado}")
        else:
            if num2 == 0:
                print("não é possível a divisão por zero.")
            else:
                resultado = num1 / num2
                print(f"O resulta da divisão dos números {num1} e {num2} é {resultado}")

print(calculadora())