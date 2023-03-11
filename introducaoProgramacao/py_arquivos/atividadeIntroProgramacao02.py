quantRodas = int(input(f'Digite a Quantidade de Rodas do Veículo: '))
pesoBruto = float(input(f'DIgite o peso bruto do veiculo: '))
quantPessoas = int(input(f'Digite a Quantidade de Pessoas no Veículo: '))


if quantRodas == 2 or quantRodas == 3:
    print("Categoria A")
elif quantRodas == 4 and quantPessoas <= 8 and pesoBruto <= 3500:
    print("Categoria B")
elif quantRodas >= 4 and quantPessoas > 8 and pesoBruto <= 6000:
    print("Categoria D")
elif quantRodas >= 4 and pesoBruto > 6000:
    print("Categoria E")
else:
    print("Categoria C")