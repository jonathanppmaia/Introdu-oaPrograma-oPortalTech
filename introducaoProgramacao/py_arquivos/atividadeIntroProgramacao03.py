#laço de repetição for:

for i in range(20, 0, -1):
    if i != 13:
        print(i)

#laço de repetição while:

i = 20
while i > 0:
    if i != 13:
        print(i)
    i -= 1


#laço de repetição for-in:
numeros = list(range(1, 21))
for i in reversed(numeros):
    if i != 13:
        print(i)

#laço de repetição "while" e uma condição de saída:
numeros = list(range(1, 21))
i = len(numeros) - 1

while True:
    num = numeros[i]
    if num != 13:
        print(num)
    i -= 1
    
    if i < 0:
        break

#O Python não tem uma estrutura de loop do-while como algumas outras linguagens de programação, 
# mas é possível simular um comportamento semelhante utilizando o laço de repetição "while" e uma condição de saída.