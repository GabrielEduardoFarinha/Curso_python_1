"""
# Exercícios de Python - Alura

Este script contém a resolução de três exercícios propostos para praticar conceitos básicos de Python, incluindo saída de dados no terminal e manipulação de strings.

## Exercício 1
Imprima a seguinte frase:
Python na Escola de Programação da Alura.

## Exercício 2
Imprima a frase:
Meu nome é {nome} e tenho {idade} anos
Onde {nome} e {idade} devem ser valores armazenados em variáveis.

## Exercício 3
Imprima a palavra ALURA, onde cada letra deve aparecer em uma linha e as letras A devem estar em vermelho.

## Código

# Exercício 1
print('Python na Escola de Programação da Alura.\n')

# Exercício 2
NOME = 'Gabriel'
IDADE = '24'

print(f'Meu nome é {NOME} e tenho {IDADE} anos de vida\n')

# Exercício 3
print('\033[31m' + 'A' + '\033[0m')
print('L')
print('U')
print('R')
print('\033[31m' + 'A' + '\033[0m\n')

## Como executar

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Salve este script em um arquivo com extensão `.py`, como `exercicios.py`.
3. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo foi salvo.
4. Execute o arquivo com o comando:
   python exercicios.py

## Saída esperada

### Exercício 1
Python na Escola de Programação da Alura.

### Exercício 2
Meu nome é Gabriel e tenho 24 anos de vida

### Exercício 3
A
L
U
R
A

No terminal com suporte a ANSI, as letras `A` aparecerão em vermelho. Em ambientes que não suportam sequências ANSI, as letras aparecerão normalmente.

## Sobre este script

Este script foi criado para fins educacionais, como parte das atividades propostas no curso de programação da Alura. Sinta-se à vontade para editar e adaptar!
"""
