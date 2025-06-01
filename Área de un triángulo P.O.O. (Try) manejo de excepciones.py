class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def mostrar_area(self):
        area = self.calcular_area()
        print(f"El área del triángulo es: {area:.2f}")

def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El valor debe ser mayor a cero.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")

def main():
    print("Cálculo del área de un triángulo")
    
    base = leer_float("Ingresa la base del triángulo: ")
    altura = leer_float("Ingresa la altura del triángulo: ")

    triangulo = Triangulo(base, altura)
    triangulo.mostrar_area()

if __name__ == "__main__":
    main()