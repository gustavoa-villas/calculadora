
print(""" Hola Bienvenido a la calculadora """)


def obtener_datos():

    try:
        cantidad = input("Cantidad de números a sumar: ")
    except ValueError:
        print("Debes ingresar un número entero")


def validacion (decision, menu):

    valor = True

    while valor == True:

        if decision == 0:

            print("Ha salido exitosamente")
            valor == False
            return False

        elif decision == 1:

            menu()
            return True

        else:

            print("opcion no valida")
            decision = int(input("¿Desea regresar al menu principal? 1 = sí, 0 = salir: "))
            activo = validacion(decision, menu)


def menu ():
    print("""

    1. suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Division entera
    6. Potencia
    7. Modulo
    8. Exit

    """)

menu()

activo = True

while activo:

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:

        print(" Ha escogido suma ")
        obtener_datos()
        contador = 0
        
        datos = []

        while contador < obtener_datos:
            ingreso_datos = int(input("ingrese el numero que desea sumar: "))

            datos.append(ingreso_datos)

            contador = contador + 1
        suma = 0
        for dato in datos:
            suma = suma + dato 

        print(f"El resultado de la suma de los numero es: {suma}")

    if opcion == 2:

        print(" Ha escogido resta ")
        cantidad = int(input("cantidad de numeros a resta: "))
        contador = 0
        
        datos = []

        while contador < cantidad:
            ingreso_datos = int(input("ingrese el numero que desea sumar: "))

            datos.append(ingreso_datos)

            contador = contador + 1
        resta = 0
        for dato in datos:
            resta = resta - dato 

        print(f"El resultado de la resta de los numero es: {resta}")
    
    if opcion == 3:

        print(" Ha escogido multiplicacion ")
        cantidad = int(input("cantidad de numeros a multiplicacion: "))
        contador = 0

        datos = []

        while contador < cantidad:

            ingreso_datos = int(input("ingrese el numero que desea multipliar: "))

            datos.append(ingreso_datos)

            contador = contador + 1

        multiplicar = 1

        for dato in datos:
            multiplicar = multiplicar * dato
        
        print(f"El resultado de la multiplicacion es: {multiplicar}")

    if opcion == 4:

        print(" Ha escogido Division ")
        cantidad = int(input("cantidad de numeros a dividir: "))
        contador = 0

        datos = []

        while contador < cantidad:

            ingreso_datos = int(input("ingrese el numero que desea dividir: "))

            datos.append(ingreso_datos)

            contador = contador + 1

        dividir = datos[0]

        for dato in datos[1:]:
            dividir = dividir / dato
        
        print(f"El resultado de la dividision es: {dividir}")

    if opcion == 5:

        print(" Ha escogido Division ")
        cantidad = int(input("cantidad de numeros a dividir: "))
        contador = 0

        datos = []

        while contador < cantidad:

            ingreso_datos = int(input("ingrese el numero que desea dividir: "))

            datos.append(ingreso_datos)

            contador = contador + 1

        dividir = datos[0]

        for dato in datos[1:]:
            dividir = dividir // dato
        
        print(f"El resultado de la dividision es: {dividir}")

    if opcion == 6:

        print(" Ha escogido Potencia ")
        numero = int(input("ingrese el numero que desea elevar a la potencia n: "))
        potencia = int(input("ingrese el valor de n: "))

        resultado = numero ** potencia
        
        print(f"El resultado de la Potencia es: {resultado}")

    if opcion == 7:

        print(" Residuo de la division que desea conocer: ")
        numero_1 = int(input("ingrese el primer numero"))
        numero_2 = int(input("ingrese el segundo numero"))

        resultado = numero_1 % numero_2
        
        print(f"El residuo de la division es: {resultado}")

    elif opcion == 8:

        print("Ha salido del menu")
        activo = False

    if activo:
        decision = int(input("¿Desea regresar al menu principal? 1 = sí, 0 = salir: "))
        activo = validacion(decision, menu)    



    