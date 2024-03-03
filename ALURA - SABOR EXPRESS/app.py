import os
restaurantes = ['Pizza', 'Sushi']

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
    print('3. Ativar restaurante')
    print('4. sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app :)')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal:  ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto, '\n')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')
    nome_nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_nome_restaurante)
    print(f'O restaurante {nome_nome_restaurante} foi cadastrado com sucessos!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurante')

    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurantes')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()