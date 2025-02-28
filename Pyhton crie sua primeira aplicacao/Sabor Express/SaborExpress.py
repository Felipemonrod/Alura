import os

# ---- Lista ----

                #Dicionario utiliza {} dentro de uma []
restaurantes = [{'nome':'Sushi','categoria':'Japonessa','ativo':False},
                {'nome':'Macarrao','categoria':'Italiana','ativo':True},
                {'nome':'Lamen','categoria':'Japonesa','ativo':True}
                ]

# ---- Exibir titulos ----

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
def exibir_titulo(texto):
    os.system('cls')
    linha = '-' * len((texto))
    print (linha)
    print(texto)
    print(linha)

# ----- Menu de seleção -----

def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar Status do restaurante')
    print('4. Listar restaurantes Ativos')
    print('5. Listar restaurantes Desativados')
    print('6. Listar restaurantes Status')
    print('7. Sair\n')

# ---- finalizar ações -----

def finalizar_app():
    os.system('exit')
    exibir_titulo('Finalizando o app\n')
    
def voltar_ao_menu():
    input('\nDigite um caracter para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu()

def pergunta_bolean():
    try:
        bolean = input('Escolha S ou N: ')
        match bolean:
            case 'S' | 's':
                listar_restaurante_status()
            case 'N' | 'n':
                voltar_ao_menu()
    except: ValueError
    print('Resultado Não aceito Voltando ao menu')
    voltar_ao_menu()

# ---- Funções do menu ----
    # lembrente: para adcionar dados no dicionario usar como entrada um dicionario
def cadastrar_restaurante():
    exibir_titulo('\nCadastro de Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input (f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante= {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurente {nome_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu()

def listar_restaurante():
    exibir_titulo('\nListar Restaurantes')
    print(f'{'Nome do restaurante'.ljust(25)}| {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes: 
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status.ljust(20)}')
    voltar_ao_menu()

def alterar_status_restaurante():
    exibir_titulo('\n Ativar Restaurante')
    nome_restaurante  = input('Digite o nome do restaurante para alterear o status no restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante{nome_restaurante}foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O não foi encontrado')
    voltar_ao_menu()

    # obs: as 3 outras listas foram feitas para praticar   
def listar_restaurantes_ativos():
    exibir_titulo('\nListar Restaurantes Ativos')
    for restaurante in restaurantes:
        nome_restaurante =  restaurante ['nome']
        status = restaurante ['ativo']
        if status == True:
            print(f'- {nome_restaurante.ljust(20)} | {status}')
    voltar_ao_menu()

def listar_restaurantes_desativados():
    exibir_titulo('\nListar Restaurantes Desativados')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        status = restaurante ['ativo']
        if status == False:
            print(f'- {nome_restaurante.ljust(20)} | {status}') 
    voltar_ao_menu()
       
def listar_restaurante_status():
    exibir_titulo('\nListar Status dos Restaurantes')
    print('1 para Restaurantes Ativos')
    print('2 para Restaurantes Desativados')
    try:
        resposta = int(input('Escolha uma opção: '))
        match resposta:
            case 1:
                print('\nRestaurantes Ativos')
                for restaurante in restaurantes:
                    nome_restaurante = restaurante ['nome']
                    status = restaurante ['ativo']
                    if status == True:
                        print(f'- {nome_restaurante.ljust(20)} | {status}')
                print('Gostaria de Listar outros restaurantes?')
                pergunta_bolean()
            case 2:
                print('\nRestaurantes Desativados')
                for restaurante in restaurantes:
                    nome_restaurante = restaurante ['nome']
                    status = restaurante ['ativo']
                    if status == False:
                        print(f'- {nome_restaurante.ljust(20)} | {status}')
                print('Gostaria de Listar outros restaurantes?')
                pergunta_bolean()            
    except: ValueError
    print('Resultado Não aceito Voltando ao menu')
    voltar_ao_menu()

# ---- Menu ----

def escolher_op_switch():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurantes')
                cadastrar_restaurante()
            case 2:
                print('Listar restaurantes')
                listar_restaurante()
            case 3:
                print('Ativar restaurante')
                alterar_status_restaurante()
            case 4:
                print ('listar restaurantes Ativos')
                listar_restaurantes_ativos()
            case 5:
                print ('Listar restaurantes Desativados')
                listar_restaurantes_desativados()
            case 6:
                print('Listar Status dos restaurantes')
                listar_restaurante_status()
            case 7:
                print('Finalizar app')
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_programa()
    menu()
    escolher_op_switch()

if __name__ == '__main__':
    main()
