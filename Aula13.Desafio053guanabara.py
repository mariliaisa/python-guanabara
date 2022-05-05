frase = str(input('Digite uma frase: ')).strip().upper().split()
frase2 = ''.join(frase)
inverso = '' #como se fosse uma variável soma
for letra in range(len(frase2) - 1, -1, -1): #len(frase) - 1 porque a contagem é do 0 ao numero final
    inverso += frase2[letra]
print('Temos as frases {} e {}'.format(frase2, inverso), end=' ')
if inverso == frase2:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

