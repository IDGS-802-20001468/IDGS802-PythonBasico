'''
Leer un numero por ejemplo 5 

5 x 1 = 5 

'''

num1 = int(input('Dame un numero:'))
for var in range(1,11):
    print('{} X {} = {}'.format(num1, var, (num1*var)))
