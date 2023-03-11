nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
res_media = (nota01 +nota02)/2
print(f'Sua Primeira média foi %s'  %(res_media))
if res_media >= 7.0:
    print(f'Você foi aprovado')
else:
    print(f'Infelizmente você foi reprovado!')