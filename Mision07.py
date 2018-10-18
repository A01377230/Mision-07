#Jesús Roberto Herrera Vieyra A01377230
#Programa de selección entre division y encontrar el mayor con ciclos while


def calcularDivisor():
    dividendo = int(input("Teclea el dividendo: "))
    divisor = int(input("Teclee el divisor: "))
    cociente = 0
    residuo = dividendo

    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1
    print("El cociente de %d entre %d es: %d con residuo de %d" % (dividendo, divisor, cociente, residuo))


def encontrarMayor():

    numero = int(input("Teclea un número [-1 para salir]: "))
    mayor=numero

    if numero != -1:

        while numero != -1:

            if numero >= mayor:
                mayor = numero

            numero = int(input("Teclea un número [-1 para salir]: "))

        print("El mayor es: ", mayor)

    else:
        print("No puedo evaluar sin datos")


def leerOpcion():
    print("""
Mision 07. Ciclos while
Autor: Jesús Roberto Herrera Vieyra
Matrícula: A01377230
1. Calcular divisiones
2. Encontrar el mayor
3. Salir
""")
    opcion = int(input("Elija una opción "))
    return opcion


def main():

    opcion = leerOpcion()

    while opcion != 3:

        if opcion == 1:
            calcularDivisor()
            opcion = leerOpcion()

        elif opcion == 2:
            encontrarMayor()
            opcion = leerOpcion()

        else:
            print("Error, teclea 1, 2 o 3")
            opcion = leerOpcion()


    print("Gracias por usar este programa")


main()