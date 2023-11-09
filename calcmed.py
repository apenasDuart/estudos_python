# Criação da lista para colocar as notas
lista = []

#Looping para calcular as médias e colocar-las dentro da lista
while True:

    #Definindo as variáveis
    med_final = 10
    av = -1
    ava = -1

    #Input do usuário + verificação das notas
    nome = input("Insira o nome do aluno:\n")
    while av < 0 or av > 10:
        av = float(input("Digite a nota da AVA:\n"))
        if av < 0 or av > 10:
            print("Nota inválida, insira novamente.\n")
    while ava < 0 or ava > 2:
        ava = float(input("Digite a nota do AVA:\n"))
        if ava < 0 or ava > 2:
            print("Nota inválida, insira novamente.\n")

    #Fazendo a média (soma das notas)
    med2 = av + ava

    #Verificação da aprovação
    if med2 > 10:
        med2 == med_final
        print("Excelência, a média final do aluno é", med_final)
    elif (med2 >= 6):
        med_final = med2
        print("Aprovado, a média final do aluno é", med_final)
    else:
        med_final = med2
        print("Reprovado, a média final do aluno é", med_final)
    
    #Nome + média final
    inf_alunos = [nome, med_final]
    lista.append(inf_alunos)

    #Saida ou permanência no programa
    sair = input('Se você deseja sair do programa aperte "S"\n')
    if sair == 'S' or sair == 's':
        break

#Impressão da lista 
print("A lista das notas é,", lista)