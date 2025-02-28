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
    try:
        resposta = int(input('Escolha sua operação'))
        match resposta:
            case 1:
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

    except: ValueError