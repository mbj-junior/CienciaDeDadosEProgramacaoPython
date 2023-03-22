"""
11) A Universidade Hogwarts de Rapidópolis está contratando você para
desenvolver um algoritmo e efetuar a implementação em Python para
calcular a média dos seus alunos e verificar o nível de frequência. Os
alunos realizam duas avaliações: Aval1 e Aval2 , com o mesmo peso.
Calcular a média aritmética. Para aprovação os alunos precisam ter
pelo menos 75% de presença nas atividades acadêmicas. Utilizar os
dados da tabela a seguir para indicar o status acadêmico do aluno.
Imprimir um boletim, contendo a nota, o status de frequência e o status acadêmico. 

STATUS NOTA e FREQUÊNCIA                                STATUS ACADÊMICO 
Freqüência até 75%                                      Reprovado
Freqüência entre 75% e 100% e Nota até 4.0              Reprovado
Freqüência entre 75% e 100% e Nota de 4.0 até 6.0       Exame
Freqüência entre 75% e 100% e Nota entre 6.0 e 10.0     Aprovado
"""

exams = []

def switch():
    """Function to return student status."""
    if frequency < 75:
        return f" Notas {exams} | Média: {avarege} | Frequência {frequency}% | Status: Reprovado"
    elif avarege < 4:
        return f" Notas {exams} | Média: {avarege} | Frequência {frequency}% | Status: Reprovado"
    elif (avarege >= 4) and (avarege < 6):
        return f" Notas {exams} | Média: {avarege} | Frequência {frequency}% | Status: Exame"
    elif avarege >= 6:
        return f" Notas {exams} | Média: {avarege} | Frequência {frequency}% | Status: Aprovado"

for i in range(2):
    while True:
        try:
            exams.append(float(input(f"Nota da {i+1}ª avaliação: ")))
            break
        except ValueError:
            print("Por favor utilizar somente numeros...")
    continue

while True:
    try:
        frequency = float(input("Frequencia academica % : "))
        break
    except ValueError:
        print("Por favor utilizar somente numeros...")
    continue

avarege = float(sum(exams)/len(exams))

print(switch())
