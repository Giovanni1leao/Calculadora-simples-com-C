def calculadora():

    operacao = input('''Digite o simbolo da operacao desejada ----------------------------------------------------------------------------------------------------------------------------------------------------
    (+) (-) (*) (/) : ''')
    number1 = int(input('Digite o primeiro numero: '))
    number2 = int(input('Digite o segundo número: '))

    if operacao    == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)
    elif operacao == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)
    elif operacao == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)
    elif operacao == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)
    de_novo()
    
def de_novo():
    calc_de_novo = input('''Digite S se deseja continuar calculando e N se deseja encerrar o programa: --------------------------------------------------------------------------------------------------------------
    ''')
    if calc_de_novo.upper() == "S":
        calculadora()
    elif calc_de_novo.upper() == "N":
        print('Ate os proximos calculos, pequeno gafanhoto!')
    else:
        de_novo()

calculadora()