#Input das variáveis
while True:
    n1 = float(input('Digite o primeiro número:\n'))
    o = input('Digite o operador:\n')
    n2 = float(input('Digite o segundo número:\n'))

    #Lógica dos operandos
    if o == '+':
        resultado = n1 + n2
    elif o == '-':
        resultado = n1 - n2
    elif o == '*':
        resultado = n1 * n2
    elif o == '/':
        resultado = n1 / n2
    else:
        resultado = 'Operação inválida'

    #Resultado
    print(str(n1) + ' ' + str(o) + ' ' + str(n2) + ' = ' + str(resultado))
    b = input('Deseja continuar, se sim aperte "s" caso contrário aperte qualquer outra tecla!\n') #Rep do programa
    if b != 's':
        break
    