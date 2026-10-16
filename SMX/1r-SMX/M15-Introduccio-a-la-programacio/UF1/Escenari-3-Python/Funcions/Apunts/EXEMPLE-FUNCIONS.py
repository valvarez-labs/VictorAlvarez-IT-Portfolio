
############## DEFINICIÓ DE FUNCIONS (SEMPRE PRIMER!)
def hola(algu):
    """
    Imprimeix per pantalla un salutació, dirigida a la persona que indiquem per paràmetre (o argument).
        
    Parameters (variables LOCALS!)
    ----------
    algu  str   El nom de la persona a saludar
    """
    print("Hola ", algu,"!")
    print("Estic programant en Python.")

    # En aquest cas NO retornem cap valor!
#<----------------- Final FUNCIÓ hola (el següent sense tabulació)


def suma(param1,param2):
    """
    Calcula la suma de dos operands passats com a paràmetre
    
    Parameters
    ----------
    param1 : int
        El primer operand de la suma
    param2 : int
        El segon operand de la suma
    
    Returns
    -------
    int
        El resultat de la suma dels dos operands
    """
    resultat=param1+param2
    return resultat   # return param1+param2
#<----------------- Final FUNCIÓ suma

########### COS DEL PROGRAMA PRINCIPAL (Variables GLOBALS):
########### AQUI COMENÇA EL PROGRAMA PRINCIPAL

# Veiem diferents formes d'invocar, cridar la mateixa funció

# Exemple 1:
hola ("Pere")  # Invocació de la funció ()
help(hola)     # Per veure la descripció de la funció

# Exemple 2:
test_retorn=hola("Joan")   # Invocació/crida de la funció "hola" amb valor fixe "Joan" (com a paràmetre)
# Test de mostrar el que retorna la funció "hola"
print("Test retorn:",test_retorn,"\n")    # La funció retorna "None", es a dir RES (cap valors), i és el que mostrarà amb el "print"

# Exemple 3:
nom = input("Nom de la persona a saludar:")
hola(nom)   # Invocació/crida de la funció "hola" amb variable com a paràmetre



# Exemple 4:
calculosuma=suma(5,4)  # 5 -> parámetre concret de tipus "int"
print ("SUMA 5+4:",calculosuma)

# Exemple 5:
a=3
b=12
print (f"SUMA {param1}+{param2}:",suma(a,b))  # a -> el paràmetre és una "variable" és de tipus 'int'

