variable1=int(input("Escriu un número de mes:"))

def calcula_dies_del_mes(mes):
    """
    Aquesta funció rep el número del mes i imprimeix el nombre de dies que té aquest mes.
    """
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        print(f"El mes {mes} té 31 dies")
    elif mes in [4, 6, 9, 11]:
        print(f"El mes {mes} té 30 dies")
    elif mes == 2:
        print(f"El mes {mes} té 28 o 29 dies depenent de l'any")
    else:
        print(f"El número de mes {mes} no és vàlid")

def calcula_dies_del_mes(variable1)


