"""
9) O IMC (Índice de Massa Corporal) foi criado pelo matemático Lambert
Quételet para permitir a padronização para a análise do peso de uma
pessoa. O cálculo é muito simples:

Onde o PESO é em Kg e a ALTURA em metros. O valor do IMC pode ser
classificado de acordo com os dados listados na tabela ao lado.
Desenvolver um algoritmo e efetuar a implementação em Python, para calcular
o IMC e emitir a mensagem com a correspondente classificação.
"""

def switch(imc_sw):
    """Function to return IMC menssage."""
    if imc_sw < 18.5:
        return f"IMC de {imc_sw} | Classificação: Baixo pesso"
    elif (imc_sw >=18.5) and (imc_sw < 24.99) :
        return f"IMC de {imc_sw} | Classificação: Normal"
    elif (imc_sw >=25) and (imc_sw < 29.99) :
        return f"IMC de {imc_sw} | Classificação: Sobrepeso"
    elif imc_sw >= 30:
        return f"IMC de {imc_sw} | Classificação: Obesidade"

while True:
    try:
        weight = float(input("Informe seu peso: "))
        height = float(input("Informe sua altura: "))
        break
    except ValueError:
        print("Por favor utilizar somente numero...")
    continue

imc = round(weight/(height ** 2),2)

print(switch(imc))
