class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def main():
    try:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))

        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores a cero.")

        triangulo = Triangulo(base, altura)
        area = triangulo.calcular_area()
        print(f"El área del triángulo es: {area:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()