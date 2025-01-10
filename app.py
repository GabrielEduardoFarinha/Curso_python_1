pessoas = [{'nome':'Joe ', 'idade':'27', 'cidade': 'Detroit'}]
pessoas[0]['idade'] = 50
pessoas[0]['profissão'] = 'caminhoneiro'
del pessoas[0] ['cidade']
print(pessoas)
numeros = {i: i**2 for i in range(1, 6)}
print(numeros)
if 'idade' in pessoas[0]:
    print('existe o campo idade nesse dicionário')
else:
    print('termo inexistente no dicionário')


música_erudita = 'Aah lelek lek lek lek lek lek lek lek lek lek Aah lelek lek lek lek lek lek lek lek lek lek girando girando girando pro lado girando girando girando pro outro Aah lelek lek lek lek lek lek lek lek lek lek'

palavras = música_erudita.split()

frequencia = {}

for palavra in palavras :
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1
print(frequencia)