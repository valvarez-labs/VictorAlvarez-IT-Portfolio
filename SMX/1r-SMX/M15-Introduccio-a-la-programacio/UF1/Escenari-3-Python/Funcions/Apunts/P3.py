# Bucles

# for i in range()

for i in range(0,2): # Últim valor no s'inclou
    print(i)

for i in range(10,0,-1): # 1r Valor (Inici), 2n Valor (Final), 3è Valor opcional (Pas)
    print(i)

variable = 10


# while (condicio):

while variable >= 0:
    print(variable)
    if variable == 5:
        break           # trencar el bucle
    variable -= 1 # variable = variable - 1

print("Fi while")