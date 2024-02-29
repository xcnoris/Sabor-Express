import os
restaurantes = []

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
    os.system('cls')
    print('Encerrando app :)\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal:  ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_nome_restaurante)
    print(f'O restaurante {nome_nome_restaurante} foi cadastrado com sucess!')
    input('\nDigite uma tecla para voltar ao menu principal:  ')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurantes')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()

