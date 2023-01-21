
num1 = 20
num2 = 0

#print("La division de {0} entre {1} es {2}".format(num1, num2,(num1/num2)))

try: 
    resultado = num1/num2
except ZeroDivisionError:
    print("Error en el programa")
finally:
    print("Yo siempre aparezco")