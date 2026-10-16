num1_str = str(input('Introdueix el numero en base 10:'))
num1_int = int( num1_str )

num1_base2 = bin(num1_int)
print(f'El {num1_str} en base 2 és {num1_base2}')

num1_base8 = oct(num1_int)
print(f'El {num1_str} en base 8 és {num1_base8}')

num1_base16 = hex(num1_int)
print(f'El {num1_str} en base 16 és {num1_base16}')