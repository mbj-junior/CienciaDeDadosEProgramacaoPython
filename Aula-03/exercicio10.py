"""
10) Desenvolver um algoritmo e efetuar a implementação em Python 
para ler 3 número e verificar se então em ordem crescente.
"""

numbers = []

for i in range(3):
    while True:
        try:
            numbers.append(float(input(f"{i+1}º numero: ")))
            break
        except ValueError:
            print("Por favor utilizar somente numeros...")
    continue


sorted_numbers = numbers.copy()

sorted_numbers.sort()

if numbers == sorted_numbers:
    print("Numeros em ordem crescente")
else:
    print("Numero não estão ordenados")
