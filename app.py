import os

restaurantes = [{'nome':'Joe Marmitas', 'categoria':'popular', 'ativo': False},
                {'nome':'Pizza da Serra', 'categoria':'pizzaria', 'ativo': True},
                {'nome':'b-52', 'categoria':'hamburgueria', 'ativo': False}]

def alteraçao_de_estado():
    exibir_subtitulo('alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_econtrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_econtrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f' o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_econtrado:
        print('o restaurante não foi encontrado')
    voltar_ao_menu_inicial()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_inicial():
    input('\nDigite qualquer tecla para voltar ao menu ')
    main()

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def menu_opcoes():
    print('1. cadastrar restaurante')
    print('2. listar restaurantes')
    print('3. alteração de estado')
    print('4. sair do cadastro\n')

def opcao_invalida():
    print('opção não existente\n')
    voltar_ao_menu_inicial()

def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('digite o nome do novo restaurante: ')
    categoria = input(f'digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria' : categoria ,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_inicial()

def listar_restaurantes():
    exibir_subtitulo('lista de restuarantes a baixo: ')
    print(f'{'nome do restaurante'.ljust(22)}|{'categoria'.ljust(20)}|Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)}|{categoria.ljust(20)}|{estado}')
    voltar_ao_menu_inicial()

def escolha_opcao():
    try:
        opcao_escolhida = int(input('escolha uma opção: '))



        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alteraçao_de_estado()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
            
def finalizar_app():
    exibir_subtitulo('finalizando o app')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu_opcoes()
    escolha_opcao()
 
if __name__ == '__main__':
    main()
