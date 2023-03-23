"""
2) Desenvolva um algoritmo e efetue a implementação em Python para 
ler n valores (sendo n informado pelo usuário) e imprimir o valor médio, 
o maior e o menor valor.
"""

numbers = []

def average(list_numbers):
    """Calculate the avarege of a list"""
    return sum(list_numbers) / len(list_numbers)

while True:
    try:
        number_repetitions = int(input("Quantidade de numeros: "))
        if number_repetitions == 0:
            raise RecursionError("Não pode ser 0")
        if number_repetitions < 0:
            raise RecursionError("Não pode ser negativo")
        break
    except RecursionError as error:
        print("Valor inválido:", error)
    except ValueError as error:
        print("Utilizar somente numeros")
    continue


for i in range(number_repetitions):
    while True:
        try:
            numbers.append(float(input(f"{i+1}º numero: ")))
            break
        except ValueError:
            print("Por favor utilizar somente numeros...")
    continue

print("")
print(f"Valor médio: {average(numbers)}")
print(f"Maior valor: {max(numbers)}")
print(f"Menor valor: {min(numbers)}")
print("")
