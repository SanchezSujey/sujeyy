def leer_datos():
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    return base, altura

def calcular_area(base, altura):
    return (base * altura) / 2

def mostrar_resultado(area):
    print(f"El área del triángulo es: {area}")

def main():
    base, altura = leer_datos()
    area = calcular_area(base, altura)
    mostrar_resultado(area)

if __name__ == "__main__":
    main()