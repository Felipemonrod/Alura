import os

restaurantes = []


def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('exit')
    os.system('cls')
    print('Finalizando o app\n')

def opcao_invalida():
    print('Opção invalida\n')
    input('Digite um caracter para voltar ao menu principal')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('\nCadastro de Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'\nO restaurente {nome_restaurante} foi cadastrado com sucesso\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def listar_restaurante():
    for item in restaurantes: 
        print('\n'+ item)
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_op_switch():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurantes')
                cadastrar_restaurante()
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                print('Finalizar app')
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida
    

def main():
    os.system('cls')
    exibir_nome_programa()
    menu()
    escolher_op_switch()
    #escolher_op()


if __name__ == '__main__':
    main()


# ----- reutilizar

# def escolher_op():
#     opcao_escolhida = int(input('Escolha uma opção: '))# colocar o tipo de variavel antes do input para transformar a resposta
#         # opcao_escolhida = int(opcao_escolhida) outra opc
#     if opcao_escolhida == 1 :
#         print('Cadastras Restaurante')

#     elif opcao_escolhida == 2 :
#         print('Listar Restaurante')

#     elif opcao_escolhida == 3 :
#         print('Ativar Restaurante')

#     else:
#         finalizar_app

#------- utlizar o match uso parecido com o switch 
