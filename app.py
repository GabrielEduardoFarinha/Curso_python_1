import os

restaurantes = ['sushi', 'lasanha']

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def menu_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurantes')
    print('3. ativar restaurante')
    print('4. sair do cadastro\n')

def opcao_invalida():
    print('opção não existente\n')
    input('digite qualquer tecla para voltar ao menu')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('digite o nome do novo restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('\ndigite qualquer tecla para voltar ao menu')
    main()

def listar_restaurantes():
    os.system('cls')
    print('lista de restuarantes a baixo: \n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    input('\ndigite qualquer tecla para voltar ao menu')
    main()


def escolha_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opção: '))



        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
            
def finalizar_app():
    os.system('cls')
    print('finalizando o app')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu_opcoes()
    escolha_opcao()
 
if __name__ == '__main__':
    main()
