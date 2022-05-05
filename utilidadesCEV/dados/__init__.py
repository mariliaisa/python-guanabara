def leiadinheiro():
    while True:
        num = str(input('Digite o valor: R$')).replace(',', '.').strip()
        if num.isnumeric():
            return float(num)    
        else:
            print(f'\033[1;31mERRO! Digite novamente\033[0m')



def leiaInt(texto=''):
    while True:
        texto = str(input('Digite um número: ')).strip()
        if texto.isnumeric():
            texto = int(texto)
            return f'Você acabou de digitar o número {texto}'
        else:
            print(f'\033[1;31mTente novamente.\033[0m')


