"""
12) Desenvolver um algoritmo e efetuar a implementação em Python para calcular o valor
da função f(x). Atenção: NÃO É PERMITIDO EFETUAR A DIVISÃO POR ZERO.

f(x) = (4 * x**2 - 3 * x + 9)/x 

"""
def calculate():
    """Function to calculate."""
    result = (4 * (number_x**2) - 3 * (number_x + 9))/number_x
    return result



while True:
    try:
        number_x = float(input("Informe x: "))
        if number_x == 0:
            raise ValueError("Não pode ser 0")
    except ValueError as error:
        print("Valor inválido:", error)
    else:
        break

print(f"Resultado da função: {calculate()}")
