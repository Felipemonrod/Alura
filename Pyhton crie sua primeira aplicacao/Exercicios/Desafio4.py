import os

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""
informacoes_gerais = [{'nome':'Pessoa1','idade': 20 ,'cidade':'Petrolina'},
                      {'nome':'Pessoa2','idade': 18 ,'cidade':'São Paulo'},
                      {'nome':'Pessoa3','idade': 35 ,'cidade':'Maceio'},
                      ]

print('\n 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.\n')
for dados in informacoes_gerais:
    nome = dados['nome']
    idade = dados['idade']
    cidade = dados['cidade']
    print (f'- {nome.ljust(5)} | {idade} | {cidade}')

"""
# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

"""
"""
# por tal dos assinantes não esta funcionando tela branca 
informacoes_gerais = [{'nome':'Pessoa1','idade': 20 ,'cidade':'Petrolina','profissao':''},
                      {'nome':'Pessoa2','idade': 18 ,'cidade':'São Paulo','profissao':'Progamador'},
                      {'nome':'Pessoa3','idade': 35 ,'cidade':'Maceio','profissao':'Engenhiro Alimentar'},
                      ]
def menu():
    print('\n')
    print('.1 Adicione um Item')
    print('.2 Modifica os itens')
    print('.3 Adiciona uma profissao')
    print('.4 Lista as pessoas')
    print('.5 Remove uma das categorias')

def voltar_ao_menu():
    input('\nDigite um caracter para voltar ao menu principal ')
    main()

def menu_switch():
    try:
        resposta = int(input('Escolha sua operação'))
        match resposta:
            case 1:
                adcionar_item()
        match resposta:
            case 2:
                modificar_itens()
        match resposta:
            case 3:
                adiciona_profissao()
        match resposta:
            case 4:
                listar_item
        match resposta:
            case 5:
                remover()

    except: ValueError

def adcionar_item():    
    print('\nAdicione um Item')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade: ')
    boolean = input('Gostaria de adicionar uma profissão S ou N?')
    if boolean == 'S' | 's':
        profissao = input('Digite sua profisssão: ')
    else:
        print('Voltando ao menu')
        menu()
    for dados_item in informacoes_gerais:
        if nome == informacoes_gerais['nome']:
            print('Nome já cadastrado, cadastre novamente')
            adcionar_item()
        else:
            dados_item =[{'nome': nome, 'idade' : idade, 'cidade' : cidade, 'profissao' : profissao}]
            informacoes_gerais.append(dados_item) 
    print(f'\n {nome} foi cadastrado com sucesso')
    voltar_ao_menu()

def modificar_itens():
    print('\nModificar itens\n')
    nome_busca = input('Digite o nome da pessoa a ser alaterado os itens: ')
    nome_encontrato = False
    for dados in informacoes_gerais:
        if nome_busca == dados['nome']:
            nome_encontrato = True
            print('\n1. Alterar o nome')
            print('2. Alterar o idade')
            print('3. Alterar o cidade')
            print('4. Alterar o profissao')
            try:
                escolha = int(input('Escolha '))
                match escolha:
                    case 1:
                        novo_nome = input(f'Digite seu novo de {nome_busca} nome: ')
                        dados['nome'] = novo_nome
                        print(f'O nome foi alterado com sucesso para {novo_nome}')
                        voltar_ao_menu()
                    case 2:
                        nova_idade = int(input(f'Digite sua nova idade'))
                        dados['idade'] = nova_idade
                        print(f'A idade de {nome_busca} foi alterada para {nova_idade}')
                        voltar_ao_menu()
                    case 3:
                        nova_cidade = input('Digite sua nova cidade: ')
                        dados['cidade'] = nova_cidade
                        print(f'A cidade de {nome_busca} foi alterada para {nova_cidade}')
                        voltar_ao_menu()
                    case 4:
                        nova_profissao = input(f'Digite a sua nova profissão para o {nome_busca}: ')
                        dados['profissao'] = nova_profissao
                        print(f'A profissao de {nome_busca} foi alterada para {nova_profissao}')
                        voltar_ao_menu()
            except: ValueError
            print('Entrada inválida. Tente novamente.')
            modificar_itens()
        if not nome_encontrato:
            print(f'Nome {nome_busca} não foi encontrado Tente Novamente')
            modificar_itens()
    voltar_ao_menu()


def adiciona_profissao():
    print('\n Adiciona profissao\n')
    nome_busca = input('Digite o nome da pessoa')
    nome_encontrado = False
    for dados in informacoes_gerais:
        if nome_busca == dados[{'nome'}]:
            nome_encontrado = True
            nova_profissao =  input(f'Digite a nova profissao do(a) {nome_encontrado} ')
            dados ['profissao'] == nova_profissao
            print(f'A profissão de {nome_busca} foi atualizada para {nova_profissao}')
        break
    if not nome_encontrado:
        print(f'nome {nome_busca} não encontrado tente outro')
        adiciona_profissao()


def listar_item():
    print('\n Listar Itens\n')
    for dados in informacoes_gerais:
        nome = dados['nome']
        idade = dados['idade']
        cidade = dados['cidade']
        profissao = '' if dados['Sem profissao'] else dados['profissao']
        print(f'- O ou A {nome} com idade de {idade} mora na{cidade} e trabalha com {profissao}')
        voltar_ao_menu()

def remover():
    print('\n Remover itens')
    nome_busca = input('Digite o nome para deletar seus dados')
    nome_encontrato = False
    for i, dados in enumerate(informacoes_gerais):
        if nome_busca == dados['nome']:
            nome_encontrato = True
            del informacoes_gerais[i]
        print(f'Os dados de {nome_busca} foram removidos')
        break        
    if not nome_encontrato:
        print('Não foi encontrado nenhuma pessoa com este nome')
    voltar_ao_menu()

def main():
    os.system('cls')
    menu()
    menu_switch()

if __name__ == '__main__':
    main()
