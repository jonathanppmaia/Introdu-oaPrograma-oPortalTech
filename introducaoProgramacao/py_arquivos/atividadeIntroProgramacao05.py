import datetime

while True:
    try:
        nome = input("Digite seu nome completo: ")
        ano_nascimento = int(input("Digite o ano do seu nascimento (entre 1922 e 2021): "))
        if ano_nascimento not in [ano for ano in range(1922, 2022)]:
            raise ValueError("Ano de nascimento fora do intervalo válido!")
        break
    except ValueError as e:
        print(e)

idade = datetime.date.today().year - ano_nascimento
print(f"Olá, {nome}! Você tem {idade} anos.")