print("--------------------------")
print("JOC DEL MAREJAT               |")
print("--------------------------")

x=0
y=0

x_objectiu=int(input("Introdueix la coordenada X:"))
y_objectiu=int(input("Introdueix la coordenada Y:"))
print(f'El marejat es troba en ({x},{y}) i ha d arribar a ({x_objectiu},{y_objectiu})')

while x != x_objectiu or y != y_objectiu:
    direcció=input("Cap a on va? (N,O,S o E): ")
    passos=input("Quants passos? ")

    if direcció == 'N':
        y + passos

    elif direcció == 'E':
        x + passos
    
    elif direcció == 'S':
        y - passos

    elif direcció == 'O':
        x - passos 

    else:
        print("EL marejat no reconeix aquesta direcció!")

    
while x == x_objectiu and y == y_objectiu:
    print(f'El marejat ja ha arribat a ({x_objectiu}, {y_objectiu})!!')