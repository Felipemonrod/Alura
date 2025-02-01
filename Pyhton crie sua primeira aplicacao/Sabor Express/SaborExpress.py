import os
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
    print('Finalizando o app\n')

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
def escolher_op_switch():
    opcao_escolhida = int(input('Escolha uma opção:'))
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurantes')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção invalida!')

def main():
    exibir_nome_programa()
    menu()
    escolher_op_switch()
    #escolher_op()


if __name__ == '__main__':
    main()