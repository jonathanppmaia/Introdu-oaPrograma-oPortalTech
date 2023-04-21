def nome_ano_nascimento():
    nome = input("Digite o seu nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
            if (ano_nascimento >= 1922 and ano_nascimento <= 2021):
                idade = 2022 - ano_nascimento
                print("Olá,",nome,'!', "Você completou, ou irá completar,",idade,"anos em 2022.")
                break
            else:
                print("Ano de nascimento inválido.")
        except:
            print("Ano de nascimento inválido.")

nome_ano_nascimento()