numero = input('digite um numero pf: ')

ultimo_numero = numero [-1]

if ultimo_numero in '02468':
    print(f'o número {numero} é par!')
else:
    print(f'o número {numero} é impar')

idade = int(input('digite a sua idade: '))

if idade <= 12:
    print('vocé é considerado uma criança')
elif 13 <= idade <= 18:
    print('vocé é considerado um adolescente')
else:
    print('vocé já é um adulto')

usuario_esperado = 123
senha_esperada = 123
usuario = int(input('pf digite um usuario: '))
senha = int(input('pf digite uma senha: '))

if usuario == usuario_esperado:
    print('usuario correcto')
else:
    print('usuario incorreto')

if senha == senha_esperada:
    print('senha correta')
else:
    print('senha incorreta')