class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def mostrar_area(self):
        area = self.calcular_area()
        print(f"El área del triángulo es: {area}")

def main():
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    
    triangulo = Triangulo(base, altura)
    triangulo.mostrar_area()

if __name__ == "__main__":
    main()