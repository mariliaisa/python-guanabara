num = int(input('número: '))
teste = 'é primo'
if num != 1:
    for i in range (2,num):
        if num % i == 0:
            teste = 'Não é primo'
print('O número {} {}'.format(num, teste))

