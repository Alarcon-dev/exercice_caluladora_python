"""
calculadora en python: debe permitir hacer operaciones básicas

"""
print('Bienvenido a PythonCalculator')  
salida = 0 
number_1 = False
number_2 = False
while salida == 0:
    continuar = input("Digita 0 para salir o digita 1 para continuar: ")
    if continuar == "0":
        salida = 1
    
    elif continuar == "1":
        
        n1 = input('ingresar el primer numero: ')
        n2 = input('ingresa el segundo numero: ')
        
        number_1 = int(n1)
        number_2 = int(n2)
        
        if isinstance(number_1, int)  and isinstance(number_2, int) :
            operation = input('digita el simbolo de tu operación: + - * /: ')
            
            if operation == "+":
                result = "Resultado: " + str(number_1 + number_2)
                print(result)
            
            if operation == "-":
                result = "Resultado: " + str(number_1 - number_2)
                print(result)
            
            if operation == "*":
                result = "Resultado: " + str(number_1 * number_2)
                print(result)
            
            if operation == "/" and number_1 != 0 and number_2 != 0:
                result = "Resultado: " + str(number_1 / number_2)
                print(round(result))
            elif number_1 == 0 and number_2 == 0: 
                print("No se puede dividir por cero ingresa números válidos")
        else:
            print('asegurate de agregar los numeros solicitados')
    else:
        salida = 1


        