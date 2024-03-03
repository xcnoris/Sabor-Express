import os
restaurantes =[{'nome': 'Campos', 'categoria': 'Pizza', 'ativo': False},
               {'nome':'Titos', 'categoria': 'marmitas', 'ativo': True},
               {'nome':'Sabor Brasil', 'categoria': 'Lanches', 'ativo': False}]


def main():
    os.system('cls')
    exibir_nome_do_programa() 
    exibir_opcoes_menu()
    escolher_opcao()


def exibir_nome_do_programa():

    print("""
    
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    \n""")


def exibir_opcoes_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Altenar estado do restaurante')
    print('4. sair\n')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                altenar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    exibir_subtitulo('Finalizando app :)')


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha, '\n')



def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal:  ')
    main()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucessos!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{'   Nome'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def altenar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'\nO restaurante {nome_restaurante} não foi encontrado\n')
    voltar_ao_menu_principal()



if __name__ == '__main__':
    main()