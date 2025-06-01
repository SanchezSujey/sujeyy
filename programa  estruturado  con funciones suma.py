def leer_numero(mensaje):
    return float(input(mensaje))

def sumar(a, b):
    return a + b


def main():
    print("Programa que suma dos números\n")
    
    num1 = leer_numero("Ingrese el primer número: ")
    num2 = leer_numero("Ingrese el segundo número: ")
    
    resultado = sumar(num1, num2)
    
    print(f"\nLa suma de {num1} y {num2} es: {resultado}")


if __name__ == "__main__":
    main()