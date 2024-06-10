def adicionar(x, y):
    # Função que soma dois números.
    return x + y

def subtrair(x, y):
    # Função que subtrai o segundo número do primeiro.
    return x - y

def multiplicar(x, y):
    # Função que multiplica dois números.
    return x * y

def dividir(x, y):
    # Função que divide o primeiro número pelo segundo.
    if y == 0:
        return 'Erro: Divisão por zero!'
    return x / y

def menu():
    # Exibe o menu de opções.'
    print('\nEscolha a operação:')
    print('1. Adicionar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Sair')


def main():
    while True:
        menu()
        try:
            escolha = int(input('Digite a opção (1/2/3/4/5): '))

            if escolha == 5:
                print('Saindo... Obrigado por usar a calculadora!')
                break
            elif escolha in [1, 2, 3, 4]:
                try:
                    num1 = float(input('Digite o primeiro número: '))
                    num2 = float(input('Digite o segundo número: '))

                    if escolha == 1:
                        print(f'Resultado: {num1} + {num2} = {adicionar(num1, num2)}')
                    elif escolha == 2:
                        print(f'Resultado: {num1} - {num2} = {subtrair(num1, num2)}')
                    elif escolha == 3:
                        print(f'Resultado: {num1} * {num2} = {multiplicar(num1, num2)}')
                    elif escolha == 4:
                        resultado = dividir(num1, num2)
                        print(f'Resultado: {num1} / {num2} = {resultado}')
                except ValueError:
                    print('Entrada inválida! Por favor, digite números válidos.')
            else:
                print('Opção inválida! Por favor, escolha uma opção de 1 a 5.')
        except ValueError:
            print('Entrada inválida! Por favor, digite um número para a opção.')


if __name__ == '__main__':
    main()
