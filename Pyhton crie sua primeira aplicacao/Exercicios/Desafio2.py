#--- atv 1
# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# numero = int(input('Digite seu numero:'))
# if numero % 2 == 0:
#     print(f'Este numero {numero} é par')
# else:
#     print(f'Este numero {numero} é impar')

#---- atv 2
# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# idade = int(input('Digite sua idade:'))
# if idade <= 12:
#     print(f'Voce é uma criança{idade}')
# elif idade <= 13 or idade <=18:
#     print(f'Voce é um adolescente{idade}')
# elif idade > 18:
#     print(f'Voce é um adulto {idade}')
       
#---- metodo atv2 com match teste o qualqueria fazer

# idade = int(input('Digite sua idade: '))

# match idade:
#     case idade if idade <= 12:
#         print('Você é uma criança')
#     case idade if 13 <= idade <= 18:
#         print('Você é um adolescente')
#     case idade if idade > 18:
#         print('Você é um adulto')
#     case _:
#         print('Valor inválido!')

#----- atv 3
# Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você

# def menu():
#     print('\nMenu\n')
#     print('Escolha seu procedimento:\n')
#     print('1. Cadastras usuario')
#     print('2. Verificar senha')
#     print('3. Sair')

# def escolher_op():
#     escolha = int(input('Digite o numero da sua escolha'))
#     match escolha:
#         case 1:
#             print('valor cadastrar seu usuario')
#             cadastro()
#         case 2:
#             print('Vamos verificar seu usuario')
#             pesquisa()
#         case 3:
#             print('Finalizando codigo')

# def cadastro():
#     nome = input('Digite seu nome:')
#     senha = int(input('Digite a senha em Digitos exemplo 11111\n'))
#     print(f'Seu nome é: {nome}')
#     print(f'Sua senha é: {senha}\n')
#     resposta = input('Gostaria de verificar seu usuario? S ou N')
#     if resposta == 'S':
#         pesquisa(nome,senha) # para passar os paramentros devo colocar eles dentro dos ()
#     elif resposta == 'N':
#         finalizar_app()


# def pesquisa(nome,senha): # e chamar eles aqui 
#     print('\nPesquisa\n')
#     nome_p = input('Digite seu nome:')
#     senha_p = int(input('Digite a senha\n'))
#     if nome_p == nome and senha_p == senha:
#         print('Seu usuario e senha estão certos')
#         finalizar_app()
#     else:
#         print('digite novamente seus dados')
#         pesquisa(nome,senha)

# def finalizar_app():
#     print('Finalizando app')

# def main():
#     menu()
#     escolher_op()
#     cadastro()
#     pesquisa()
#     finalizar_app()

# if __name__ == '__main__':
#     main()

#---- atv 4
# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# def menu():
#     x = int(input('\nMe informe o numero de x: '))
#     y = int(input('Me informe o numero de y: '))
#     calcular(x,y)

# def calcular(x,y):
#     if x > 0 and y > 0:
#         print(f'Localizado no primeiro quadrande valor em x:{x} e valor em y:{y}')
#     elif x < 0 and y > 0:
#         print(f'Localizado no segundo quadrande valor em x:{x} e valor em y:{y}')
#     elif x < 0 and y < 0:
#         print(f'Localizado no terceiro quadrande valor em x:{x} e valor em y:{y}')
#     elif x > 0 and y < 0:
#         print(f'Localizado no quarto quadrante quadrande valor em x:{x} e valor em y:{y}')
#     else:
#         print(f'O ponto está localizado no eixo ou origem valores em x:{x} em y:{y}')

# def main():
#     menu()

# if __name__ == '__main__':
#     main()