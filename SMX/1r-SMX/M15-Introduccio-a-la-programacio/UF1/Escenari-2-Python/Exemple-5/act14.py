aparell=float(input('Quants W gasta per hora el teu aparrell? '))
hores=float(input('Quantes hores el fas servir? '))
cost=(aparell)*(hores)*365*0.124985
consum=(aparell)*(hores)*0.001
print(f'El cost anual és {cost}€')
print(f'El consum en un any és {consum}KW')