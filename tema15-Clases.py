import os

class OperasBas:
    #declaracion de propiedades 
    res = 0

    #declaracion de constructor
    def __init__(self):
        pass

    #declaracion de metodos de clase 
    def suma(self, a, b):
        self.res = a + b 
        os.system('cls')
        print("La suma es: {} ".format(self.res))

    def resta(self, a, b):
        self.res = a - b
        os.system('cls')
        print("La resta es: {} ".format(self.res))
    
    def division(self, a, b):
        self.res = a / b 
        os.system('cls')
        print("La division es: {} ".format(self.res))
    
    def multi(self, a, b):
        self.res = a * b 
        os.system('cls')
        print("La multiplicacion es: {} ".format(self.res))

    def menu(self):
        print('Ingresa el numero de la opcion que desees realizar')
        print('1- Suma')
        print('2- Resta')
        print('3- Multiplicacion')
        print('4- Division')
        print('5- Salir')
    

def main():
        os.system('cls')
        obj = OperasBas()   
        operacion = 0
        while operacion < 5:
            obj.menu()
            operacion = int (input())
            if(operacion < 5):
                num1 = int(input("Ingresa el primer numero "))
                num2 = int(input("Ingresa el segundo numero "))
                     
            if(operacion == 1):
                obj.suma(num1, num2)
            elif(operacion == 2):
                obj.resta(num1, num2)
            elif(operacion == 3):
                obj.multi(num1, num2)
            elif(operacion == 4):
                obj.division(num1, num2)
            

if __name__ == "__main__":
        main()

    