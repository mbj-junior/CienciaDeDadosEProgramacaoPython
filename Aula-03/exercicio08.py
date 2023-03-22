"""
8) Em Rapidópolis, a prefeitura proporciona desconto do IPTU em função da idade do imóvel:
IDADE < 5 anos 0%
IDADE >=5 e IDADE < 20 15%
IDADE >=20 e IDADE < 40 25%
IDADE >= 40 30% 

Desenvolver um algoritmo e realizar a implementação em Python, para efetuar a leitura do ano
de construção do imóvel, do ano atual, calcular a idade do imóvel e calcular o percentual 
de desconto do IPTU.
"""

from datetime import datetime
CURRENT_YEAR = datetime.today().year

def switch(age):
    """Function to return deduction."""
    if age < 5:
        return f"Propriedade com {age} anos 0% de desconto"
    elif (age >=5) and (age < 20) :
        return f"Propriedade com {age} anos 15% de desconto"
    elif (age >=20) and (age < 40) :
        return f"Propriedade com {age} anos 25% de desconto"
    elif age >= 40:
        return f"Propriedade com {age} anos 30% de desconto"

while True:
    try:
        year_construction_property = int(input("Ano de construção do imóvel: "))
        break
    except ValueError:
        print("Por favor utilizar somente numero...")
    continue

property_age = CURRENT_YEAR - year_construction_property

print(switch(property_age))
