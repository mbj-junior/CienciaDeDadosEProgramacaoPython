"""
1) Os comerciantes do Mercado Municipal de Rapidópolis estabeleceram 
um percentual de margem mínima de lucro em função do valor do produto:

Valor do Produto (VP) < R$ 25,00        Lucro de 100%
R$ 25,00 ≤ VP < R$ 100,00               Lucro de 70%
R$ 100,00 ≤ VP < R$ 500,00              Lucro de 60%
R$ 500,00 ≤ VP < R$ 1000,00             Lucro de 50%
VP ≥ R$ 1000,00                         Lucro de 40%

Desenvolver um algoritmo para efetuar a leitura do valor do produto 
e apontar o percentual mínimo de lucro. Efetue a implementação em 
Python tratando exceções de dados durante a execução do programa.
"""

def profit():
    """Function to return profit."""
    if product_price < 25:
        return f"Lucro de 100% = {product_price}"
    elif (product_price >= 25) and (product_price < 100):
        return f"Lucro de 70% = {product_price * 0.7}"
    elif (product_price >= 100) and (product_price < 500):
        return f"Lucro de 60% = {product_price * 0.6}"
    elif (product_price >= 500) and (product_price < 1000):
        return f"Lucro de 50% = {product_price * 0.5}"
    elif product_price >= 1000:
        return f"Lucro de 40% = {product_price * 0.4}"

while True:
    try:
        product_price = float(input("Valor do produto: "))
        if product_price == 0:
            raise RecursionError("Não pode ser 0")
        if product_price < 0:
            raise RecursionError("Não pode ser negativo")
        break
    except RecursionError as error:
        print("Valor inválido:", error)
    except ValueError as error:
        print("Utilizar somente numeros")
    continue

print(profit())
