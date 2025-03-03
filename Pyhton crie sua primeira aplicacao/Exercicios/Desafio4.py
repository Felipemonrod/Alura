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


informacoes_gerais = [
    {'nome': 'Pessoa1', 'idade': 20, 'cidade': 'Petrolina', 'profissao': ''},
    {'nome': 'Pessoa2', 'idade': 18, 'cidade': 'São Paulo', 'profissao': 'Programador'},
    {'nome': 'Pessoa3', 'idade': 35, 'cidade': 'Maceió', 'profissao': 'Engenheiro Alimentar'}
]

def menu():
    print('\n')
    print('.1 Adicione um Item')
    print('.2 Modifica os itens')
    print('.3 Adiciona uma profissão')
    print('.4 Lista as pessoas')
    print('.5 Remove uma das categorias')

def voltar_ao_menu():
    input('\nDigite um caractere para voltar ao menu principal ')
    menu()
    menu_switch()

def menu_switch():
    try:
        resposta = int(input('Escolha sua operação: '))
        match resposta:
            case 1:
                adcionar_item()
            case 2:
                modificar_itens()
            case 3:
                adiciona_profissao()
            case 4:
                listar_item()
            case 5:
                remover()
            case _:
                print('Opção inválida. Tente novamente.')
                menu_switch()
    except ValueError:
        print('Entrada inválida')
        menu_switch()

def listar_item():
    print('\nListar Itens\n')
    for dados in informacoes_gerais:
        nome = dados['nome']
        idade = dados['idade']
        cidade = dados['cidade']
        profissao = dados['profissao'] if dados['profissao'] else "Sem profissão"
        print(f'- {nome}, {idade} anos, mora em {cidade} e trabalha como {profissao}')
    voltar_ao_menu()

def adcionar_item():    
    print('\nAdicione um Item')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade: ')
    profissao = ''
    boolean = input('Gostaria de adicionar uma profissão (S/N)? ').strip().upper()
    if boolean == 'N':
        print('Voltando ao menu')
        menu()
    else:
        profissao = input('Digite sua profissão: ')
    informacoes_gerais.append({'nome': nome, 'idade': idade, 'cidade': cidade, 'profissao': profissao})
    print(f'\n{nome} foi cadastrado com sucesso')
    voltar_ao_menu()

def modificar_itens():
    print('\nModificar itens\n')
    nome_busca = input('Digite o nome da pessoa a ser alterado os itens: ')
    for dados in informacoes_gerais:
        if nome_busca == dados['nome']:
            print('\n1. Alterar o nome')
            print('2. Alterar a idade')
            print('3. Alterar a cidade')
            print('4. Alterar a profissão')
            try:
                escolha = int(input('Escolha: '))
                match escolha:
                    case 1:
                        dados['nome'] = input(f'Digite o novo nome para {nome_busca}: ')
                    case 2:
                        dados['idade'] = int(input(f'Digite a nova idade de {nome_busca}: '))
                    case 3:
                        dados['cidade'] = input(f'Digite a nova cidade de {nome_busca}: ')
                    case 4:
                        dados['profissao'] = input(f'Digite a nova profissão de {nome_busca}: ')
                    case _:
                        print('Opção inválida.')
                        modificar_itens()
                print('Alteração realizada com sucesso!')
                voltar_ao_menu()
                return
            except ValueError:
                print('Entrada inválida. Tente novamente.')
                modificar_itens()
    print(f'Nome {nome_busca} não foi encontrado. Tente novamente.')
    modificar_itens()

def adiciona_profissao():
    print('\nAdicionar profissão\n')
    nome_busca = input('Digite o nome da pessoa: ')
    for dados in informacoes_gerais:
        if nome_busca == dados['nome']:
            dados['profissao'] = input(f'Digite a nova profissão para {nome_busca}: ')
            print(f'A profissão de {nome_busca} foi atualizada.')
            voltar_ao_menu()
            return
    print(f'Nome {nome_busca} não encontrado. Tente novamente.')
    adiciona_profissao()

def remover():
    print('\nRemover itens')
    nome_busca = input('Digite o nome para deletar seus dados: ')
    for i, dados in enumerate(informacoes_gerais):
        if nome_busca == dados['nome']:
            del informacoes_gerais[i]
            print(f'Os dados de {nome_busca} foram removidos.')
            voltar_ao_menu()
            return
    print('Não foi encontrada nenhuma pessoa com este nome.')
    voltar_ao_menu()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    menu_switch()

if __name__ == '__main__':
    main()

"""
