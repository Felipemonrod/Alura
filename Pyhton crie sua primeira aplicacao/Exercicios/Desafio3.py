# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.


"""
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
nomes = ['nome0','nome1','nome2','nome3']
anos = [2005,2025]

for numero in numeros: 
        print(f'- {numero}')
for nome in nomes:
        print(f'- {nome}')
for ano in anos:
        print (f'- {ano}')
"""

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

"""
import os

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]  

def main():
    menu()

def menu():
    try:
        print ('\n\nMENU:')
        print('1 - Adicionar numero\n')
        print('2 - Listar numeros\n')
        print('3 - Finalizar app\n')
        opcao_escolhida = int(input('Escolha uma opção:'))
        match opcao_escolhida:
            case 1:
                print('Adicionar numero')
                novos_numero()
            case 2:
                print('Listar numeros')
                listar_numero()
            case 3:
                print('Finalizar app')
                sair()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def voltar_ao_menu():
    input('\nDigite um caracter para voltar ao menu principal ')
    main()

def novos_numero():
    print('\nDigite abaixo um numero de 1 a 10')
    for _ in range(3):
        novo_numero = int(input('\nDigite um numero positivo: '))
        if 0 < novo_numero < 10:
            numeros.append(novo_numero)  
            break
    print('\nVocê digitou o número ', novo_numero)
    resposta = input('\nVocê gostaria de adicionar um novo número? S ou N: ')
    if resposta.upper() == 'S':
        novos_numero()
    elif resposta.upper() == 'N':
        voltar_ao_menu()

def listar_numero():       
    for numero in numeros: 
        print(f'- {numero}') 
    resposta = input('\nVocê gostaria de adicionar um novo número? S ou N: ')
    if resposta.upper() == 'S':
        novos_numero()
    elif resposta.upper() == 'N':
        voltar_ao_menu()

def sair():   
    print('Finalizando o app\n')
    os.system('exit')

def opcao_invalida():
    print('Opção inválida. Tente novamente.')
    voltar_ao_menu()

if __name__ == '__main__':
    main()
"""

# extra.

"""
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for numero in numeros:
        if numero % 2 != 0:
                print((f'- {numero} é ímpar'))
        elif numero % 2 == 0:
                print((f'- {numero} é par'))

"""
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

"""

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
numero_impar = []
total = 0
for numero in numeros:
    if numero % 2 != 0:
        print(f'- {numero} é ímpar')
        numero_impar.append(numero)
        total += numero  
print(f'Total dos números ímpares: {total}')

"""

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

"""
numeros = [1, 5, 2, 6, 3, 4, 8, 7, 10, 9]
lista = []

for numero in numeros:
    if numero > 0:
        if len(lista) == 0:  
            lista.append(numero)
        else:
            for i in range(len(lista)):
                if numero > lista[i]:  
                    lista.insert(i, numero)  
                    break
            else:
                lista.append(numero)  

for numero in lista:
    print(f'- {numero}')

"""

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

"""

for i in range(1, 11): 
    resultado = numero_tabuada * i  
    print(f'{numero_tabuada} x {i} = {resultado}')  
    print(f'{range(i)}')

"""

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
total = 0

try:
    for numero in numeros:
        total += numero  

    print(f'Total dos números: {total}')  
except Exception as e:
    print(f"Ocorreu um erro: {e}")  

"""

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

"""

valores = [10, 20, 30, 40, 50]  
soma_valores = 0

try:
    for valor in valores:
        soma_valores += valor  

    media = soma_valores / len(valores)  
    print(f"Média dos valores: {media}")  
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")  
except Exception as e:
    print(f"Ocorreu um erro: {e}")  

"""